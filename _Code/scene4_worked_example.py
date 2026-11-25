"""
Scene 4: Worked Example (~60 seconds)
Walks step-by-step through A = [[2, 1], [1, 3]] acting on v = [2, 1]^T -> [5, 5]^T.
Shows both algebraic calculation and live geometric linear combination
2*T(î) + 1*T(ĵ) on a split-screen coordinate grid with zero clipping or overlap.
"""

from manim import *
import numpy as np
from config import (
    BG_COLOR,
    COLOR_ACCENT,
    COLOR_I,
    COLOR_J,
    COLOR_TEXT,
    COLOR_V,
)
from helpers import (
    add_bg_pill,
    color_coded_matrix,
    interp_matrix,
    make_card,
    make_header,
    make_plane_pair,
    place_tip_label,
    vec_arrow,
)


class WorkedExampleScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = make_header("Worked Example: Computing Av Geometrically", "Scene 4 • Step-by-Step")
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.9)

        # Right side coordinate grid covering [-1, 6] x [-1, 6]
        ghost, active, origin_pt = make_plane_pair(
            x_range=(-1, 6, 1),
            y_range=(-1, 6, 1),
            unit_size=0.66,
            center=RIGHT * 3.35 + DOWN * 0.15,
            show_numbers=True,
        )

        mat_i = np.eye(2)
        mat_a = np.array([[2.0, 1.0], [1.0, 3.0]])
        v_in = np.array([2.0, 1.0])

        # Left side: Given matrix & vector at top left
        given_eq = VGroup(
            MathTex(r"A = ", font_size=30),
            color_coded_matrix(2, 1, 1, 3, font_size=30),
            MathTex(r",\;\; \mathbf{v} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", font_size=30, color=COLOR_V),
        ).arrange(RIGHT, buff=0.12)
        given_card = make_card(given_eq, border_color=COLOR_ACCENT, pad=0.18)
        given_card.move_to(LEFT * 3.55 + UP * 2.15)

        # Initial vectors on right grid before matrix deformation
        i_orig = vec_arrow(ghost, [1, 0], COLOR_I)
        j_orig = vec_arrow(ghost, [0, 1], COLOR_J)
        v_orig = vec_arrow(ghost, v_in, COLOR_V, stroke_width=4.6)

        i_orig_lbl = place_tip_label(MathTex(r"\hat{\imath}", font_size=22, color=COLOR_I), ghost, [1, 0], 0.28)
        j_orig_lbl = place_tip_label(MathTex(r"\hat{\jmath}", font_size=22, color=COLOR_J), ghost, [0, 1], 0.28)
        v_orig_lbl = add_bg_pill(
            place_tip_label(MathTex(r"\mathbf{v}=(2,1)", font_size=22, color=COLOR_V), ghost, v_in, 0.44)
        )

        leg_2i = DashedLine(ghost.c2p(0, 0), ghost.c2p(2, 0), color=COLOR_I, stroke_width=2.4)
        leg_1j = DashedLine(ghost.c2p(2, 0), ghost.c2p(2, 1), color=COLOR_J, stroke_width=2.4)

        self.play(Create(ghost), Create(active), FadeIn(given_card), run_time=1.4)
        self.play(
            GrowArrow(i_orig), GrowArrow(j_orig), FadeIn(i_orig_lbl), FadeIn(j_orig_lbl),
            run_time=1.0,
        )
        self.play(
            Create(leg_2i), Create(leg_1j),
            GrowArrow(v_orig), FadeIn(v_orig_lbl),
            run_time=1.4,
        )
        self.wait(3.4)

        # ── STEP 1 & STEP 2 SIDE-BY-SIDE CARDS (compact vertical footprint!) ──
        s1_lbl = Text("Step 1: Col 1 = T(î)", font_size=18, weight=BOLD, color=COLOR_I)
        s1_math = MathTex(
            r"\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix}"
            r"= \begin{bmatrix} 2 \\ 1 \end{bmatrix}",
            font_size=23,
        )
        s1_card = make_card(VGroup(s1_lbl, s1_math).arrange(DOWN, buff=0.12), border_color=COLOR_I, pad=0.16)

        s2_lbl = Text("Step 2: Col 2 = T(ĵ)", font_size=18, weight=BOLD, color=COLOR_J)
        s2_math = MathTex(
            r"\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix}"
            r"= \begin{bmatrix} 1 \\ 3 \end{bmatrix}",
            font_size=23,
        )
        s2_card = make_card(VGroup(s2_lbl, s2_math).arrange(DOWN, buff=0.12), border_color=COLOR_J, pad=0.16)

        steps_12 = VGroup(s1_card, s2_card).arrange(RIGHT, buff=0.2)
        steps_12.next_to(given_card, DOWN, buff=0.22)
        steps_12.set_x(-3.55)

        ti_arrow = vec_arrow(ghost, [2, 1], COLOR_I)
        ti_lbl = add_bg_pill(
            place_tip_label(MathTex(r"T(\hat{\imath})=(2,1)", font_size=20, color=COLOR_I), ghost, [2, 1], 0.44)
        )

        self.play(FadeIn(s1_card, shift=RIGHT * 0.2), run_time=1.0)
        self.play(
            FadeOut(leg_2i), FadeOut(leg_1j),
            TransformFromCopy(i_orig, ti_arrow),
            FadeIn(ti_lbl),
            run_time=1.6,
        )
        self.wait(4.0)

        tj_arrow = vec_arrow(ghost, [1, 3], COLOR_J)
        tj_lbl = add_bg_pill(
            place_tip_label(MathTex(r"T(\hat{\jmath})=(1,3)", font_size=20, color=COLOR_J), ghost, [1, 3], 0.44)
        )

        self.play(FadeIn(s2_card, shift=RIGHT * 0.2), run_time=1.0)
        self.play(
            TransformFromCopy(j_orig, tj_arrow),
            FadeIn(tj_lbl),
            run_time=1.6,
        )
        self.wait(4.0)

        # ── STEP 3: Compute Av step-by-step (plenty of room above bottom edge!) ──
        s3_lbl = Text("Step 3: Weighted Sum  2·T(î) + 1·T(ĵ)", font_size=19, weight=BOLD, color=COLOR_V)
        s3_math1 = MathTex(
            r"A\mathbf{v} = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix}"
            r"= \begin{bmatrix} 2(2)+1(1) \\ 1(2)+3(1) \end{bmatrix}",
            font_size=24,
        )
        s3_math2 = MathTex(
            r"= 2\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 1 \\ 3 \end{bmatrix}"
            r"= \begin{bmatrix} 4 \\ 2 \end{bmatrix} + \begin{bmatrix} 1 \\ 3 \end{bmatrix}"
            r"= \begin{bmatrix} 5 \\ 5 \end{bmatrix}",
            font_size=24,
            color=COLOR_V,
        )
        s3_card = make_card(
            VGroup(s3_lbl, s3_math1, s3_math2).arrange(DOWN, aligned_edge=LEFT, buff=0.14),
            border_color=COLOR_V,
            pad=0.2,
        )
        s3_card.next_to(steps_12, DOWN, buff=0.22)
        s3_card.set_x(-3.55)

        self.play(FadeIn(s3_card, shift=UP * 0.2), run_time=1.3)
        self.wait(6.0)

        # ── STEP 4: Full Grid Deformation & Tip-to-Tail Geometric Verification ──
        self.play(
            FadeOut(ti_arrow), FadeOut(ti_lbl),
            FadeOut(tj_arrow), FadeOut(tj_lbl),
            run_time=0.6,
        )

        alpha = ValueTracker(0.0)
        self.remove(i_orig, j_orig, v_orig, i_orig_lbl, j_orig_lbl, v_orig_lbl)

        i_dyn = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ np.array([1.0, 0.0]), COLOR_I))
        j_dyn = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ np.array([0.0, 1.0]), COLOR_J))
        v_dyn = always_redraw(lambda: vec_arrow(ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ v_in, COLOR_V, stroke_width=4.6))

        i_dyn_lbl = always_redraw(lambda: add_bg_pill(place_tip_label(
            MathTex(r"T(\hat{\imath})=(2,1)" if alpha.get_value() > 0.7 else r"\hat{\imath}", font_size=18, color=COLOR_I),
            ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ np.array([1.0, 0.0]), 0.36,
        )))
        j_dyn_lbl = always_redraw(lambda: add_bg_pill(place_tip_label(
            MathTex(r"T(\hat{\jmath})=(1,3)" if alpha.get_value() > 0.7 else r"\hat{\jmath}", font_size=18, color=COLOR_J),
            ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ np.array([0.0, 1.0]), 0.36,
        )))
        v_dyn_lbl = always_redraw(lambda: add_bg_pill(place_tip_label(
            MathTex(r"A\mathbf{v}=(5,5)" if alpha.get_value() > 0.7 else r"\mathbf{v}=(2,1)", font_size=20, color=COLOR_V),
            ghost, interp_matrix(mat_i, mat_a, alpha.get_value()) @ v_in, 0.42,
        )))

        self.add(i_dyn, j_dyn, v_dyn, i_dyn_lbl, j_dyn_lbl, v_dyn_lbl)

        self.play(
            ApplyMatrix(mat_a, active, about_point=origin_pt),
            alpha.animate.set_value(1.0),
            run_time=3.5,
        )
        self.wait(3.0)

        # Tip-to-tail highlight: 2*T(î) = (4,2) then + 1*T(ĵ) = (5,5)
        two_ti = DashedLine(ghost.c2p(0, 0), ghost.c2p(4, 2), color=COLOR_I, stroke_width=3.2)
        one_tj = DashedLine(ghost.c2p(4, 2), ghost.c2p(5, 5), color=COLOR_J, stroke_width=3.2)
        pt_4_2 = Dot(ghost.c2p(4, 2), color=COLOR_I, radius=0.06)
        lbl_4_2 = add_bg_pill(
            MathTex(r"2T(\hat{\imath})=(4,2)", font_size=18, color=COLOR_I).next_to(pt_4_2, DR, buff=0.1)
        )
        lbl_plus_tj = add_bg_pill(
            MathTex(r"+T(\hat{\jmath})", font_size=18, color=COLOR_J).next_to(one_tj.get_center(), RIGHT, buff=0.14)
        )

        self.play(Create(two_ti), FadeIn(pt_4_2), FadeIn(lbl_4_2), run_time=1.4)
        self.play(Create(one_tj), FadeIn(lbl_plus_tj), run_time=1.4)
        self.wait(4.0)

        # Bottom summary card positioned cleanly below Step 3 on the left side (never overlapping!)
        verify_txt = MathTex(
            r"\|\mathbf{v}\| = \sqrt{5} \approx 2.24 \;\to\; \|A\mathbf{v}\| = 5\sqrt{2} \approx 7.07"
            r"\quad (26.6^\circ \to 45^\circ)",
            font_size=20,
            color=COLOR_TEXT,
        )
        verify_card = make_card(verify_txt, border_color=COLOR_ACCENT, pad=0.15)
        verify_card.next_to(s3_card, DOWN, buff=0.2).set_x(-3.55)

        self.play(FadeIn(verify_card, shift=UP * 0.15), run_time=1.1)
        self.wait(5.5)

        insight_txt = Text(
            "Matrix multiplication = linear combination of columns!",
            font_size=19,
            weight=BOLD,
            color=COLOR_ACCENT,
        )
        insight_card = make_card(insight_txt, border_color=COLOR_ACCENT, pad=0.15)
        insight_card.move_to(verify_card)
        self.play(Transform(verify_card, insight_card), run_time=1.0)
        self.wait(5.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
