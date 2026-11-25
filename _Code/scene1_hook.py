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
