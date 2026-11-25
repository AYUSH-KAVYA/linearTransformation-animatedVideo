"""
Scene 1: Hook / Context (~44 seconds)
Includes mandatory Opening Frame (Title, Concept, Student Name & ID),
real-world motivation, and a visual geometric teaser.
"""

from manim import *
import numpy as np
from config import (
    BG_COLOR,
    CARD_BG,
    CARD_BORDER,
    COLOR_ACCENT,
    COLOR_AREA,
    COLOR_AREA_OUT,
    COLOR_I,
    COLOR_J,
    COLOR_MUTED,
    COLOR_TEXT,
    COLOR_V,
    COURSE_TITLE,
    STUDENT_ID,
    STUDENT_NAME,
    VIDEO_SUBTITLE,
    VIDEO_TITLE,
)
from helpers import (
    color_coded_matrix,
    interp_matrix,
    make_card,
    make_plane_pair,
    place_tip_label,
    vec_arrow,
)


class HookScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. OPENING FRAME (0:00 – 0:08) ─────────────────────────────────
        course_pill_txt = Text(COURSE_TITLE, font_size=18, weight=BOLD, color=COLOR_ACCENT)
        course_pill_box = RoundedRectangle(
            corner_radius=0.18,
            width=course_pill_txt.width + 0.6,
            height=course_pill_txt.height + 0.26,
            stroke_color=COLOR_ACCENT,
            stroke_width=1.5,
            fill_color=CARD_BG,
            fill_opacity=0.95,
        )
        course_pill = VGroup(course_pill_box, course_pill_txt)
        course_pill_txt.move_to(course_pill_box)

        title = Text(VIDEO_TITLE, font_size=60, weight=BOLD, color=COLOR_TEXT)
        subtitle = Text(VIDEO_SUBTITLE, font_size=26, color=COLOR_ACCENT)

        presenter_txt = Text(
            f"Concept: Linear Transformations in ℝ²    •    Student: {STUDENT_NAME}    •    ID: {STUDENT_ID}",
            font_size=19,
            color=COLOR_MUTED,
        )
        presenter_card = make_card(presenter_txt, border_color=CARD_BORDER, pad=0.22)

        opening = VGroup(course_pill, title, subtitle, presenter_card).arrange(DOWN, buff=0.45)
        opening.move_to(ORIGIN)

        self.play(FadeIn(course_pill, shift=DOWN * 0.2), run_time=0.8)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.0)
        self.play(FadeIn(presenter_card, shift=UP * 0.2), run_time=0.8)
        self.wait(3.8)

        self.play(FadeOut(opening), run_time=0.8)  # Total so far: 8.6s

        # ── 2. REAL-WORLD MOTIVATION + MINI MORPHING GRID (0:08 – 0:24) ───
        mot_header = Text(
            "Where Do Matrices Move the World?",
            font_size=34,
            weight=BOLD,
            color=COLOR_TEXT,
        ).to_corner(UL, buff=0.45)

        bullets = VGroup(
            Text("• Computer Graphics: rotating & scaling 2D/3D scenes", font_size=22, color=COLOR_TEXT),
            Text("• Robotics & Physics: switching coordinate frames", font_size=22, color=COLOR_TEXT),
            Text("• Data Science: projecting & compressing high-dim data", font_size=22, color=COLOR_TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        bullets.next_to(mot_header, DOWN, buff=0.45).align_to(mot_header, LEFT)
        mot_card = make_card(bullets, border_color=COLOR_ACCENT, pad=0.3)

        # Right side mini-plane with a simple house shape so deformation feels tangible
        ghost, active, origin_pt = make_plane_pair(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            unit_size=0.62,
            center=RIGHT * 3.1 + DOWN * 0.15,
            show_numbers=False,
        )
        house_pts = [(0, 0), (1.5, 0), (1.5, 1.1), (0.75, 1.8), (0, 1.1)]
        house = Polygon(
            *[ghost.c2p(x, y) for x, y in house_pts],
            stroke_color=COLOR_V,
            stroke_width=3.2,
            fill_color=COLOR_V,
            fill_opacity=0.22,
        )
        mat_badge = MathTex(r"A = \begin{bmatrix} 1 & 0.6 \\ 0 & 1 \end{bmatrix}", font_size=28, color=COLOR_ACCENT)
        mat_badge.next_to(ghost, UP, buff=0.22)

        self.play(Write(mot_header), FadeIn(mot_card), run_time=1.4)
        self.play(Create(ghost), Create(active), Create(house), FadeIn(mat_badge), run_time=1.5)
        self.wait(1.8)

        # Shear then rotate the house smoothly
        shear = np.array([[1.0, 0.6], [0.0, 1.0]])
        self.play(
            ApplyMatrix(shear, active, about_point=origin_pt),
            ApplyMatrix(shear, house, about_point=origin_pt),
            run_time=2.2,
        )
        self.wait(1.5)

        rot_mat = MathTex(r"R = \begin{bmatrix} \cos 30^\circ & -\sin 30^\circ \\ \sin 30^\circ & \cos 30^\circ \end{bmatrix}", font_size=24, color=COLOR_ACCENT)
        rot_mat.move_to(mat_badge)
        self.play(
            Transform(mat_badge, rot_mat),
            Rotate(active, angle=PI / 6, about_point=origin_pt),
            Rotate(house, angle=PI / 6, about_point=origin_pt),
            run_time=2.2,
        )
        self.wait(2.5)

        self.play(
            FadeOut(mot_header),
            FadeOut(mot_card),
            FadeOut(ghost),
            FadeOut(active),
            FadeOut(house),
            FadeOut(mat_badge),
            run_time=0.8,
        )  # Total so far: ~22.5s

        # ── 3. GUIDING QUESTION & TEASER (0:24 – 0:44) ─────────────────────
        q_title = Text("The Central Question", font_size=26, weight=BOLD, color=COLOR_ACCENT)
        q_body = Text(
            "What happens to all of 2D space when we\nmultiply every vector by a 2 × 2 matrix?",
            font_size=34,
            weight=BOLD,
            color=COLOR_TEXT,
            line_spacing=1.35,
        )
        q_group = VGroup(q_title, q_body).arrange(DOWN, buff=0.35).move_to(UP * 0.3)

        self.play(FadeIn(q_title), Write(q_body), run_time=2.2)
        self.wait(2.5)
        self.play(FadeOut(q_group), run_time=0.7)

        # Full-plane teaser with matrix A = [[1.5, 0.8], [-0.3, 1.2]]
        ghost2, active2, origin2 = make_plane_pair(
            x_range=(-5, 5, 1),
            y_range=(-3, 3, 1),
            unit_size=0.82,
            center=DOWN * 0.15,
            show_numbers=True,
        )

        alpha = ValueTracker(0.0)
        mat_start = np.eye(2)
        mat_end = np.array([[1.5, 0.8], [-0.3, 1.2]])

        unit_sq = always_redraw(lambda: Polygon(
            *[
                ghost2.c2p(*interp_matrix(mat_start, mat_end, alpha.get_value()) @ p)
                for p in [(0, 0), (1, 0), (1, 1), (0, 1)]
            ],
            stroke_color=COLOR_AREA_OUT,
            stroke_width=2.5,
            fill_color=COLOR_AREA if alpha.get_value() < 0.5 else COLOR_AREA_OUT,
            fill_opacity=0.28,
        ))
        i_vec = always_redraw(lambda: vec_arrow(
            ghost2,
            interp_matrix(mat_start, mat_end, alpha.get_value()) @ np.array([1.0, 0.0]),
            COLOR_I,
        ))
        j_vec = always_redraw(lambda: vec_arrow(
            ghost2,
            interp_matrix(mat_start, mat_end, alpha.get_value()) @ np.array([0.0, 1.0]),
            COLOR_J,
        ))
        i_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\hat{\imath}", font_size=30, color=COLOR_I),
            ghost2,
            interp_matrix(mat_start, mat_end, alpha.get_value()) @ np.array([1.0, 0.0]),
            offset_scale=0.35,
        ))
        j_lbl = always_redraw(lambda: place_tip_label(
            MathTex(r"\hat{\jmath}", font_size=30, color=COLOR_J),
            ghost2,
            interp_matrix(mat_start, mat_end, alpha.get_value()) @ np.array([0.0, 1.0]),
            offset_scale=0.35,
        ))

        teaser_mat = VGroup(
            MathTex(r"A = ", font_size=34, color=COLOR_TEXT),
            color_coded_matrix(1.5, 0.8, -0.3, 1.2, font_size=34),
        ).arrange(RIGHT, buff=0.15)
        teaser_card = make_card(teaser_mat, border_color=COLOR_ACCENT, pad=0.2).to_corner(UL, buff=0.4)

        self.play(Create(ghost2), Create(active2), FadeIn(teaser_card), run_time=1.4)
        self.play(Create(unit_sq), GrowArrow(i_vec), GrowArrow(j_vec), FadeIn(i_lbl), FadeIn(j_lbl), run_time=1.0)
        self.wait(1.2)

        self.play(
            ApplyMatrix(mat_end, active2, about_point=origin2),
            alpha.animate.set_value(1.0),
            run_time=3.2,
        )
        self.wait(2.2)

        bridge = Text(
            "Let's uncover how four numbers encode this entire motion.",
            font_size=26,
            weight=BOLD,
            color=COLOR_ACCENT,
        )
        bridge_card = make_card(bridge, border_color=COLOR_ACCENT, pad=0.22).to_edge(DOWN, buff=0.32)
        self.play(FadeIn(bridge_card, shift=UP * 0.2), run_time=1.0)
        self.wait(3.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
