"""
Reusable Manim helper utilities for Linear Transformations scenes:
- Safe section headers & badges
- Ghost + active NumberPlane pairs with exact pixel-locked basis/vector tracking
- Color-coded 2x2 matrix displays highlighting basis columns
- Clean card containers for formulas and insights
"""

from manim import *
import numpy as np
from config import (
    ACTIVE_GRID,
    AXIS_COLOR,
    CARD_BG,
    CARD_BORDER,
    COLOR_ACCENT,
    COLOR_AREA,
    COLOR_I,
    COLOR_J,
    COLOR_MUTED,
    COLOR_TEXT,
    COLOR_V,
    GHOST_GRID,
)


def make_header(title_text: str, badge_text: str = "") -> VGroup:
    """Create a clean top-left section header with an opaque top backdrop so grids never cross title text."""
    items = []
    if badge_text:
        pill_label = Text(badge_text.upper(), font_size=16, weight=BOLD, color=COLOR_ACCENT)
        pill_box = RoundedRectangle(
            corner_radius=0.14,
            width=pill_label.width + 0.34,
            height=pill_label.height + 0.18,
            color=COLOR_ACCENT,
            stroke_width=1.5,
            fill_color=CARD_BG,
            fill_opacity=0.95,
        )
        pill = VGroup(pill_box, pill_label)
        pill_label.move_to(pill_box)
        items.append(pill)

    title = Text(title_text, font_size=36, weight=BOLD, color=COLOR_TEXT)
    items.append(title)

    group = VGroup(*items).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
    group.to_corner(UL, buff=0.38)
    underline = Line(
        LEFT * 6.5, RIGHT * 6.5,
        stroke_width=1.2,
        color=CARD_BORDER,
    ).next_to(group, DOWN, buff=0.18).set_x(0)

    top_mask = Rectangle(
        width=15.0,
        height=1.18,
        stroke_width=0,
        fill_color="#0F172A",
        fill_opacity=1.0,
    ).to_edge(UP, buff=0)
    top_mask.set_z_index(11)
    group.set_z_index(12)
    underline.set_z_index(12)

    return VGroup(top_mask, group, underline)


def make_card(content: Mobject, border_color=CARD_BORDER, pad=0.28, fill_opacity=0.95, z_index=10) -> VGroup:
    """Wrap a mobject inside a neat rounded panel."""
    rect = RoundedRectangle(
        corner_radius=0.14,
        width=content.width + pad * 2,
        height=content.height + pad * 2,
        stroke_color=border_color,
        stroke_width=1.8,
        fill_color=CARD_BG,
        fill_opacity=fill_opacity,
    )
    rect.move_to(content.get_center())
    card = VGroup(rect, content)
    card.set_z_index(z_index)
    return card


def add_bg_pill(mob: Mobject, bg_color="#0F172A", opacity=0.82, pad=0.06) -> VGroup:
    """Place a subtle dark pill behind floating graph labels so axes never cut through text."""
    bg = RoundedRectangle(
        corner_radius=0.08,
        width=mob.width + pad * 2,
        height=mob.height + pad * 2,
        stroke_width=0,
        fill_color=bg_color,
        fill_opacity=opacity,
    ).move_to(mob)
    grp = VGroup(bg, mob)
    grp.set_z_index(8)
    return grp
