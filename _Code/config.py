"""
Shared configuration, theme colors, and metadata for the
Linear Transformations M3 Internal Assessment animation video.
"""

from manim import *

# ─── Student & Course Metadata (Edit before final GitHub upload) ───
COURSE_TITLE = "Linear Algebra and Calculus (M3) • Internal Assessment"
VIDEO_TITLE = "Linear Transformations"
VIDEO_SUBTITLE = "How Matrices Map Vectors, Deform Space & Scale Area"
STUDENT_NAME = "Ayush Sharma"
STUDENT_ID = "E25B070912"

# ─── Consistent Color Palette ───
BG_COLOR = "#0F172A"         # Deep slate-navy background
CARD_BG = "#1E293B"          # Elevated panel fill
CARD_BORDER = "#334155"      # Subtle border
GHOST_GRID = "#334155"       # Original reference grid
ACTIVE_GRID = "#38BDF8"      # Transformed grid (sky blue)
AXIS_COLOR = "#E2E8F0"       # Coordinate axes

COLOR_I = "#4ADE80"          # Basis vector î and Column 1 (emerald green)
COLOR_J = "#FB7185"          # Basis vector ĵ and Column 2 (coral red)
COLOR_V = "#FACC15"          # Test vector v and T(v) (gold)
COLOR_W = "#C084FC"          # Secondary vector / nonlinear accent (violet)
COLOR_ACCENT = "#2DD4BF"     # Headings & highlights (teal)
COLOR_TEXT = "#F8FAFC"       # Primary crisp text
COLOR_MUTED = "#94A3B8"      # Secondary annotations
COLOR_AREA = "#38BDF8"       # Original unit square fill
COLOR_AREA_OUT = "#FACC15"   # Transformed parallelogram fill
COLOR_NEG = "#F43F5E"        # Negative determinant / flip warning
COLOR_ZERO = "#FB923C"       # Singular / zero determinant warning
