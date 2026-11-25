"""
Scene 5: Interpretation — Determinant, Area & Orientation (~54 seconds)
Connects the algebra of det(A) = ad - bc back to geometry across 3 regimes:
  1. det > 0 : Area scales by det(A), orientation preserved (A = [[2,1],[1,3]], det = 5)
  2. det < 0 : Area scales by |det(B)|, orientation flipped (B = [[-1,1],[0,2]], det = -2)
  3. det = 0 : 2D plane collapses onto a 1D line, area -> 0, non-invertible (C = [[2,1],[4,2]], det = 0)
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
    COLOR_ZERO,
)
from helpers import (
    add_bg_pill,
    build_orientation_arc,
    color_coded_matrix,
    interp_matrix,
    make_card,
    make_header,
    make_plane_pair,
    place_tip_label,
    vec_arrow,
)


class InterpretationScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = make_header("Geometric Meaning of the Determinant", "Scene 5 • Interpretation")
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.9)

        # ── CASE 1 : det(A) = +5 > 0 ───────────────────────────────────────
        ghost1, active1, orig1 = make_plane_pair(
            x_range=(-1, 5, 1),
            y_range=(-1, 5, 1),
            unit_size=0.76,
            center=RIGHT * 3.15 + DOWN * 0.2,
            show_numbers=True,
        )

        mat_a = np.array([[2.0, 1.0], [1.0, 3.0]])
        alpha1 = ValueTracker(0.0)

        def cur1():
            return interp_matrix(np.eye(2), mat_a, alpha1.get_value())

        sq1 = always_redraw(lambda: Polygon(
            *[ghost1.c2p(*(cur1() @ p)) for p in [(0, 0), (1, 0), (1, 1), (0, 1)]],
            stroke_color=COLOR_AREA_OUT if alpha1.get_value() > 0.3 else COLOR_AREA,
            stroke_width=2.6,
            fill_color=COLOR_AREA_OUT if alpha1.get_value() > 0.3 else COLOR_AREA,
            fill_opacity=0.3,
        ))
        area_lbl1 = always_redraw(lambda: add_bg_pill(MathTex(
            r"\text{Area} = 1" if alpha1.get_value() < 0.5 else r"\text{Area} = 5",
            font_size=22,
            color=COLOR_TEXT,
        ).move_to(ghost1.c2p(*(cur1() @ np.array([0.5, 0.5]))))))

        arc1 = always_redraw(lambda: build_orientation_arc(
            ghost1, cur1() @ np.array([1.0, 0.0]), cur1() @ np.array([0.0, 1.0]),
            radius=0.5, color=COLOR_ACCENT,
        ))
        i1 = always_redraw(lambda: vec_arrow(ghost1, cur1() @ np.array([1.0, 0.0]), COLOR_I))
        j1 = always_redraw(lambda: vec_arrow(ghost1, cur1() @ np.array([0.0, 1.0]), COLOR_J))

        # Left panel for Case 1
        c1_title = Text("Case 1: Positive Determinant (det > 0)", font_size=23, weight=BOLD, color=COLOR_V)
        c1_formula = MathTex(
            r"\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc",
            font_size=30,
            color=COLOR_ACCENT,
        )
        c1_calc = MathTex(
            r"\det(A) = \det\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} = (2)(3) - (1)(1) = +5",
            font_size=28,
        )
        c1_notes = VGroup(
            Text("• Unit square (Area 1) → Parallelogram (Area 5)", font_size=20, color=COLOR_TEXT),
            Text("• Positive sign → Orientation preserved (CCW)", font_size=20, color=COLOR_I),
            Text("• Non-zero det → Reversible (invertible)", font_size=20, color=COLOR_ACCENT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        c1_card = make_card(
            VGroup(c1_title, c1_formula, c1_calc, c1_notes).arrange(DOWN, aligned_edge=LEFT, buff=0.28),
            border_color=COLOR_V,
            pad=0.26,
        ).move_to(LEFT * 3.45 + DOWN * 0.25)

        self.play(FadeIn(c1_card, shift=RIGHT * 0.2), Create(ghost1), Create(active1), run_time=1.3)
        self.play(Create(sq1), Write(area_lbl1), Create(arc1), GrowArrow(i1), GrowArrow(j1), run_time=1.2)
        self.wait(2.5)

        self.play(
            ApplyMatrix(mat_a, active1, about_point=orig1),
            alpha1.animate.set_value(1.0),
            run_time=3.0,
        )
        self.wait(6.5)

        self.play(
            FadeOut(c1_card), FadeOut(ghost1), FadeOut(active1),
            FadeOut(sq1), FadeOut(area_lbl1), FadeOut(arc1), FadeOut(i1), FadeOut(j1),
            run_time=0.7,
        )  # ~16.1s

        # ── CASE 2 : det(B) = -2 < 0 ───────────────────────────────────────
        ghost2, active2, orig2 = make_plane_pair(
            x_range=(-3, 3, 1),
            y_range=(-1, 3, 1),
            unit_size=0.86,
            center=RIGHT * 3.15 + DOWN * 0.2,
            show_numbers=True,
        )
        mat_b = np.array([[-1.0, 1.0], [0.0, 2.0]])
        alpha2 = ValueTracker(0.0)

        def cur2():
            return interp_matrix(np.eye(2), mat_b, alpha2.get_value())

        sq2 = always_redraw(lambda: Polygon(
            *[ghost2.c2p(*(cur2() @ p)) for p in [(0, 0), (1, 0), (1, 1), (0, 1)]],
            stroke_color=COLOR_NEG if np.linalg.det(cur2()) < 0 else COLOR_AREA,
            stroke_width=2.6,
            fill_color=COLOR_NEG if np.linalg.det(cur2()) < 0 else COLOR_AREA,
            fill_opacity=0.28,
        ))
        area_lbl2 = always_redraw(lambda: add_bg_pill(MathTex(
            r"\text{Area} = 1" if alpha2.get_value() < 0.5 else r"\text{Area} = |-2| = 2",
            font_size=20,
            color=COLOR_TEXT,
        ).move_to(ghost2.c2p(*(cur2() @ np.array([0.5, 0.5]))))))

        arc2 = always_redraw(lambda: build_orientation_arc(
            ghost2, cur2() @ np.array([1.0, 0.0]), cur2() @ np.array([0.0, 1.0]),
            radius=0.48,
            color=COLOR_NEG if np.linalg.det(cur2()) < 0 else COLOR_ACCENT,
        ))
        i2 = always_redraw(lambda: vec_arrow(ghost2, cur2() @ np.array([1.0, 0.0]), COLOR_I))
        j2 = always_redraw(lambda: vec_arrow(ghost2, cur2() @ np.array([0.0, 1.0]), COLOR_J))

        c2_title = Text("Case 2: Negative Determinant (det < 0)", font_size=23, weight=BOLD, color=COLOR_NEG)
        c2_mat = VGroup(
            MathTex(r"B = ", font_size=30),
            color_coded_matrix(-1, 1, 0, 2, font_size=30),
        ).arrange(RIGHT, buff=0.12)
        c2_calc = MathTex(
            r"\det(B) = (-1)(2) - (1)(0) = -2",
            font_size=28,
            color=COLOR_NEG,
        )
        c2_notes = VGroup(
            Text("• Magnitude |−2| = 2 → Area doubles to 2", font_size=20, color=COLOR_TEXT),
            Text("• Negative sign → Space flips inside-out!", font_size=20, color=COLOR_NEG),
            Text("• Arc î → ĵ reverses from CCW to CW", font_size=20, color=COLOR_MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        c2_card = make_card(
            VGroup(c2_title, c2_mat, c2_calc, c2_notes).arrange(DOWN, aligned_edge=LEFT, buff=0.28),
            border_color=COLOR_NEG,
            pad=0.26,
        ).move_to(LEFT * 3.45 + DOWN * 0.25)

        self.play(FadeIn(c2_card, shift=RIGHT * 0.2), Create(ghost2), Create(active2), run_time=1.2)
        self.play(Create(sq2), Write(area_lbl2), Create(arc2), GrowArrow(i2), GrowArrow(j2), run_time=1.0)
        self.wait(1.8)

        self.play(
            ApplyMatrix(mat_b, active2, about_point=orig2),
            alpha2.animate.set_value(1.0),
            run_time=3.0,
        )
        self.wait(5.8)

        self.play(
            FadeOut(c2_card), FadeOut(ghost2), FadeOut(active2),
            FadeOut(sq2), FadeOut(area_lbl2), FadeOut(arc2), FadeOut(i2), FadeOut(j2),
            run_time=0.7,
        )  # ~29.6s

        # ── CASE 3 : det(C) = 0 (SINGULAR COLLAPSE) ────────────────────────
        ghost3, active3, orig3 = make_plane_pair(
            x_range=(-2, 4, 1),
            y_range=(-1, 5, 1),
            unit_size=0.76,
            center=RIGHT * 3.15 + DOWN * 0.2,
            show_numbers=True,
        )
        mat_c = np.array([[2.0, 1.0], [4.0, 2.0]])
        alpha3 = ValueTracker(0.0)

        def cur3():
            return interp_matrix(np.eye(2), mat_c, alpha3.get_value())

        sq3 = always_redraw(lambda: Polygon(
            *[ghost3.c2p(*(cur3() @ p)) for p in [(0, 0), (1, 0), (1, 1), (0, 1)]],
            stroke_color=COLOR_ZERO,
            stroke_width=2.6,
            fill_color=COLOR_ZERO,
            fill_opacity=0.28,
        ))
        i3 = always_redraw(lambda: vec_arrow(ghost3, cur3() @ np.array([1.0, 0.0]), COLOR_I))
        j3 = always_redraw(lambda: vec_arrow(ghost3, cur3() @ np.array([0.0, 1.0]), COLOR_J))
        i3_lbl = always_redraw(lambda: add_bg_pill(place_tip_label(
            MathTex(r"C\hat{\imath}=(2,4)" if alpha3.get_value() > 0.7 else r"\hat{\imath}", font_size=18, color=COLOR_I),
            ghost3, cur3() @ np.array([1.0, 0.0]), 0.36,
        )))
        j3_lbl = always_redraw(lambda: add_bg_pill(place_tip_label(
            MathTex(r"C\hat{\jmath}=(1,2)" if alpha3.get_value() > 0.7 else r"\hat{\jmath}", font_size=18, color=COLOR_J),
            ghost3, cur3() @ np.array([0.0, 1.0]), 0.36,
        )))

        c3_title = Text("Case 3: Zero Determinant (det = 0)", font_size=23, weight=BOLD, color=COLOR_ZERO)
        c3_mat = VGroup(
            MathTex(r"C = ", font_size=30),
            color_coded_matrix(2, 1, 4, 2, font_size=30),
        ).arrange(RIGHT, buff=0.12)
        c3_calc = MathTex(
            r"\det(C) = (2)(2) - (1)(4) = 0",
            font_size=28,
            color=COLOR_ZERO,
        )
        c3_notes = VGroup(
            Text("• Both columns lie on the same line y = 2x", font_size=20, color=COLOR_TEXT),
            Text("• The entire 2D plane squishes onto 1D!", font_size=20, color=COLOR_ZERO),
            Text("• Area → 0, information lost (singular!)", font_size=20, color=COLOR_MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        c3_card = make_card(
            VGroup(c3_title, c3_mat, c3_calc, c3_notes).arrange(DOWN, aligned_edge=LEFT, buff=0.28),
            border_color=COLOR_ZERO,
            pad=0.26,
        ).move_to(LEFT * 3.45 + DOWN * 0.1)

        self.play(FadeIn(c3_card, shift=RIGHT * 0.2), Create(ghost3), Create(active3), run_time=1.2)
        self.play(Create(sq3), GrowArrow(i3), GrowArrow(j3), FadeIn(i3_lbl), FadeIn(j3_lbl), run_time=1.0)
        self.wait(2.0)

        self.play(
            ApplyMatrix(mat_c, active3, about_point=orig3),
            alpha3.animate.set_value(1.0),
            run_time=3.2,
        )
        line_badge = make_card(
            MathTex(r"\text{Image}(C) : y = 2x \quad (\text{Area} = 0)", font_size=23, color=COLOR_ZERO),
            border_color=COLOR_ZERO,
            pad=0.16,
        ).next_to(c3_card, DOWN, buff=0.28)
        self.play(FadeIn(line_badge, shift=UP * 0.15), run_time=0.9)
        self.wait(6.0)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
