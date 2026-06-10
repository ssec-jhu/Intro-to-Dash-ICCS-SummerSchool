"""
Interactive Gapminder Dashboard — EXERCISE
===========================================
Build an interactive dashboard step by step!
Fill in the TODOs below to connect Dash components to a scatter chart.

If you get stuck, check the solution: 06_interactive_exercise_solution.py
"""

# --------------------------
# Imports
# --------------------------
from dash import Dash, html  # https://dash.plotly.com/
import plotly.express as px  # https://plotly.com/python/plotly-express/
import dash_bootstrap_components as dbc  # https://dash-bootstrap-components.opensource.faculty.ai/
from dash_bootstrap_templates import load_figure_template

# --------------------------
# Data
# --------------------------
# df columns: country, continent, year, lifeExp, pop, gdpPercap, iso_alpha, iso_num
df = px.data.gapminder()

# --------------------------
# App setup
# --------------------------
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css])
# loads the template and sets it as the default
load_figure_template("minty")


def get_dropdown_component():
    """Continent multi-select dropdown."""
    # ╔════════════════════════════════════════════════════════════════════╗
    # ║ TODO 1: Complete get_dropdown_component()                          ║
    # ║                                                                    ║
    # ║  Return an html.Div containing a dcc.Dropdown with:                ║
    # ║  - id: "id-dropdown-continent"                                     ║
    # ║  - multi=True (allow selecting multiple continents)                ║
    # ║  - options: one option per unique value in df["continent"]         ║
    # ║  - value: default to ALL continents selected                       ║
    # ║                                                                    ║
    # ║  Docs: https://dash.plotly.com/dash-core-components/dropdown       ║
    # ╚════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dcc.Dropdown here!"
        ],
    )


def get_range_slider_component():
    """Year range slider to filter the table."""
    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║ TODO 2: Complete get_range_slider_component()                        ║
    # ║                                                                      ║
    # ║  Return an html.Div containing a dcc.RangeSlider with:               ║
    # ║  - id: "id-slider-year-range"                                        ║
    # ║  - min: df["year"].min()                                             ║
    # ║  - max: df["year"].max()                                             ║
    # ║  - value: [min_year, max_year] (default to full range)               ║
    # ║                                                                      ║
    # ║  Docs: https://dash.plotly.com/dash-core-components/rangeslider      ║
    # ╚══════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dcc.RangeSlider here!"
        ],
    )


def get_switch_component():
    """Toggle switch for log x-axis on the scatter chart."""
    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║ TODO 3: Complete get_switch_component()                              ║
    # ║                                                                      ║
    # ║  Return an html.Div containing a dbc.Switch with:                    ║
    # ║  - id: "id-switch-log"                                               ║
    # ║  - label: "Log x-axis"                                               ║
    # ║  - value: True (log scale on by default)                             ║
    # ║                                                                      ║
    # ║  Docs: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/  
    # ╚══════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dbc.Switch here!"
        ],
    )


def get_grid_component():
    """AG Grid showing the gapminder data."""
    # ╔════════════════════════════════════════════════════════════════════╗
    # ║ TODO 4: Complete get_grid_component()                              ║
    # ║                                                                    ║
    # ║  Return an html.Div containing a dag.AgGrid with:                  ║
    # ║  - id: "id-grid-data"                                              ║
    # ║  - columnDefs: [{"field": col} for col in df.columns]              ║
    # ║  - rowData: df.to_dict("records")                                  ║
    # ║  - dashGridOptions: {"pagination": True, "paginationPageSize": 10} ║
    # ║  - columnSize: "sizeToFit"                                         ║
    # ║                                                                    ║
    # ║  Docs: https://dash.plotly.com/dash-ag-grid/getting-started        ║
    # ╚════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dag.AgGrid here!"
        ],
    )


def get_graph_component(log_x=True):
    """Scatter chart with an initial figure. log_x sets the default x-axis scale."""
    # ╔══════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 5: Complete get_graph_component(log_x)                             ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a dcc.Graph with:                        ║
    # ║  - id: "id-graph-scatter"                                               ║
    # ║  - figure: a px.scatter of the FULL df with:                            ║
    # ║      x = "gdpPercap"                                                    ║
    # ║      y = "lifeExp"                                                      ║
    # ║      size = "pop"          (maps to bubble size)                        ║
    # ║      size_max = 40   (max bubble pixel size — prevents overlap)         ║
    # ║      color = "continent"   (maps to point color + legend)               ║
    # ║      hover_name = "country"   (bold title in hover tooltip)             ║
    # ║      hover_data = ["year"]   (extra info shown in tooltip)              ║
    # ║      log_x = log_x   (use the function parameter!)                      ║
    # ║                                                                         ║
    # ║  Docs:                                                                  ║
    # ║    https://dash.plotly.com/dash-core-components/graph                   ║
    # ║    https://plotly.com/python/line-and-scatter/                          ║
    # ║    https://plotly.com/python-api-reference/generated/plotly.express.scatter.html  ║
    # ╚══════════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dcc.Graph with initial px.scatter figure here!"
        ],
    )


