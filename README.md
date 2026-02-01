# Streamlit Use Case Demo App

A demo app that showcases **Streamlit** features and common use cases: widgets, layout, data display, charts, file upload, caching, session state, forms, and progress/status.

## Quick Start

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser (usually at `http://localhost:8501`).

## Use Cases Demonstrated

| Section | What it shows |
|--------|----------------|
| **Overview** | Page config, metrics, info messages |
| **Text & Markdown** | `st.write`, `st.markdown`, `st.code`, `st.caption` |
| **Widgets** | Slider, selectbox, multiselect, checkbox, button, text/date/number input |
| **Layout** | Columns, expander |
| **Data & Charts** | DataFrames, tables, line/bar/area charts |
| **File Upload** | Upload CSV, preview, download button |
| **Caching** | `@st.cache_data` for expensive computation |
| **Session State** | Persisting counter across reruns |
| **Forms** | `st.form` for batch submit |
| **Progress & Status** | Progress bar, spinner, balloons |

## Requirements

- Python 3.8+
- See `requirements.txt` for packages

## Project Structure

```
.
├── app.py           # Main Streamlit app
├── requirements.txt
└── README.md
```
