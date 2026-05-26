"""
Interactive Gapminder Dashboard — EXERCISE
===========================================
Build an interactive dashboard step by step!
Fill in the TODOs below to connect Dash components to a scatter chart.

If you get stuck, check the solution: 04_interactive_exercise_solution.py
"""

# ------------
# Imports
# -------------
from dash import Dash, html  # https://dash.plotly.com/
import plotly.express as px  # https://plotly.com/python/plotly-express/
import dash_bootstrap_components as dbc  # https://dash-bootstrap-components.opensource.faculty.ai/
from dash_bootstrap_templates import load_figure_template

# ------------
# Data
# -------------
df = px.data.gapminder()

# ------------
# App setup
# -------------
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc_css])
# loads the template and sets it as the default
load_figure_template("FLATLY")

# ╔══════════════════════════════════════════════════════════════════════╗
# ║ TODO 1: Add a dcc.Dropdown to filter by continent                  ║
# ║                                                                    ║
# ║  - id: "id-dropdown-continent"                                     ║
# ║  - multi=True (allow selecting multiple continents)                ║
# ║  - options: one option per unique value in df["continent"]         ║
# ║  - value: default to ALL continents selected                       ║
# ║                                                                    ║
# ║  Docs: https://dash.plotly.com/dash-core-components/dropdown       ║
# ╚══════════════════════════════════════════════════════════════════════╝
dropdown = html.Div(
    children=["add your dcc.Dropdown here!"],
)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║ TODO 2: Add a dcc.Slider to select the year                        ║
# ║                                                                    ║
# ║  - id: "id-slider-year"                                            ║
# ║  - min: df["year"].min()                                           ║
# ║  - max: df["year"].max()                                           ║
# ║  - step: 5                                                         ║
# ║  - value: 2007 (default year)                                      ║
# ║  - marks: one mark per unique year in the data                     ║
# ║                                                                    ║
# ║  Docs: https://dash.plotly.com/dash-core-components/slider         ║
# ╚══════════════════════════════════════════════════════════════════════╝
slider = html.Div(
    children=["add your dcc.Slider here!"],
)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║ TODO 3: Add a dag.AgGrid to show the data                          ║
# ║                                                                    ║
# ║  - id: "id-grid-data"                                              ║
# ║  - columnDefs: [{"field": col} for col in df.columns]              ║
# ║  - rowData: df.to_dict("records")                                  ║
# ║  - dashGridOptions: {"pagination": True, "paginationPageSize": 10} ║
# ║  - The rowData will be updated by the callback (TODO 5)            ║
# ║                                                                    ║
# ║  Docs: https://dash.plotly.com/dash-ag-grid/getting-started        ║
# ╚══════════════════════════════════════════════════════════════════════╝
grid = html.Div(
    children=["add your dag.AgGrid here!"],
)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║ TODO 4: Add a dcc.Graph to display a scatter chart                 ║
# ║                                                                    ║
# ║  - id: "id-graph-scatter"                                          ║
# ║  - The chart should be a px.scatter with:                          ║
# ║      x = "gdpPercap"   (GDP per capita)                            ║
# ║      y = "lifeExp"     (life expectancy)                           ║
# ║      size = "pop"      (population → bubble size)                  ║
# ║      color = "continent"                                           ║
# ║      hover_name = "country"                                        ║
# ║  - The figure will be created in the callback (TODO 6),            ║
# ║    so here you just need the dcc.Graph component with the id.      ║
# ║                                                                    ║
# ║  Docs: https://dash.plotly.com/dash-core-components/graph          ║
# ╚══════════════════════════════════════════════════════════════════════╝
graph = html.Div(
    children=["add your dcc.Graph here!"],
)

# ------------
# Layout
# -------------
app.layout = dbc.Container(
    [
        html.H1("Intro to Dash Interactive Exercise"),
        # Dropdown: filter by continent
        html.Label("Select Continent(s):"),
        # TODO 1: go to dropdown above
        dropdown,
        html.Br(),
        # Slider: select year
        html.Label("Select Year:"),
        # TODO 2: go to slider above
        slider,
        html.Br(),
        # AG Grid: show filtered data
        # TODO 3: go to grid above
        grid,
        html.Br(),
        # Graph: scatter plot
        # TODO 4: go to graph above
        graph,
        html.Br(),
        # Country detail in a dbc.Card (populated by clicking a point on the graph)
        dbc.Card(
            [
                dbc.CardHeader("Country Details", id="id-card-header"),
                dbc.CardBody(id="id-card-country"),
            ]
        ),
    ],
    # this sets the overall theme and styling for the app using Bootstrap
    className="dbc dbc-ag-grid",
    style={"maxWidth": "900px", "padding": "20px"},
)


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 5: Write a @callback that updates the AG Grid                         ║
# ║                                                                            ║
# ║  - Output: the "rowData" property of "id-grid-data"                       ║
# ║  - Inputs:                                                                 ║
# ║      1. "value" property of "id-dropdown-continent" (list of continents)   ║
# ║      2. "value" property of "id-slider-year" (selected year)               ║
# ║  - Inside the function:                                                    ║
# ║      1. Filter df where continent is in selected_continents                ║
# ║         AND year == selected_year                                          ║
# ║      2. Return filtered.to_dict("records")                                ║
# ║                                                                            ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 6: Write a @callback that updates the scatter chart                   ║
# ║                                                                            ║
# ║  - Output: the "figure" property of "id-graph-scatter"                     ║
# ║  - Inputs:                                                                 ║
# ║      1. "value" property of "id-dropdown-continent" (list of continents)   ║
# ║      2. "value" property of "id-slider-year" (selected year)               ║
# ║  - Inside the function:                                                    ║
# ║      1. Filter df where continent is in selected_continents                ║
# ║         AND year == selected_year                                          ║
# ║      2. Create a px.scatter with x="gdpPercap", y="lifeExp",              ║
# ║         size="pop", color="continent", hover_name="country"               ║
# ║      3. Return the figure                                                 ║
# ║                                                                            ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 7: Write a @callback that shows country details in the dbc.Card       ║
# ║         when you click a point on the scatter chart                        ║
# ║                                                                            ║
# ║  - Output: the "children" property of "id-card-country"                   ║
# ║  - Input: the "clickData" property of "id-graph-scatter"                  ║
# ║  - Inside the function:                                                    ║
# ║      1. If clickData is None, return a placeholder message                 ║
# ║      2. Extract the country name from clickData["points"][0]["hovertext"]  ║
# ║      3. Look up that country in df and display its stats                   ║
# ║      4. Return the content as a list of html components                    ║
# ║         (e.g. [html.H4("Country"), html.P("Stat: value"), ...])           ║
# ║                                                                            ║
# ║  Docs (clickData): https://dash.plotly.com/interactive-graphing            ║
# ║  Docs (Card): https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/  ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ------------
# Run
# -------------
if __name__ == "__main__":
    app.run(debug=True)
