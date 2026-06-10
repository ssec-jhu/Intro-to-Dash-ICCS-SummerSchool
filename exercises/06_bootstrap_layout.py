"""
Bootstrap Layout — Visual Grid Explorer
=========================================
This exercise lets you explore the Bootstrap 12-column grid system
using dash-bootstrap-components (dbc).

Each ROW has a RED border and each COLUMN has a BLUE border so you can
clearly see how space is divided.

Try changing:
  • The `width` values on columns (integers 1–12, "auto", or True)
  • Adding/removing columns from a row
  • Using `offset` and `order` in width dicts
  • Resizing your browser window to see responsive behaviour

Reference: https://www.dash-bootstrap-components.com/docs/components/layout/

Run:  python exercises/06_bootstrap_layout.py
"""

# --------------------------
# Imports
# --------------------------
from dash import Dash, html
import dash_bootstrap_components as dbc

# --------------------------
# App setup
# --------------------------
app = Dash(external_stylesheets=[dbc.themes.COSMO])

# --------------------------
# Styles
# --------------------------
# Red border for rows so you can see where each row starts/ends
row_style = {
    "border": "2px solid red",
    # "padding": "10px",
}
row_class = "p-2 mb-3"  # this is dbc class for padding (adds padding inside the row)

# Blue border for columns so you can see each column's boundaries
col_style = {
    "border": "2px solid blue",
    "textAlign": "center",
    "backgroundColor": "#f0f8ff",
    # "padding": "10px",
}

# --------------------------
# Row definitions
# --------------------------
# Each row is stored in a variable so you can easily rearrange or comment them out.

first_row = html.Div(
    [
        html.H4("Example 1 — Equal-width columns (default)"),
        html.P("Three columns with no width specified → each gets 1/3 of the row."),
        dbc.Row(
            [
                dbc.Col(html.Div("Col 1 of 3"), style=col_style),
                dbc.Col(html.Div("Col 2 of 3"), style=col_style),
                dbc.Col(html.Div("Col 3 of 3"), style=col_style),
                # Try adding another column here and see what happens!
                # dbc.Col(html.Div("Another Column!"), style=col_style),
            ],
            style=row_style,
            className=row_class,
        ),
    ]
)

second_row = html.Div(
    [
        html.H4("Example 2 — Specified widths"),
        html.P("width=6 (half), width=3 (quarter), width=3 (quarter) → 6+3+3 = 12."),
        dbc.Row(
            [
                dbc.Col(html.Div("Col width=6"), width=6, style=col_style),
                dbc.Col(html.Div("Col width=3"), width=3, style=col_style),
                dbc.Col(html.Div("Col width=3"), width=3, style=col_style),
                # Try changing the widths here and see what happens!
                # Try commenting some columns and see what happens!
            ],
            style=row_style,
            className=row_class,
        ),
    ]
)

third_row = html.Div(
    [
        html.H4("Example 3 — Fixed widths + fill"),
        html.P(
            "First two columns have fixed widths (width=2 and width=3). "
            "The third column has no width set, so it fills the remaining space."
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Col width=2 (fixed)"), width=2, style=col_style),
                dbc.Col(html.Div("Col width=3 (fixed)"), width=3, style=col_style),
                dbc.Col(html.Div("Col (fills remaining 7)"), style=col_style),
            ],
            style=row_style,
            className=row_class,
        ),
    ]
)

fourth_row = html.Div(
    [
        html.H4("Example 4 — Columns pushed to both ends"),
        html.P(
            "Two columns with width=2, justified to opposite ends of the row "
            'using justify="between". The empty space in the middle is unused grid columns.'
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Col width=2 (start)"), width=2, style=col_style),
                dbc.Col(html.Div("Col width=2 (end)"), width=2, style=col_style),
            ],
            # this will push the columns to opposite ends of the row
            # Try changing justify to "center" or "end"
            justify="between",
            style=row_style,
            className=row_class,
        ),
    ]
)

# --------------------------
# Layout
# --------------------------
app.layout = dbc.Container(
    [
        html.H2("Bootstrap Grid — Visual Explorer", className="my-4"),
        html.P(
            "The grid has 12 columns. Rows are outlined in RED, "
            "columns in BLUE. Edit this file and refresh to experiment!"
        ),
        html.A(
            "Dash Bootstrap Layout Docs",
            href="https://www.dash-bootstrap-components.com/docs/components/layout/",
            target="_blank",
        ),
        html.Hr(),
        first_row,
        second_row,
        third_row,
        fourth_row,
    ],
    # fluid=True,
    # style={"padding": "30px"},
)

if __name__ == "__main__":
    app.run(debug=True)
