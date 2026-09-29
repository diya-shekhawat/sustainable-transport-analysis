import streamlit as st
import matplotlib.pyplot as plt

# ============================================================
# GUI DESIGN - WHITE + PINK THEME
# Sustainable Transport Choices Streamlit App
# ============================================================

# -----------------------------
# Theme Colors
# -----------------------------
PINK = "#EC4899"
DARK_PINK = "#BE185D"
MEDIUM_PINK = "#DB2777"
LIGHT_PINK = "#FCE7F3"
PALE_PINK = "#FFF7FB"
BORDER_PINK = "#F9C2DC"
TEXT = "#3F2732"
MUTED_TEXT = "#7A5A68"
WHITE = "#FFFFFF"


def apply_theme():
    """
    Apply the complete White + Pink Streamlit theme.
    Call this once near the top of app.py after st.set_page_config().
    """

    st.markdown(
        f"""
        <style>

        /* ==========================================
           MAIN APP
           ========================================== */

        .stApp {{
            background: linear-gradient(
                180deg,
                {WHITE} 0%,
                {PALE_PINK} 100%
            );
            color: {TEXT};
        }}

        .main .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1450px;
        }}

        /* Hide Streamlit default decoration */
        #MainMenu {{
            visibility: hidden;
        }}

        footer {{
            visibility: hidden;
        }}

        header {{
            background: transparent !important;
        }}

        /* ==========================================
           SIDEBAR
           ========================================== */

        section[data-testid="stSidebar"] {{
            background: linear-gradient(
                180deg,
                #FFF0F6 0%,
                #FFF8FB 100%
            );
            border-right: 1px solid {BORDER_PINK};
        }}

        section[data-testid="stSidebar"] > div {{
            padding-top: 1.5rem;
        }}

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {{
            color: {DARK_PINK};
        }}

        section[data-testid="stSidebar"] label {{
            color: {TEXT} !important;
            font-weight: 600 !important;
        }}

        /* Multiselect */
        div[data-baseweb="select"] > div {{
            background-color: {WHITE} !important;
            border: 1px solid {BORDER_PINK} !important;
            border-radius: 10px !important;
        }}

        div[data-baseweb="select"] > div:focus-within {{
            border-color: {PINK} !important;
            box-shadow: 0 0 0 2px rgba(236, 72, 153, 0.12) !important;
        }}

        /* ==========================================
           HEADINGS
           ========================================== */

        h1, h2, h3 {{
            color: {DARK_PINK} !important;
        }}

        h1 {{
            font-weight: 800 !important;
            letter-spacing: -0.5px;
        }}

        h2 {{
            font-weight: 750 !important;
        }}

        h3 {{
            font-weight: 700 !important;
        }}

        p, span, label, div {{
            font-family: Arial, Helvetica, sans-serif;
        }}

        /* ==========================================
           HERO HEADER
           ========================================== */

        .pink-hero {{
            background:
                radial-gradient(
                    circle at top right,
                    rgba(236,72,153,0.20),
                    transparent 35%
                ),
                linear-gradient(
                    135deg,
                    #FFFFFF 0%,
                    #FFF0F6 52%,
                    #FCE7F3 100%
                );

            border: 1px solid {BORDER_PINK};
            border-radius: 22px;
            padding: 28px 34px;
            margin: 0 0 26px 0;
            box-shadow: 0 8px 25px rgba(190, 24, 93, 0.08);
        }}

        .pink-hero-title {{
            color: {DARK_PINK};
            font-size: 36px;
            font-weight: 800;
            margin-bottom: 5px;
        }}

        .pink-hero-subtitle {{
            color: {MEDIUM_PINK};
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .pink-hero-description {{
            color: {MUTED_TEXT};
            font-size: 15px;
            line-height: 1.6;
            margin: 0;
        }}

        /* ==========================================
           SECTION HEADER
           ========================================== */

        .section-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            color: {DARK_PINK};
            font-size: 25px;
            font-weight: 800;
            margin: 28px 0 15px 0;
        }}

        .section-line {{
            height: 3px;
            width: 58px;
            background: linear-gradient(
                90deg,
                {PINK},
                #F9A8D4
            );
            border-radius: 10px;
            margin-bottom: 20px;
        }}

        /* ==========================================
           KPI CARDS
           ========================================== */

        .kpi-card {{
            background: {WHITE};
            border: 1px solid {BORDER_PINK};
            border-radius: 18px;
            padding: 20px 18px;
            min-height: 125px;
            box-shadow: 0 7px 20px rgba(190, 24, 93, 0.07);
            transition: all 0.2s ease;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(190, 24, 93, 0.12);
            border-color: #F9A8D4;
        }}

        .kpi-icon {{
            font-size: 24px;
            margin-bottom: 7px;
        }}

        .kpi-label {{
            color: {MUTED_TEXT};
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .kpi-value {{
            color: {DARK_PINK};
            font-size: 25px;
            font-weight: 800;
            margin-top: 5px;
            word-break: break-word;
        }}

        /* ==========================================
           TABS
           ========================================== */

        button[data-baseweb="tab"] {{
            color: {MUTED_TEXT} !important;
            font-weight: 700 !important;
            border-radius: 10px 10px 0 0 !important;
            padding: 10px 15px !important;
        }}

        button[data-baseweb="tab"]:hover {{
            color: {PINK} !important;
            background: {LIGHT_PINK} !important;
        }}

        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {DARK_PINK} !important;
            border-bottom: 3px solid {PINK} !important;
            background: {LIGHT_PINK} !important;
        }}

        div[data-baseweb="tab-highlight"] {{
            background-color: {PINK} !important;
        }}

        /* ==========================================
           BUTTONS
           ========================================== */

        .stButton > button {{
            background: linear-gradient(
                135deg,
                {PINK},
                {MEDIUM_PINK}
            ) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            padding: 0.55rem 1rem !important;
            box-shadow: 0 5px 12px rgba(236,72,153,0.18);
        }}

        .stButton > button:hover {{
            background: linear-gradient(
                135deg,
                {MEDIUM_PINK},
                {DARK_PINK}
            ) !important;
            border: none !important;
            transform: translateY(-1px);
        }}

        /* ==========================================
           DATAFRAMES / TABLES
           ========================================== */

        div[data-testid="stDataFrame"] {{
            border: 1px solid {BORDER_PINK};
            border-radius: 13px;
            overflow: hidden;
            box-shadow: 0 5px 16px rgba(190, 24, 93, 0.05);
            background: white;
        }}

        /* ==========================================
           METRIC DEFAULT STREAMLIT
           ========================================== */

        div[data-testid="stMetric"] {{
            background: {WHITE};
            border: 1px solid {BORDER_PINK};
            border-radius: 16px;
            padding: 16px;
            box-shadow: 0 6px 18px rgba(190, 24, 93, 0.06);
        }}

        div[data-testid="stMetricLabel"] {{
            color: {MUTED_TEXT} !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: {DARK_PINK} !important;
            font-weight: 800 !important;
        }}

        /* ==========================================
           ALERTS
           ========================================== */

        div[data-testid="stAlert"] {{
            border-radius: 12px;
            border: 1px solid {BORDER_PINK};
        }}

        /* ==========================================
           EXPANDER
           ========================================== */

        details {{
            background: {WHITE};
            border: 1px solid {BORDER_PINK} !important;
            border-radius: 12px !important;
        }}

        /* ==========================================
           DIVIDER
           ========================================== */

        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(
                90deg,
                transparent,
                {BORDER_PINK},
                transparent
            );
            margin: 25px 0;
        }}

        /* ==========================================
           CAPTION
           ========================================== */

        .stCaption {{
            color: {MUTED_TEXT} !important;
        }}

        /* ==========================================
           SCROLLBAR
           ========================================== */

        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: #FFF5F9;
        }}

        ::-webkit-scrollbar-thumb {{
            background: #F9A8D4;
            border-radius: 10px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: {PINK};
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


def page_header(
    title="🚆 Sustainable Transport Choices",
    subtitle="Field Project Data Analysis Dashboard",
    description=(
        "Analysis of survey responses on transportation habits, "
        "public transport, sustainability awareness, barriers and suggestions."
    )
):
    """Display the main white + pink hero header."""

    st.markdown(
        f"""
        <div class="pink-hero">
            <div class="pink-hero-title">{title}</div>
            <div class="pink-hero-subtitle">{subtitle}</div>
            <p class="pink-hero-description">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_header(title, icon=""):
    """Display a styled section heading."""

    st.markdown(
        f"""
        <div class="section-title">
            <span>{icon}</span>
            <span>{title}</span>
        </div>
        <div class="section-line"></div>
        """,
        unsafe_allow_html=True
    )


def metric_card(label, value, icon="📊"):
    """Display a custom pink KPI card."""

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, text, icon="💡"):
    """Display a small information card."""

    st.markdown(
        f"""
        <div class="kpi-card" style="min-height: auto;">
            <div class="kpi-icon">{icon}</div>
            <div style="
                color:{DARK_PINK};
                font-size:16px;
                font-weight:800;
                margin-bottom:6px;
            ">{title}</div>
            <div style="
                color:{MUTED_TEXT};
                font-size:14px;
                line-height:1.55;
            ">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def style_matplotlib():
    """
    Return a white + pink Matplotlib configuration.
    Use this before creating charts in the main app.
    """

    plt.rcParams.update({
        "figure.facecolor": WHITE,
        "axes.facecolor": WHITE,
        "axes.edgecolor": "#E8B7CC",
        "axes.labelcolor": TEXT,
        "xtick.color": MUTED_TEXT,
        "ytick.color": MUTED_TEXT,
        "text.color": TEXT,
        "axes.titlecolor": DARK_PINK,
        "axes.titleweight": "bold",
        "font.size": 10,
    })


def chart_colors():
    """Pink shades for charts."""

    return [
        "#EC4899",
        "#F472B6",
        "#F9A8D4",
        "#FBCFE8",
        "#BE185D",
        "#DB2777",
        "#FDA4AF",
        "#E879A9",
    ]


def footer():
    """Display the dashboard footer."""

    st.markdown(
        f"""
        <div style="
            margin-top:35px;
            padding:18px;
            text-align:center;
            border-top:1px solid {BORDER_PINK};
            color:{MUTED_TEXT};
            font-size:13px;
        ">
            <b style="color:{DARK_PINK};">
                Sustainable Transport Choices
            </b>
            &nbsp;|&nbsp;
            Python • Pandas • Matplotlib • Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )
