"""
Interactive Gapminder Dashboard — EXERCISE
===========================================
Build an interactive dashboard step by step!
Fill in the TODOs below to connect Dash components to a scatter chart.

If you get stuck, check the solution: 07_interactive_exercise_solution.py
"""

# --------------------------
# Imports
# --------------------------
from dash import Dash, html, dcc  # https://dash.plotly.com/
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
    # ╔═════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 1: get_dropdown_component()                                        ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a dcc.Dropdown that lets users pick      ║
    # ║  one or more continents to filter the data.                             ║
    # ║                                                                         ║
    # ║  Properties:                                                            ║
    # ║  - id: "id-dropdown-continent"                                          ║
    # ║  - options: the unique continent values from df["continent"]            ║
    # ║  - value: all , one or no continents selected by default                ║
    # ║  - multi-select enabled                                                 ║
    # ║                                                                         ║
    # ║  Docs: https://dash.plotly.com/dash-core-components/dropdown            ║
    # ║                                                                         ║
    # ║  Hints:                                                                 ║
    # ║  - df["continent"].unique() gives a list of unique values               ║
    # ║  - the multi property (boolean) enables multi-select                    ║
    # ╚═════════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dcc.Dropdown here!"
        ],
    )


def get_range_slider_component():
    """Year range slider to filter the table."""
    # ╔═════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 2: get_range_slider_component()                                    ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a dcc.RangeSlider that lets users        ║
    # ║  select a year range to filter the table.                               ║
    # ║                                                                         ║
    # ║  Properties:                                                            ║
    # ║  - id: "id-slider-year-range"                                           ║
    # ║  - min/max: derived from df["year"]                                     ║
    # ║  - value: default to the full range [min_year, max_year]                ║
    # ║                                                                         ║
    # ║  Docs: https://dash.plotly.com/dash-core-components/rangeslider         ║
    # ║                                                                         ║
    # ║  Hints:                                                                 ║
    # ║  - df["year"].min() gets the minimum year as an integer                 ║
    # ║  - df["year"].max() gets the maximum year as an integer                 ║
    # ║  - value takes a two-element list: [min, max]                           ║
    # ╚═════════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dcc.RangeSlider here!"
        ],
    )


def get_switch_component():
    """Toggle switch for log x-axis on the scatter chart."""
    # ╔══════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 3: get_switch_component()                                          ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a dbc.Switch that controls whether       ║
    # ║  the scatter chart x-axis is logarithmic or linear. You already         ║
    # ║  imported dbc in exercise 06 — check the dbc docs for a Switch.         ║
    # ║                                                                         ║
    # ║  Properties:                                                            ║
    # ║  - id: "id-switch-log"                                                  ║
    # ║  - label: anything descriptive                                          ║
    # ║  - value: should default be set to on or off?                            ║
    # ║                                                                         ║
    # ║  Docs: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/                                                ║
    # ║                                                                         ║
    # ║  Hints:                                                                 ║
    # ║  - dbc.Switch value is a boolean (True/False)                           ║
    # ╚═════════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dbc.Switch here!"
        ],
    )


def get_grid_component():
    """AG Grid showing the gapminder data."""
    # ╔═════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 4: get_grid_component()                                            ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a paginated data table that shows        ║
    # ║  the gapminder DataFrame. Look at exercise 04_ag_grid.py to see how     ║
    # ║  a grid is set up — what import, properties, and options did it use?    ║
    # ║                                                                         ║
    # ║  Properties:                                                            ║
    # ║  - id: "id-grid-data"                                                   ║
    # ║  - enable pagination (10 rows per page)                                 ║
    # ║  - set columnSize: "sizeToFit"                                          ║
    # ║                                                                         ║
    # ║  Docs: https://dash.plotly.com/dash-ag-grid/getting-started             ║
    # ║                                                                         ║
    # ║  Hints:                                                                 ║
    # ║  - check 04_ag_grid.py: what library is imported and how is rowData     ║
    # ║    set from a DataFrame?                                                ║
    # ║  - [{"field": col} for col in df.columns] builds column definitions     ║
    # ║    for every column automatically                                       ║
    # ╚═════════════════════════════════════════════════════════════════════════╝
    return html.Div(
        children=[
            "add your dash ag-grid here!"
        ],
    )


def get_graph_component(log_x: bool = True):
    """Scatter chart with an initial figure. log_x sets the default x-axis scale."""
    # ╔═════════════════════════════════════════════════════════════════════════╗
    # ║ TODO 5: get_graph_component(log_x)                                      ║
    # ║                                                                         ║
    # ║  Return an html.Div containing a dcc.Graph with a px.scatter bubble     ║
    # ║  chart of the full gapminder dataset. See 03_dcc_graph.py for how       ║
    # ║  px.scatter and dcc.Graph work together.                                ║
    # ║                                                                         ║
    # ║  Properties:                                                            ║
    # ║  - id: "id-graph-scatter"                                               ║
    # ║  - figure: a px.scatter of the full df where:                           ║
    # ║      x-axis: GDP per capita column                                      ║
    # ║      y-axis: life expectancy column                                     ║
    # ║      bubble size: population column                                     ║
    # ║      color: by continent                                                ║
    # ║      hover: set hover_name="country" and hover_data=["year"],           ║
    # ║      log_x: use the function parameter                                  ║
    # ║                                                                         ║
    # ║  Docs: https://dash.plotly.com/dash-core-components/graph               ║
    # ║        https://plotly.com/python/line-and-scatter/                      ║
    # ║                                                                         ║
    # ║  Hints:                                                                 ║
    # ║  - log_x is a boolean (True/False), not an integer                      ║
    # ║  - size_max=40 caps the largest bubble so they don't overlap            ║
    # ║  - hover_name makes a bold title; hover_data adds extra tooltip fields  ║
    # ║  - create the figure first: fig = px.scatter(df, ...)                   ║
    # ║  - then pass it to dcc.Graph(id=..., figure=fig)                        ║
    # ╚═════════════════════════════════════════════════════════════════════════╝
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

