# Visualising Data with dcc.Graph and DataTable
# ===============================================
# In this exercise we display charts (dcc.Graph) and an interactive
# table (dash_table.DataTable) — still no callbacks!
#
# We'll use a fun synthetic dataset.
# their coffee habits, coding output, and bug counts.
#
# Run the app and explore the charts. Then tweak the code to try
# different chart types and table settings.

from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

# ── Synthetic Summer School Data ─────────────────────────────────
# This is our "dataset" — feel free to add rows or columns!
df = pd.DataFrame(
    {
        "research_software_engineer": [
            "Alice",
            "Bob",
            "Carlos",
            "Diana",
            "Elena",
            "Femi",
            "Greta",
            "Hassan",
            "Isla",
            "Jun",
            "Kofi",
            "Lena",
            "Miguel",
            "Noor",
            "Oscar",
        ],
        "country": [
            "UK",
            "USA",
            "Mexico",
            "Germany",
            "Spain",
            "Nigeria",
            "Sweden",
            "Egypt",
            "Scotland",
            "South Korea",
            "Ghana",
            "Norway",
            "Brazil",
            "Pakistan",
            "Argentina",
        ],
        "coffees_per_day": [3, 1, 5, 2, 4, 0, 6, 2, 4, 1, 3, 7, 4, 2, 5],
        "lines_of_code": [
            120,
            85,
            310,
            95,
            250,
            60,
            420,
            110,
            275,
            70,
            190,
            500,
            220,
            130,
            350,
        ],
        "bugs_introduced": [12, 5, 42, 8, 30, 3, 55, 9, 28, 4, 15, 61, 25, 11, 38],
        "workshop_rating": [5, 4, 5, 3, 4, 5, 5, 4, 3, 5, 4, 5, 4, 5, 3],
        "favourite_snack": [
            "Biscuits",
            "Chips",
            "Tacos",
            "Pretzels",
            "Churros",
            "Puff Puff",
            "Kanelbullar",
            "Koshari",
            "Shortbread",
            "Tteok",
            "Kelewele",
            "Lefse",
            "Pão de queijo",
            "Samosa",
            "Empanadas",
        ],
    }
)


# ── Chart 1: Scatter — Coffee vs. Lines of Code ─────────────────
fig_scatter = px.scatter(
    df,
    x="coffees_per_day",
    y="lines_of_code",
    size="bugs_introduced",
    color="country",
    # Try: set color="workshop_rating" instead of country
    hover_name="research_software_engineer",
    hover_data=["favourite_snack"],
    title="Coffee Consumption vs. Lines of Code Written",
    labels={
        "coffees_per_day": "Coffees per Day",
        "lines_of_code": "Lines of Code",
        "bugs_introduced": "Bugs Introduced (bubble size)",
    },
)


# ── Chart 2: Bar — Bug Rate (bugs per 100 lines of code) ────────
df["bug_rate"] = (df["bugs_introduced"] / df["lines_of_code"] * 100).round(1)

fig_bar = px.bar(
    df.sort_values("bug_rate", ascending=False),
    x="research_software_engineer",  # categorical x-axis with RSE names
    y="bug_rate",  # numeric y-axis showing bugs per 100 lines of code
    color="coffees_per_day",  # colour bars by coffee consumption
    color_continuous_scale="RdYlGn_r",
    title="Bugs per 100 Lines of Code",
    labels={
        # these labels will show up in the hover tooltip and axes
        "research_software_engineer": "RSE",
        "bug_rate": "Bugs per 100 Lines",
        "coffees_per_day": "Coffees/Day",
    },
    hover_data=["lines_of_code", "bugs_introduced", "country"],
)

# ── Layout ───────────────────────────────────────────────────────
app = Dash()

app.layout = html.Div(
    style={"maxWidth": "1000px", "margin": "auto", "padding": "20px"},
    children=[
        html.H2("Summer School Data Explorer"),
        html.P(
            "Below you'll find two charts and a data table — all built from "
            "a synthetic dataset of research software engineers. "
            "No callbacks needed — Plotly charts are interactive out of the box! "
            "Try hovering, zooming, and clicking the legend."
        ),
        # --------------
        # dcc.Graph (Scatter)
        # --------------
        html.H3("dcc.Graph — Scatter Plot"),
        html.P(
            "dcc.Graph renders interactive Plotly figures. "
            "Hover over points to see details, zoom, pan, or click legend items to toggle traces."
        ),
        html.A(
            "Graph docs",
            href="https://dash.plotly.com/dash-core-components/graph",
            target="_blank",
        ),
        dcc.Graph(figure=fig_scatter),
        html.Br(),
        # --------------
        # dcc.Graph (Bar)
        # --------------
        html.H3("dcc.Graph — Bar Chart"),
        html.P(
            "The same dcc.Graph component can display any Plotly figure — "
            "bar charts, pie charts, histograms, and more."
        ),
        html.A(
            "Graph docs",
            href="https://dash.plotly.com/dash-core-components/graph",
            target="_blank",
        ),
        dcc.Graph(figure=fig_bar),
        html.Br(),
        # --------------
        # dash_table.DataTable
        # --------------
        html.H3("dash_table.DataTable"),
        html.P(
            "DataTable displays tabular data with built-in sorting, filtering, and pagination."
        ),
        html.A(
            "DataTable docs", href="https://dash.plotly.com/datatable", target="_blank"
        ),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": col, "id": col} for col in df.columns],
            page_size=8,
            sort_action="native",
            filter_action="native",
            style_header={"fontWeight": "bold"},
        ),
        html.Br(),
        html.Br(),
        html.Br(),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
