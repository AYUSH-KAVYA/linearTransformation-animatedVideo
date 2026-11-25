"""
Scene 6: Summary & Credits (~32 seconds)
Recaps 3 core takeaways and presents Closing Frame with References,
Audio/Music Notice, and mandatory AI Disclosure.
"""

from manim import *
from config import (
    BG_COLOR,
    CARD_BORDER,
    COLOR_ACCENT,
    COLOR_I,
    COLOR_J,
    COLOR_MUTED,
    COLOR_TEXT,
    COLOR_V,
    COURSE_TITLE,
    STUDENT_ID,
    STUDENT_NAME,
)
from helpers import make_card, make_header


class SummaryScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. THREE CORE TAKEAWAYS (0:00 – 0:18) ──────────────────────────
        header = make_header("Three Core Takeaways", "Scene 6 • Summary")
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.9)

        takeaways = [
            (
                "1",
                "Basis Vectors Determine Everything",
                "A linear map keeps the origin fixed and grid lines parallel & evenly spaced.\n"
                "Knowing where î and ĵ land determines every vector in ℝ².",
                COLOR_I,
            ),
            (
                "2",
                "Read Columns Directly from the Matrix",
                "Column 1 is T(î) and Column 2 is T(ĵ). Multiplying A·v simply forms\n"
                "the weighted linear combination x·T(î) + y·T(ĵ).",
                COLOR_J,
            ),
            (
                "3",
                "Determinant Encodes Area & Orientation",
                "|det(A)| scales area; det > 0 keeps orientation, det < 0 flips space,\n"
                "and det = 0 collapses 2D space onto a lower dimension (non-invertible).",
                COLOR_V,
            ),
        ]

        cards = VGroup()
        for num, title_str, body_str, col in takeaways:
            badge_txt = Text(num, font_size=26, weight=BOLD, color=BG_COLOR)
            badge = Circle(radius=0.28, color=col, fill_color=col, fill_opacity=1.0)
            badge_txt.move_to(badge)
            badge_grp = VGroup(badge, badge_txt)

            t_head = Text(title_str, font_size=24, weight=BOLD, color=col)
            t_body = Text(body_str, font_size=19, color=COLOR_TEXT, line_spacing=1.28)
            text_col = VGroup(t_head, t_body).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

            row = VGroup(badge_grp, text_col).arrange(RIGHT, buff=0.32, aligned_edge=UP)
            card = make_card(row, border_color=col, pad=0.24)
            cards.add(card)

        cards.arrange(DOWN, buff=0.28).move_to(DOWN * 0.25)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.25), run_time=1.3)
            self.wait(4.2)

        self.wait(2.4)
        self.play(FadeOut(header), FadeOut(cards), run_time=0.8)  # ~21s
