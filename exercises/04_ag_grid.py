# Displaying Data with Dash AG Grid
# ===================================
# In this exercise we display an interactive table using dag.AgGrid
# — still no callbacks!
#
# The data is loaded from a shared CSV file (same one used by 03_dcc_graph.py).
#
# Run the app and explore sorting, filtering, and pagination.
# Then tweak column definitions and grid options.

from pathlib import Path

from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# ── Load Data ────────────────────────────────────────────────────
data_path = Path(__file__).parent.parent / "data" / "rse_data.csv"
df = pd.read_csv(data_path)

# ── Column Definitions ────────────────────────────────────────────
column_defs = [
    {"field": "research_software_engineer", "headerName": "RSE"},
    {"field": "country", "headerName": "Country"},
    {"field": "coffees_per_day", "headerName": "Coffees/Day"},
    {"field": "lines_of_code", "headerName": "Lines of Code"},
    {"field": "bugs_introduced", "headerName": "Bugs Introduced"},
    {"field": "workshop_rating", "headerName": "Workshop Rating"},
    {"field": "university", "headerName": "University"},
]
# TODO: Try setting sortable=False on a column, e.g. {"field": "Country", "sortable": False}


# ── Layout ───────────────────────────────────────────────────────
app = Dash(
    # need this for the rowClassRules styling in the second grid below
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
    ]
)

app.layout = html.Div(
    style={"maxWidth": "1000px", "margin": "auto", "padding": "20px"},
    children=[
        html.H2("AG Grid Table"),
        html.P(
            "AG Grid displays tabular data with built-in sorting, filtering, "
            "and pagination. The data comes from the same CSV used in the "
            "previous graph exercise."
        ),
        html.A(
            "AG Grid docs",
            href="https://dash.plotly.com/dash-ag-grid",
            target="_blank",
        ),
        dag.AgGrid(
            # row data is the data to display, in the form of a list of dicts (one dict per row)
            rowData=df.to_dict("records"),
            # column definitions specify how to display each column (field) in the data
            columnDefs=column_defs,
            # defaultColDef applies to all columns, here we add filtering, sorting, and resizing
            defaultColDef={"filter": True, "sortable": True, "resizable": True},
            # additional grid options are passed via dashGridOptions, here we enable pagination
            dashGridOptions={"pagination": True},
        ),
        html.H2("AG Grid with Row Class Rules"),
        # to add styles you need to add the style sheet in the app and then specify class names
        # in rowClassRules
        dag.AgGrid(
            # same as above
            rowData=df.to_dict("records"),
            columnDefs=column_defs,
            defaultColDef={"filter": True, "sortable": True, "resizable": True},
            # same as above but with rowClassRules to add a CSS
            # class to rows where bugs_introduced > 50
            dashGridOptions={
                "pagination": True,
                "rowClassRules": {
                    "text-danger fw-bold fs-4": "params.data.bugs_introduced > 50",
                },
            },
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