# --------------------------
# Layout
# --------------------------
app.layout = dbc.Container(
    [
        html.H1("Intro to Dash Interactive Exercise"),
        # Dropdown: filter by continent
        html.Label("Select Continent(s):"),
        get_dropdown_component(),
        html.Br(),
        # RangeSlider: filter table by year range
        html.Label("Select Year Range:"),
        get_range_slider_component(),
        html.Br(),
        # AG Grid: show filtered data
        get_grid_component(),
        html.Br(),
        # Switch: toggle log x-axis on graph
        get_switch_component(),
        # Graph: scatter plot
        html.Div(id="id-graph-container", children=[get_graph_component(log_x=True)]),
        html.Br(),
        # Country detail in a dbc.Card (populated by clicking a point on the graph)
        dbc.Card(
            [
                dbc.CardHeader(
                    children="Country Details",
                    id="id-card-header"
                ),
                dbc.CardBody(
                    id="id-card-country"
                ),
            ]
        ),
    ],
    # this sets the overall theme and styling for the app using Bootstrap
    className="dbc dbc-ag-grid",
    style={"maxWidth": "900px", "padding": "20px"},
)

# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 6:                                                                    ║
# ║     Write a @callback that updates the AG Grid based on                    ║
# ║     selected continents (the dropdown) and year range (the range slider)   ║
# ║                                                                            ║
# ║  - Output: the "rowData" property of "id-grid-data"                        ║
# ║  - Inputs:                                                                 ║
# ║      1. "value" property of "id-dropdown-continent" (list of continents)   ║
# ║      2. "value" property of "id-slider-year-range" (a list: [min, max])    ║
# ║  - Inside the function:                                                    ║
# ║      1. Filter df where continent is in selected_continents                ║
# ║         AND year >= year_range[0] AND year <= year_range[1]                ║
# ║      2. Return filtered.to_dict("records")                                 ║
# ║                                                                            ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                             ║
# ╚════════════════════════════════════════════════════════════════════════════╝

# --------------------------
# Callback 1: Update the AG Grid - STUB
# --------------------------
# @callback(
#     Output("id-grid-data", "rowData"),
#     Input( ... ),
#     Input( ... ),
# )
# def update_table(selected_continents, year_range):
#     # TODO: filter df by continent and year range, return as list of dicts


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 7:                                                                    ║
# ║     Write a @callback that updates the scatter chart's x-axis scale  to be ║
# ║     log based or not log based                                             ║
# ║                                                                            ║
# ║  - Output: the "children" property of "id-graph-container"                 ║
# ║  - Input: "value" property of "id-switch-log" (True/False)                 ║
# ║  - Inside the function:                                                    ║
# ║      1. Call get_graph_component(log_x=bool(log_x))                        ║
# ║      2. Return the result                                                  ║
# ║  - Users can filter continents using the chart's built-in legend!          ║
# ║                                                                            ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                             ║
# ╚════════════════════════════════════════════════════════════════════════════╝

# --------------------------
# Callback 2: Update the scatter chart - STUB
# --------------------------
# @callback(
#     Output("id-graph-container", "children"),
#     Input( ... ),
# )
# def update_graph(log_x):
#     # TODO: call get_graph_component with log_x and return the result


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ TODO 8:                                                                    ║
# ║     Write a @callback that shows country details in the dbc.Card           ║
# ║     when you click a point on the scatter chart                            ║
# ║                                                                            ║
# ║  - Outputs:                                                                ║
# ║      1. "children" property of "id-card-header"(output country name here)  ║
# ║      2. "children" property of "id-card-country" (output other info here)  ║
# ║  - Input:                                                                  ║
# ║      the "clickData" property of "id-graph-scatter"                        ║
# ║      (a dictionary containing information about the clicked point)         ║
# ║  - Inside the function:                                                    ║
# ║      1. If click_data is None, return a placeholder header and message     ║
# ║      2. Get the clicked point: point = click_data["points"][0]             ║
# ║      3. Extract info directly from the point dict:                         ║
# ║           - country name:   point["hovertext"]                             ║
# ║           - gdpPerCap:      point["x"]                                     ║
# ║           - lifeExp:        point["y"]                                     ║
# ║      4. Return:                                                            ║
#            country name in id-card-header                                    ║
#            other info in id-card-country as id-card-country ║
# ║                                                                            ║
# ║  Docs (clickData): https://dash.plotly.com/interactive-graphing            ║
# ║  Docs (Card): https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
# ╚════════════════════════════════════════════════════════════════════════════╝

# --------------------------
# Callback 3: Click on graph → show country details in Card - STUB
# --------------------------
# @callback(
#     Output("id-card-header", "children"),
#     Output("id-card-country", "children"),
#     Input( ... ),
# )
# def show_country_detail(click_data):
#     # TODO: if click_data is None, return placeholder.
#     # Otherwise extract country, gdp, life_exp, year directly from
#     # click_data["points"][0] and return header + body components.


# --------------------------
# Run
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
