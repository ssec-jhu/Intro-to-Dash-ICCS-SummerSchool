"""
Interactive Gapminder Dashboard — SOLUTION
==========================================
This is the fully working solution for 04_interactive_exercise.py.
Run this file to see the finished app, then go back to the exercise and try it yourself!
"""

# ------------
# Imports
# -------------
from dash import Dash, html, dcc, callback, Input, Output  # https://dash.plotly.com/
import plotly.express as px  # https://plotly.com/python/plotly-express/
import dash_ag_grid as dag  # https://dash.plotly.com/dash-ag-grid
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

dropdown = html.Div(
    children=[
        dcc.Dropdown(
            id="id-dropdown-continent",
            options=[{"label": c, "value": c} for c in df["continent"].unique()],
            value=df["continent"].unique().tolist(),
            multi=True,
        ),
    ],
)

slider = html.Div(
    children=[
        dcc.Slider(
            id="id-slider-year",
            min=int(df["year"].min()),
            max=int(df["year"].max()),
            step=5,
            value=2007,
            marks={str(y): str(y) for y in df["year"].unique()},
        ),
    ],
)

grid = html.Div(
    children=[
        dag.AgGrid(
            id="id-grid-data",
            columnDefs=[{"field": col} for col in df.columns],
            rowData=df.to_dict("records"),
            dashGridOptions={"pagination": True, "paginationPageSize": 10},
            columnSize="sizeToFit",
            # className="ag-theme-alpine dbc-ag-grid",
        ),
    ],
)

graph = html.Div(
    children=[
        dcc.Graph(id="id-graph-scatter"),
    ],
)


# ------------
# Layout
# -------------
app.layout = dbc.Container(
    [
        html.H1("Intro to Dash Interactive Exercise"),
        # Dropdown: filter by continent
        html.Label("Select Continent(s):"),
        dropdown,
        html.Br(),
        # Slider: select year
        html.Label("Select Year:"),
        slider,
        html.Br(),
        # AG Grid: show filtered data
        grid,
        html.Br(),
        # Graph: scatter plot
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


# ------------
# Callback 1: Update the AG Grid
# -------------
# Docs: https://dash.plotly.com/basic-callbacks
@callback(
    Output("id-grid-data", "rowData"),
    Input("id-dropdown-continent", "value"),
    Input("id-slider-year", "value"),
)
def update_table(selected_continents, selected_year):
    filtered = df[
        (df["continent"].isin(selected_continents)) & (df["year"] == selected_year)
    ]
    return filtered.to_dict("records")


# ------------
# Callback 2: Update the scatter chart
# -------------
# Docs: https://dash.plotly.com/basic-callbacks
@callback(
    Output("id-graph-scatter", "figure"),
    Input("id-dropdown-continent", "value"),
    Input("id-slider-year", "value"),
)
def update_graph(selected_continents, selected_year):
    filtered = df[
        (df["continent"].isin(selected_continents)) & (df["year"] == selected_year)
    ]
    fig = px.scatter(
        filtered,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        title=f"Life Expectancy vs GDP per Capita ({selected_year})",
        log_x=True,
        size_max=40,
    )
    return fig


# ------------
# Callback 3: Click on graph → show country details in Card
# -------------
# Docs: https://dash.plotly.com/interactive-graphing
@callback(
    Output("id-card-header", "children"),
    Output("id-card-country", "children"),
    Input("id-graph-scatter", "clickData"),
    Input("id-slider-year", "value"),
)
def show_country_detail(click_data, selected_year):
    if click_data is None:
        return "Country Details", html.P(
            "Click on a point in the chart to see country details.",
            className="text-muted",
        )

    # get the country name from clickData and look up its stats in df
    point = click_data["points"][0]
    country = point["hovertext"]

    # filter df for that country and the selected year and get the first row
    row = df[(df["country"] == country) & (df["year"] == selected_year)].iloc[0]

    header = f"🌍 {country}"
    body = [
        html.P(f"Year: {selected_year}"),
        html.P(f"Continent: {row['continent']}"),
        html.P(f"Life Expectancy: {row['lifeExp']:.1f} years"),
        html.P(f"GDP per Capita: ${row['gdpPercap']:,.0f}"),
        html.P(f"Population: {row['pop']:,}"),
    ]
    return header, body


# ------------
# Run
# -------------
if __name__ == "__main__":
    app.run(debug=True)
