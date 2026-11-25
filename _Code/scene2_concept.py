"""
Scene 2: Concept Introduction (~62 seconds)
Covers Learning Objective, Notation definitions, Additivity & Homogeneity
(with visual parallelogram demo + nonlinear contrast), and Matrix Representation.
"""

from manim import *
import numpy as np
from config import (
    BG_COLOR,
    CARD_BORDER,
    COLOR_ACCENT,
    COLOR_I,
    COLOR_J,
    COLOR_MUTED,
    COLOR_NEG,
    COLOR_TEXT,
    COLOR_V,
    COLOR_W,
)
from helpers import (
    color_coded_matrix,
    interp_matrix,
    make_card,
    make_header,
    make_plane_pair,
    place_tip_label,
    vec_arrow,
)


class ConceptIntroScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. HEADER & LEARNING OBJECTIVE (0:00 – 0:11) ───────────────────
        header = make_header("What Is a Linear Transformation?", "Scene 2 • Definition")
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.9)

        obj_title = Text("Learning Objective", font_size=22, weight=BOLD, color=COLOR_V)
        obj_body = Text(
            "By the end of this video, you will be able to interpret any 2 × 2 matrix\n"
            "as a geometric transformation — predicting vector images, area scaling,\n"
            "and orientation directly from its entries.",
            font_size=23,
            color=COLOR_TEXT,
            line_spacing=1.35,
        )
        obj_group = VGroup(obj_title, obj_body).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        obj_card = make_card(obj_group, border_color=COLOR_V, pad=0.3).move_to(UP * 1.1)

        # Notation bar below objective
        not_title = Text("Notation Used Throughout", font_size=20, weight=BOLD, color=COLOR_ACCENT)
        not_math = MathTex(
            r"\mathbb{R}^2 \text{: 2D plane}"
            r"\qquad \mathbf{u}, \mathbf{v} \in \mathbb{R}^2 \text{: vectors}"
            r"\qquad c \in \mathbb{R} \text{: scalar}"
            r"\qquad \hat{\imath} = \begin{bmatrix}1\\0\end{bmatrix},\; \hat{\jmath} = \begin{bmatrix}0\\1\end{bmatrix}",
            font_size=26,
            color=COLOR_TEXT,
        )
        not_group = VGroup(not_title, not_math).arrange(DOWN, buff=0.22)
        not_card = make_card(not_group, border_color=CARD_BORDER, pad=0.26).move_to(DOWN * 1.45)

        self.play(FadeIn(obj_card, shift=UP * 0.2), run_time=1.3)
        self.wait(3.8)
        self.play(FadeIn(not_card, shift=UP * 0.2), run_time=1.3)
        self.wait(3.6)

        self.play(FadeOut(obj_card), FadeOut(not_card), run_time=0.7)  # ~11.6s

        # ── 2. FORMAL AXIOMS + VISUAL ADDITIVITY & HOMOGENEITY (0:11 – 0:38)
        left_title = MathTex(r"T : \mathbb{R}^2 \to \mathbb{R}^2 \text{ is linear if:}", font_size=30, color=COLOR_ACCENT)
        left_title.move_to(LEFT * 3.5 + UP * 2.15)

        p1_lbl = Text("1. Additivity (preserves sums)", font_size=21, weight=BOLD, color=COLOR_I)
        p1_eq = MathTex(r"T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})", font_size=30, color=COLOR_TEXT)
        p1_card = make_card(VGroup(p1_lbl, p1_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.16), border_color=COLOR_I, pad=0.22)
        p1_card.next_to(left_title, DOWN, buff=0.3).align_to(left_title, LEFT)

        p2_lbl = Text("2. Homogeneity (preserves scaling)", font_size=21, weight=BOLD, color=COLOR_J)
        p2_eq = MathTex(r"T(c\,\mathbf{u}) = c\,T(\mathbf{u})", font_size=30, color=COLOR_TEXT)
        p2_card = make_card(VGroup(p2_lbl, p2_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.16), border_color=COLOR_J, pad=0.22)
        p2_card.next_to(p1_card, DOWN, buff=0.28).align_to(p1_card, LEFT)

        origin_note = MathTex(
            r"\text{Consequence: } T(\mathbf{0}) = T(0\cdot\mathbf{u}) = \mathbf{0}",
            font_size=24,
            color=COLOR_MUTED,
        ).next_to(p2_card, DOWN, buff=0.3).align_to(p2_card, LEFT)

        # Right mini plane for Additivity demo
        ghost, active, origin_pt = make_plane_pair(
            x_range=(-1, 4, 1),
            y_range=(-1, 4, 1),
            unit_size=0.92,
            center=RIGHT * 3.2 + DOWN * 0.25,
            show_numbers=True,
        )

        alpha = ValueTracker(0.0)
        mat_i = np.eye(2)
        mat_m = np.array([[1.0, 0.5], [0.2, 1.0]])
        u_coords = np.array([1.5, 0.5])
        v_coords = np.array([0.5, 1.5])
        sum_coords = u_coords + v_coords  # (2.0, 2.0) -> maps to (3.0, 2.4)

        u_vec = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_m, alpha.get_value()) @ u_coords, COLOR_I))
        v_vec = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_m, alpha.get_value()) @ v_coords, COLOR_J))
        sum_vec = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_m, alpha.get_value()) @ sum_coords, COLOR_V))

        # Parallelogram dashed legs
        para_u_v = always_redraw(lambda: DashedLine(
            ghost.c2p(*(interp_matrix(mat_i, mat_m, alpha.get_value()) @ u_coords)),
            ghost.c2p(*(interp_matrix(mat_i, mat_m, alpha.get_value()) @ sum_coords)),
            color=COLOR_J,
            stroke_width=2.2,
        ))
        para_v_u = always_redraw(lambda: DashedLine(
            ghost.c2p(*(interp_matrix(mat_i, mat_m, alpha.get_value()) @ v_coords)),
            ghost.c2p(*(interp_matrix(mat_i, mat_m, alpha.get_value()) @ sum_coords)),
            color=COLOR_I,
            stroke_width=2.2,
        ))

        u_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\mathbf{u}" if alpha.get_value() < 0.5 else r"T(\mathbf{u})", font_size=24, color=COLOR_I),
            ghost,
            interp_matrix(mat_i, mat_m, alpha.get_value()) @ u_coords,
            offset_scale=0.3,
        ))
        v_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\mathbf{v}" if alpha.get_value() < 0.5 else r"T(\mathbf{v})", font_size=24, color=COLOR_J),
            ghost,
            interp_matrix(mat_i, mat_m, alpha.get_value()) @ v_coords,
            offset_scale=0.3,
        ))
        sum_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\mathbf{u}+\mathbf{v}" if alpha.get_value() < 0.5 else r"T(\mathbf{u}+\mathbf{v})", font_size=24, color=COLOR_V),
            ghost,
            interp_matrix(mat_i, mat_m, alpha.get_value()) @ sum_coords,
            offset_scale=0.36,
        ))

        self.play(Write(left_title), Create(ghost), Create(active), run_time=1.3)
        self.play(FadeIn(p1_card, shift=RIGHT * 0.2), run_time=1.1)
        self.play(
            GrowArrow(u_vec), GrowArrow(v_vec),
            Create(para_u_v), Create(para_v_u),
            GrowArrow(sum_vec),
            FadeIn(u_lbl), FadeIn(v_lbl), FadeIn(sum_lbl),
            run_time=1.6,
        )
        self.wait(2.2)

        # Animate T acting on the parallelogram!
        self.play(
            ApplyMatrix(mat_m, active, about_point=origin_pt),
            alpha.animate.set_value(1.0),
            run_time=2.6,
        )
        self.wait(2.5)

        # Now highlight Homogeneity + live scaling check on the same grid!
        self.play(FadeIn(p2_card, shift=RIGHT * 0.2), run_time=1.1)
        self.wait(1.4)

        # Show c = 1.5 scaling on transformed u -> T(1.5 u) = 1.5 T(u)
        c_scale = 1.45
        scaled_u = vec_arrow(ghost, (mat_m @ (c_scale * u_coords)), COLOR_W, stroke_width=4.0)
        scaled_lbl = place_tip_label(
            MathTex(r"T(c\mathbf{u}) = c\,T(\mathbf{u})", font_size=22, color=COLOR_W),
            ghost,
            mat_m @ (c_scale * u_coords),
            offset_scale=0.38,
        )
        self.play(GrowArrow(scaled_u), FadeIn(scaled_lbl), run_time=1.6)
        self.wait(2.4)

        self.play(FadeIn(origin_note), run_time=1.0)
        self.wait(2.8)

        # Clean up right plane and left cards before visual geometric rule
        self.play(
            FadeOut(left_title), FadeOut(p1_card), FadeOut(p2_card), FadeOut(origin_note),
            FadeOut(ghost), FadeOut(active),
            FadeOut(u_vec), FadeOut(v_vec), FadeOut(sum_vec),
            FadeOut(para_u_v), FadeOut(para_v_u),
            FadeOut(u_lbl), FadeOut(v_lbl), FadeOut(sum_lbl),
            FadeOut(scaled_u), FadeOut(scaled_lbl),
            run_time=0.8,
        )  # ~34s in scene
