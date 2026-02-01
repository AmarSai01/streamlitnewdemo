"""
Streamlit Use Case Demo App
Demonstrates key Streamlit features: widgets, layout, data display, charts, caching, and more.
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# Page config - must be first Streamlit command
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a polished look
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stMetric {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("# 📊 Streamlit Demo")
st.sidebar.markdown("---")

demo_choice = st.sidebar.radio(
    "Choose a use case:",
    [
        "🏠 Overview",
        "📝 Text & Markdown",
        "🎛️ Widgets",
        "📐 Layout (Columns & Expander)",
        "📊 Data & Charts",
        "📁 File Upload",
        "⚡ Caching",
        "🔄 Session State",
        "📋 Forms",
        "⏳ Progress & Status",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit")

# ============== OVERVIEW ==============
if demo_choice == "🏠 Overview":
    st.markdown('<p class="main-header">Streamlit Use Case Demo</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Explore different Streamlit features using the sidebar.</p>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Widgets", "15+", "Interactive")
    with col2:
        st.metric("Layout Options", "Columns, Sidebar", "Flexible")
    with col3:
        st.metric("Data Viz", "Charts & Tables", "Built-in")

    st.info("👈 Select a use case from the **sidebar** to see it in action.")

# ============== TEXT & MARKDOWN ==============
elif demo_choice == "📝 Text & Markdown":
    st.header("📝 Text & Markdown")
    st.write("Streamlit supports rich text and Markdown.")

    st.subheader("Plain text & write()")
    st.write("Hello! This is **bold**, *italic*, and `code` via write().")

    st.subheader("Markdown")
    st.markdown("""
    - Bullet list
    - Another item
    - **Bold** and *italic*

    | Col A | Col B |
    |-------|-------|
    | 1     | 2     |
    """)

    st.subheader("Code block")
    st.code("import streamlit as st\nst.write('Hello, Streamlit!')", language="python")

    st.caption("Caption text for small hints.")

# ============== WIDGETS ==============
elif demo_choice == "🎛️ Widgets":
    st.header("🎛️ Widgets")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Inputs")
        name = st.text_input("Your name", placeholder="Enter name")
        age = st.slider("Age", 0, 100, 25)
        color = st.selectbox("Favorite color", ["Red", "Green", "Blue", "Yellow"])
        options = st.multiselect("Select options", ["A", "B", "C", "D"])
        agree = st.checkbox("I agree")

    with col2:
        st.subheader("Output")
        st.write(f"**Name:** {name or '(not set)'}")
        st.write(f"**Age:** {age}")
        st.write(f"**Color:** {color}")
        st.write(f"**Options:** {options}")
        st.write(f"**Agreed:** {agree}")

    if st.button("Click me"):
        st.balloons()
        st.success("Button clicked! 🎈")

    st.number_input("Number", value=42, key="num")
    st.date_input("Pick a date", value=datetime.now())

# ============== LAYOUT ==============
elif demo_choice == "📐 Layout (Columns & Expander)":
    st.header("📐 Layout: Columns & Expander")

    st.subheader("Columns")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("Column 1")
        st.write("Content in first column.")
    with c2:
        st.warning("Column 2")
        st.write("Content in second column.")
    with c3:
        st.success("Column 3")
        st.write("Content in third column.")

    st.subheader("Expander (collapsible)")
    with st.expander("Click to expand"):
        st.write("Hidden content that appears when expanded.")
        st.code("st.expander('Title')")

# ============== DATA & CHARTS ==============
elif demo_choice == "📊 Data & Charts":
    st.header("📊 Data & Charts")

    # Sample data
    np.random.seed(42)
    n = 50
    df = pd.DataFrame({
        "x": range(n),
        "y": np.cumsum(np.random.randn(n)),
        "category": np.random.choice(["A", "B", "C"], n),
    })

    st.subheader("DataFrame")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Static table")
    st.table(df.head(5))

    st.subheader("Charts")
    chart_type = st.radio("Chart type", ["Line", "Bar", "Area"], horizontal=True)

    if chart_type == "Line":
        st.line_chart(df.set_index("x")["y"])
    elif chart_type == "Bar":
        st.bar_chart(df.groupby("category")["y"].sum())
    else:
        st.area_chart(df.set_index("x")["y"])

# ============== FILE UPLOAD ==============
elif demo_choice == "📁 File Upload":
    st.header("📁 File Upload")

    uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.success(f"Loaded {len(df)} rows × {len(df.columns)} columns")
        st.dataframe(df.head(20), use_container_width=True)
        st.download_button(
            "Download as CSV",
            df.to_csv(index=False).encode("utf-8"),
            file_name="export.csv",
            mime="text/csv",
        )
    else:
        st.info("Upload a CSV to see its preview and download option.")

# ============== CACHING ==============
elif demo_choice == "⚡ Caching":
    st.header("⚡ Caching")

    @st.cache_data
    def expensive_computation(n: int):
        time.sleep(2)  # Simulate slow work
        return sum(i ** 2 for i in range(n))

    n = st.slider("n for sum of squares", 100, 10000, 1000)
    if st.button("Compute (cached)"):
        with st.spinner("Computing..."):
            result = expensive_computation(n)
        st.success(f"Sum of squares 0..{n-1} = {result}")
    st.caption("Run again with same n — result loads instantly from cache.")

# ============== SESSION STATE ==============
elif demo_choice == "🔄 Session State":
    st.header("🔄 Session State")

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Increment"):
            st.session_state.counter += 1
        if st.button("Reset"):
            st.session_state.counter = 0
    with col2:
        st.metric("Counter", st.session_state.counter)

    st.code("""
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1  # persists across reruns
""", language="python")

# ============== FORMS ==============
elif demo_choice == "📋 Forms":
    st.header("📋 Forms")

    with st.form("my_form"):
        st.subheader("Submit multiple inputs at once")
        name = st.text_input("Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Submitted:", name, email)
        st.success("Form submitted!")

# ============== PROGRESS & STATUS ==============
elif demo_choice == "⏳ Progress & Status":
    st.header("⏳ Progress & Status")

    if st.button("Run progress demo"):
        progress = st.progress(0)
        status = st.empty()
        for i in range(101):
            time.sleep(0.02)
            progress.progress(i)
            status.text(f"Step {i}/100")
        status.empty()
        progress.empty()
        st.success("Done!")

    st.spinner("This spinner runs while code executes:")
    with st.spinner("Loading..."):
        time.sleep(1)
    st.success("Spinner finished.")

    st.balloons()
