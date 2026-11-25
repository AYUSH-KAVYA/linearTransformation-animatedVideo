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

        # ── 2. CLOSING FRAME: REFERENCES, CREDITS & AI DISCLOSURE (0:18 – 0:32)
        c_header = make_header("Credits, References & Disclosure", "Closing Frame")
        self.play(FadeIn(c_header, shift=DOWN * 0.15), run_time=0.8)

        refs_title = Text("References & Tools", font_size=22, weight=BOLD, color=COLOR_ACCENT)
        refs_body = Text(
            "• 3Blue1Brown (Grant Sanderson) — Essence of Linear Algebra\n"
            "• Gilbert Strang — Introduction to Linear Algebra (MIT / Wellesley-Cambridge)\n"
            "• Animation Engine: Manim Community Edition v0.22 (Python + LaTeX)\n"
            "• Presenter & Voice Narration: " + f"{STUDENT_NAME} ({STUDENT_ID})",
            font_size=19,
            color=COLOR_TEXT,
            line_spacing=1.35,
        )
        refs_card = make_card(
            VGroup(refs_title, refs_body).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            border_color=COLOR_ACCENT,
            pad=0.26,
        )

        ai_title = Text("Audio & AI Tool Disclosure", font_size=22, weight=BOLD, color=COLOR_V)
        ai_body = Text(
            "• Voice-over narration recorded directly by the student; optional background\n"
            "  music (if added) kept low-volume and credited in repository README.\n"
            "• AI Disclosure: Antigravity AI assisted with Manim scene scripting and\n"
            "  storyboard drafting. All mathematical derivations and code were verified.",
            font_size=19,
            color=COLOR_MUTED,
            line_spacing=1.35,
        )
        ai_card = make_card(
            VGroup(ai_title, ai_body).arrange(DOWN, aligned_edge=LEFT, buff=0.18),
            border_color=CARD_BORDER,
            pad=0.26,
        )

        closing_stack = VGroup(refs_card, ai_card).arrange(DOWN, buff=0.35).move_to(UP * 0.1)
        thanks = Text(
            f"Thank You for Watching!   •   {COURSE_TITLE}",
            font_size=24,
            weight=BOLD,
            color=COLOR_ACCENT,
        ).next_to(closing_stack, DOWN, buff=0.45)

        self.play(FadeIn(refs_card, shift=UP * 0.2), run_time=1.2)
        self.wait(2.5)
        self.play(FadeIn(ai_card, shift=UP * 0.2), run_time=1.2)
        self.wait(2.5)
        self.play(Write(thanks), run_time=1.1)
        self.wait(4.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
