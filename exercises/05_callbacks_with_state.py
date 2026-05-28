"""
Callbacks with State — Teaching Example
========================================
This example demonstrates three key callback concepts:

1. **Input** — triggers the callback when its value changes (the dropdown).
2. **State** — its value is read by the callback but does NOT trigger it
   (the number input). The callback only fires when an Input changes.
3. **Multiple Outputs** — a single callback can update more than one
   component (here: a graph AND a text summary).

Dataset: Plotly Express built-in "tips" dataset (restaurant tipping data).

Run:  python exercises/05_callbacks_with_state.py
"""

# ─── Imports ──────────────────────────────────────────────────────────
from dash import Dash, html, dcc, callback, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc  # https://dash-bootstrap-components.opensource.faculty.ai/
from dash_bootstrap_templates import load_figure_template

# ─── Data ─────────────────────────────────────────────────────────────
df = px.data.tips()  # columns: total_bill, tip, sex, smoker, day, time, size

# ─── App setup ────────────────────────────────────────────────────────
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(external_stylesheets=[dbc.themes.PULSE, dbc_css])
# loads the template and sets it as the default
load_figure_template("PULSE")

# ─── Layout ───────────────────────────────────────────────────────────
app.layout = html.Div(
    [
        html.H2("Tips Dataset — Callbacks with Input and State"),
        html.P(
            "Pick a numeric column from the dropdown to plot a histogram. "
            "Select a day from the second dropdown — this is a State, meaning "
            "it is only read when the first dropdown (an Input) changes. "
            "Try changing the day alone — nothing happens! Only changing the "
            "column dropdown triggers the callback."
        ),
        html.Hr(),
        html.Label("Select column to plot:"),
        dcc.Dropdown(
            id="id-dropdown-column",
            options=[
                {"label": "Total Bill ($)", "value": "total_bill"},
                {"label": "Tip ($)", "value": "tip"},
                {"label": "Party Size", "value": "size"},
            ],
            value="total_bill",  # default selection
            clearable=False,
        ),
        # ── Day dropdown (State — read but does NOT trigger callback) ─
        html.Label(
            "Filter by day (State — only applied when column dropdown changes):"
        ),
        dcc.Dropdown(
            id="id-dropdown-day",
            options=[{"label": day, "value": day} for day in df["day"].unique()],
            value="Sun",  # default selection
            clearable=False,
            style={"marginTop": "5px"},
        ),
        dcc.Graph(id="id-graph-histogram"),
        html.Div(
            id="id-text-summary",
            style={
                "padding": "12px",
                "backgroundColor": "#f0f0f0",
                "borderRadius": "6px",
                "marginTop": "10px",
                "fontSize": "16px",
            },
        ),
    ],
    style={"maxWidth": "800px", "margin": "auto", "padding": "30px"},
)


@callback(
    # Multiple Outputs: the callback returns TWO values
    Output("id-graph-histogram", "figure"),  # 1st return value → graph
    Output("id-text-summary", "children"),  # 2nd return value → text
    # Input: changing the column dropdown TRIGGERS the callback
    Input("id-dropdown-column", "value"),
    # State: the day dropdown value is READ but does NOT trigger the callback.
    # Try changing the day — nothing happens until you change the column dropdown!
    State("id-dropdown-day", "value"),
)
def update_histogram(selected_column, selected_day):
    """
    This function runs every time the column dropdown value changes.
    It reads the current-day dropdown value (State), but changing that
    dropdown alone will NOT cause this function to re-run.
    """
    # Filter the dataframe by the selected day (State value)
    filtered = df[df["day"] == selected_day]

    # Build the histogram
    fig = px.histogram(
        filtered,
        x=selected_column,
        color="smoker",
        title=f"Distribution of {selected_column} on {selected_day}",
        labels={selected_column: selected_column.replace("_", " ").title()},
        nbins=20,
    )

    # Build a text summary (second Output)
    total_rows = len(df)
    shown_rows = len(filtered)
    mean_val = filtered[selected_column].mean()
    summary = (
        f"Showing {shown_rows} of {total_rows} rows "
        f"(day = {selected_day})  |  "
        f"Mean {selected_column}: {mean_val:.2f}"
    )

    # Return TWO values — one for each Output (in order)
    return fig, summary


if __name__ == "__main__":
    app.run(debug=True)
