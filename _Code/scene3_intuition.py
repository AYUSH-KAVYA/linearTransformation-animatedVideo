"""
Scene 3: Visual Intuition — Grid Deformation (~66 seconds)
Demonstrates 4 fundamental 2D linear transformations one by one:
  1. Rotation (90 deg CCW)
  2. Horizontal Scaling (2x)
  3. Horizontal Shear
  4. Reflection (across y-axis)
Tracks basis vectors î, ĵ, sample vector v=(1,1), unit square, and orientation arc.
"""

from manim import *
import numpy as np
from config import (
    BG_COLOR,
    CARD_BORDER,
    COLOR_ACCENT,
    COLOR_AREA,
    COLOR_AREA_OUT,
    COLOR_I,
    COLOR_J,
    COLOR_MUTED,
    COLOR_NEG,
    COLOR_TEXT,
    COLOR_V,
)
from helpers import (
    build_orientation_arc,
    color_coded_matrix,
    interp_matrix,
    make_card,
    make_header,
    make_plane_pair,
    place_tip_label,
    vec_arrow,
)


class VisualIntuitionScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = make_header("Four Fundamental Transformations", "Scene 3 • Visual Intuition")
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.9)

        # Right-hand plane: x in [-3, 3], y in [-3, 3]
        ghost, active, origin_pt = make_plane_pair(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            unit_size=0.88,
            center=RIGHT * 2.45 + DOWN * 0.28,
            show_numbers=True,
        )

        # Shared tracked state
        mat_start = np.eye(2)
        mat_end = np.eye(2)
        rot_angle = None
        alpha = ValueTracker(0.0)

        def current_mat():
            return interp_matrix(mat_start, mat_end, alpha.get_value(), rot_angle)

        unit_sq = always_redraw(lambda: Polygon(
            *[ghost.c2p(*(current_mat() @ p)) for p in [(0, 0), (1, 0), (1, 1), (0, 1)]],
            stroke_color=COLOR_AREA_OUT if alpha.get_value() > 0.2 else COLOR_AREA,
            stroke_width=2.2,
            fill_color=COLOR_AREA_OUT if alpha.get_value() > 0.2 else COLOR_AREA,
            fill_opacity=0.25,
        ))
        orient_arc = always_redraw(lambda: build_orientation_arc(
            ghost,
            current_mat() @ np.array([1.0, 0.0]),
            current_mat() @ np.array([0.0, 1.0]),
            radius=0.52,
            color=COLOR_NEG if np.linalg.det(current_mat()) < 0 else COLOR_ACCENT,
        ))
        i_vec = always_redraw(lambda: vec_arrow(ghost, current_mat() @ np.array([1.0, 0.0]), COLOR_I))
        j_vec = always_redraw(lambda: vec_arrow(ghost, current_mat() @ np.array([0.0, 1.0]), COLOR_J))
        v_vec = always_redraw(lambda: vec_arrow(ghost, current_mat() @ np.array([1.0, 1.0]), COLOR_V, stroke_width=3.8))

        i_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\hat{\imath}", font_size=26, color=COLOR_I),
            ghost, current_mat() @ np.array([1.0, 0.0]), offset_scale=0.3,
        ))
        j_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\hat{\jmath}", font_size=26, color=COLOR_J),
            ghost, current_mat() @ np.array([0.0, 1.0]), offset_scale=0.3,
        ))
        v_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\mathbf{v}", font_size=24, color=COLOR_V),
            ghost, current_mat() @ np.array([1.0, 1.0]), offset_scale=0.32,
        ))

        # Intro left legend card
        legend_title = Text("Tracking Every Point", font_size=24, weight=BOLD, color=COLOR_ACCENT)
        legend_items = VGroup(
            Text("• Green arrow = î = (1, 0)", font_size=20, color=COLOR_I),
            Text("• Red arrow = ĵ = (0, 1)", font_size=20, color=COLOR_J),
            Text("• Gold arrow = v = (1, 1)", font_size=20, color=COLOR_V),
            Text("• Shaded tile = Unit Square", font_size=20, color=COLOR_AREA),
            Text("• Curved arc = Orientation (î → ĵ)", font_size=20, color=COLOR_ACCENT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        legend_card = make_card(
            VGroup(legend_title, legend_items).arrange(DOWN, aligned_edge=LEFT, buff=0.28),
            border_color=CARD_BORDER,
            pad=0.28,
        ).move_to(LEFT * 3.85 + DOWN * 0.25)

        self.play(Create(ghost), Create(active), FadeIn(legend_card), run_time=1.4)
        self.play(
            Create(unit_sq), Create(orient_arc),
            GrowArrow(i_vec), GrowArrow(j_vec), GrowArrow(v_vec),
            FadeIn(i_lbl), FadeIn(j_lbl), FadeIn(v_lbl),
            run_time=1.3,
        )
        self.wait(3.8)
        self.play(FadeOut(legend_card), run_time=0.6)  # ~8s

        demos = [
            {
                "name": "1. Rotation (90° CCW)",
                "matrix": np.array([[0.0, -1.0], [1.0, 0.0]]),
                "rot_angle": PI / 2,
                "accent": COLOR_V,
                "effects": [
                    "• Lengths: Preserved (||v|| unchanged)",
                    "• Direction: Every vector turns +90°",
                    "• Area: Scale factor det = +1",
                    "• Orientation: Preserved (CCW)",
                ],
                "v_out": "(1, 1)  →  (-1, 1)",
            },
            {
                "name": "2. Horizontal Stretch (2×)",
                "matrix": np.array([[2.0, 0.0], [0.0, 1.0]]),
                "rot_angle": None,
                "accent": COLOR_ACCENT,
                "effects": [
                    "• Lengths: x-components double",
                    "• Direction: Vectors tilt toward x-axis",
                    "• Area: Scale factor det = +2 (doubles)",
                    "• Orientation: Preserved (CCW)",
                ],
                "v_out": "(1, 1)  →  (2, 1)",
            },
        ]

        for idx, d in enumerate(demos):
            mat = d["matrix"]
            mat_start = np.eye(2)
            mat_end = mat
            rot_angle = d["rot_angle"]
            alpha.set_value(0.0)

            panel_title = Text(d["name"], font_size=26, weight=BOLD, color=d["accent"])
            m_tex = VGroup(
                MathTex(r"A = ", font_size=34, color=COLOR_TEXT),
                color_coded_matrix(mat[0, 0], mat[0, 1], mat[1, 0], mat[1, 1], font_size=34),
            ).arrange(RIGHT, buff=0.14)
            col_hint = VGroup(
                Text("Col 1 = T(î)", font_size=17, color=COLOR_I),
                Text("•", font_size=17, color=COLOR_MUTED),
                Text("Col 2 = T(ĵ)", font_size=17, color=COLOR_J),
            ).arrange(RIGHT, buff=0.18)

            eff_lines = VGroup(
                *[Text(line, font_size=19, color=COLOR_TEXT) for line in d["effects"]]
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

            v_map_txt = Text(f"Sample v:  {d['v_out']}", font_size=19, weight=BOLD, color=COLOR_V)

            left_content = VGroup(panel_title, m_tex, col_hint, eff_lines, v_map_txt).arrange(
                DOWN, aligned_edge=LEFT, buff=0.26
            )
            left_card = make_card(left_content, border_color=d["accent"], pad=0.26)
            left_card.move_to(LEFT * 3.85 + DOWN * 0.25)

            self.play(FadeIn(left_card, shift=RIGHT * 0.2), run_time=0.8)
            self.wait(1.0)

            if rot_angle is not None:
                self.play(
                    Rotate(active, angle=rot_angle, about_point=origin_pt),
                    alpha.animate.set_value(1.0),
                    run_time=2.8,
                )
            else:
                self.play(
                    ApplyMatrix(mat, active, about_point=origin_pt),
                    alpha.animate.set_value(1.0),
                    run_time=2.8,
                )
            self.wait(6.0)

            # Reset grid cleanly except after the final demo
            if idx < len(demos) - 1:
                if rot_angle is not None:
                    self.play(
                        Rotate(active, angle=-rot_angle, about_point=origin_pt),
                        alpha.animate.set_value(0.0),
                        FadeOut(left_card),
                        run_time=1.8,
                    )
                else:
                    inv = np.linalg.inv(mat)
                    self.play(
                        ApplyMatrix(inv, active, about_point=origin_pt),
                        alpha.animate.set_value(0.0),
                        FadeOut(left_card),
                        run_time=1.8,
                    )
                self.wait(0.8)
            else:
                self.play(FadeOut(left_card), run_time=0.8)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
