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


def color_coded_matrix(a, b, c, d, font_size=36, fmt="{:g}") -> MathTex:
    """Build a 2x2 MathTex matrix with Column 1 green (î) and Column 2 red (ĵ)."""
    sa, sb, sc, sd = fmt.format(a), fmt.format(b), fmt.format(c), fmt.format(d)
    mat = MathTex(
        r"\begin{bmatrix}",
        sa, "&", sb, r"\\",
        sc, "&", sd,
        r"\end{bmatrix}",
        font_size=font_size,
    )
    # Index parts: 0='\begin{bmatrix}', 1=sa, 2='&', 3=sb, 4='\\', 5=sc, 6='&', 7=sd, 8='\end{bmatrix}'
    mat[1].set_color(COLOR_I)
    mat[5].set_color(COLOR_I)
    mat[3].set_color(COLOR_J)
    mat[7].set_color(COLOR_J)
    return mat


def make_plane_pair(
    x_range=(-4, 4, 1),
    y_range=(-4, 4, 1),
    unit_size=0.68,
    center=ORIGIN,
    show_numbers=True,
):
    """
    Create a (ghost_plane, active_plane, origin_point) tuple.
    Each grid unit equals `unit_size` Manim units so c2p/p2c scale stays exact.
    """
    x_len = (x_range[1] - x_range[0]) * unit_size
    y_len = (y_range[1] - y_range[0]) * unit_size

    ghost = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_len,
        y_length=y_len,
        background_line_style={
            "stroke_color": GHOST_GRID,
            "stroke_width": 1.1,
            "stroke_opacity": 0.45,
        },
        axis_config={
            "stroke_color": GHOST_GRID,
            "stroke_width": 1.5,
            "stroke_opacity": 0.65,
            "include_numbers": show_numbers,
            "font_size": 16,
            "decimal_number_config": {"num_decimal_places": 0, "color": COLOR_MUTED},
        },
    )
    ghost.move_to(center)

    active = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_len,
        y_length=y_len,
        background_line_style={
            "stroke_color": ACTIVE_GRID,
            "stroke_width": 1.6,
            "stroke_opacity": 0.55,
        },
        faded_line_ratio=2,
        faded_line_style={
            "stroke_color": ACTIVE_GRID,
            "stroke_width": 0.7,
            "stroke_opacity": 0.18,
        },
        axis_config={
            "stroke_color": AXIS_COLOR,
            "stroke_width": 2.2,
            "include_numbers": False,
        },
    )
    active.move_to(center)
    origin_pt = ghost.c2p(0, 0)
    return ghost, active, origin_pt


def vec_arrow(ghost_plane: NumberPlane, coords, color, stroke_width=4.5, tip_length=0.2):
    """Create a crisp Arrow from plane origin to math coordinates `coords`."""
    start = ghost_plane.c2p(0, 0)
    end = ghost_plane.c2p(coords[0], coords[1])
    if np.linalg.norm(end - start) < 1e-4:
        return Dot(start, color=color, radius=0.06)
    return Arrow(
        start,
        end,
        buff=0,
        color=color,
        stroke_width=stroke_width,
        max_tip_length_to_length_ratio=0.35,
        tip_length=tip_length,
    )


def place_tip_label(label: Mobject, ghost_plane: NumberPlane, coords, offset_scale=0.32, fallback_dir=UR):
    """Position `label` neatly outside an arrow tip along the outward radial vector."""
    origin = ghost_plane.c2p(0, 0)
    tip = ghost_plane.c2p(coords[0], coords[1])
    direction = tip - origin
    norm = np.linalg.norm(direction)
    if norm < 1e-3:
        direction = np.array(fallback_dir, dtype=float)
        norm = np.linalg.norm(direction)
    unit_dir = direction / norm
    label.move_to(tip + unit_dir * offset_scale)
    return label


def interp_matrix(mat_a: np.ndarray, mat_b: np.ndarray, t: float, rotation_angle: float = None) -> np.ndarray:
    """Interpolate from mat_a to mat_b linearly, or via rotation if rotation_angle is given."""
    if rotation_angle is not None:
        theta = rotation_angle * t
        rot = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)],
        ])
        return rot @ mat_a
    return (1.0 - t) * mat_a + t * mat_b


def build_orientation_arc(ghost_plane: NumberPlane, vec_i, vec_j, radius=0.55, color=COLOR_ACCENT):
    """
    Draw a curved arc from the direction of `vec_i` to `vec_j` (with arrowhead),
    visually indicating whether orientation is counterclockwise (+) or clockwise (-).
    """
    a1 = np.arctan2(vec_i[1], vec_i[0])
    a2 = np.arctan2(vec_j[1], vec_j[0])
    # Shortest signed angular sweep
    diff = (a2 - a1 + np.pi) % (2 * np.pi) - np.pi
    if abs(diff) < 0.08:
        return VGroup()
    origin = ghost_plane.c2p(0, 0)
    arc = Arc(
        radius=radius,
        start_angle=a1,
        angle=diff,
        arc_center=origin,
        color=color,
        stroke_width=3.2,
    )
    # Add small tip at end of arc
    arc.add_tip(tip_length=0.14, tip_width=0.12)
    return arc