# ╔═════════════════════════════════════════════════════════════════════════╗
# ║ TODO 6: Callback — update the AG Grid                                   ║
# ║                                                                         ║
# ║  Write a @callback that filters the grid when the user changes the      ║
# ║  continent dropdown or the year range slider.                           ║
# ║                                                                         ║
# ║  Properties:                                                            ║
# ║  - Output: "rowData" property of "id-grid-data"                         ║
# ║  - Inputs:                                                              ║
# ║      1. "value" of "id-dropdown-continent" (list of continents)         ║
# ║      2. "value" of "id-slider-year-range"  (list: [min, max])           ║
# ║  - Filter df by continent AND year range, return as list of dicts       ║
# ║                                                                         ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                          ║
# ║                                                                         ║
# ║  Hints:                                                                 ║
# ║  - Think: what do you need to add to your dash imports for callbacks?   ║
# ║    Look back at exercise 06 for reference.                              ║
# ║  - df[df["col"].isin(values)] filters rows by a list of values          ║
# ║  - chain multiple conditions with & (wrap each in parentheses):         ║
# ║      filtered = df[(condition_1) & (condition_2)]                       ║
# ║    e.g. df[(df["continent"].isin(continents)) & (df["year"] >= min)]    ║
# ║  - for year range: (df["year"] >= year_range[0]) &                      ║
# ║                     (df["year"] <= year_range[1])                       ║
# ║  - convert result to records: filtered.to_dict("records")               ║
# ╚═════════════════════════════════════════════════════════════════════════╝

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


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║ TODO 7: Callback — toggle log scale on scatter chart                    ║
# ║                                                                         ║
# ║  Write a @callback that re-renders the scatter chart when the user      ║
# ║  flips the log-scale switch.                                            ║
# ║                                                                         ║
# ║  Properties:                                                            ║
# ║  - Output: "children" property of "id-graph-container"                  ║
# ║  - Input: "value" property of "id-switch-log" (True/False)              ║
# ║  - Call get_graph_component(log_x=...) and return the result            ║
# ║                                                                         ║
# ║  Docs: https://dash.plotly.com/basic-callbacks                          ║
# ║                                                                         ║
# ║  Hints:                                                                 ║
# ║  - bool(value) ensures the switch value is a Python boolean             ║
# ║  - users can still filter continents via the chart's built-in legend    ║
# ╚═════════════════════════════════════════════════════════════════════════╝

# --------------------------
# Callback 2: Update the scatter chart - STUB
# --------------------------
# @callback(
#     Output("id-graph-container", "children"),
#     Input( ... ),
# )
# def update_graph(log_x):
#     # TODO: call get_graph_component with log_x and return the result


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║ TODO 8: Callback — show country details on click  (CHALLENGE)           ║
# ║                                                                         ║
# ║  This one is more challenging! Write a @callback that populates the     ║
# ║  dbc.Card with details about whichever point the user clicks on the     ║
# ║  scatter chart.                                                         ║
# ║                                                                         ║
# ║  Properties:                                                            ║
# ║  - Outputs:                                                             ║
# ║      1. "children" of "id-card-header" (country name)                   ║
# ║      2. "children" of "id-card-country" (other details)                 ║
# ║  - Input: "clickData" property of "id-graph-scatter"                    ║
# ║  - If click_data is None, return a placeholder message                  ║
# ║  - Otherwise extract info from the clicked point and display it         ║
# ║                                                                         ║
# ║  Docs: https://dash.plotly.com/interactive-graphing                     ║
# ║                                                                         ║
# ║  Hints:                                                                 ║
# ║  - click_data["points"][0] returns a dict describing the clicked        ║
# ║    bubble. It looks like:                                               ║
# ║      {"hovertext": "Canada", "x": 36319.2, "y": 80.6,                   ║
# ║       "marker.size": 33390141, "customdata": [2007], ...}               ║
# ║  - use "hovertext" for country, "x" for gdpPercap, "y" for lifeExp      ║
# ║  - a callback can return multiple outputs as a tuple:                   ║
# ║      return header_value, body_value                                    ║
# ╚═════════════════════════════════════════════════════════════════════════╝

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
#     # Otherwise extract country, gdp, life_exp from
#     # click_data["points"][0] and return header + body components.


# --------------------------
# Run
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
