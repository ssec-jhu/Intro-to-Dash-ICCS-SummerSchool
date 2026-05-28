# Visualising Data with dcc.Graph
# ================================
# In this exercise we display interactive charts using dcc.Graph
# and Plotly Express — still no callbacks!
#
# The data is loaded from a shared CSV file.
#
# Run the app and explore the charts. Then tweak the code to try
# different chart types and settings.

from pathlib import Path

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash()


# ── Load Data ────────────────────────────────────────────────────
data_path = Path(__file__).parent.parent / "data" / "rse_data.csv"
df = pd.read_csv(data_path)

# ── Chart 1: Scatter — Coffee vs. Lines of Code ─────────────────
fig_scatter = px.scatter(
    df,
    x="coffees_per_day",
    y="lines_of_code",
    size="bugs_introduced",
    color="country",
    # color="workshop_rating"  # Try: set color="workshop_rating" instead of country
    hover_name="research_software_engineer",
    hover_data=["university"],
    title="Coffee Consumption vs. Lines of Code Written",
    labels={
        "coffees_per_day": "Coffees per Day",
        "lines_of_code": "Lines of Code",
        "bugs_introduced": "Bugs Introduced (bubble size)",
    },
)
fig_scatter.update_layout(title_x=0.5)


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
fig_bar.update_layout(title_x=0.5)


app.layout = html.Div(
    children=[
        html.H2("RSE Data — Charts"),
        html.P(
            "Two charts built from a shared CSV dataset of research software engineers. "
            "No callbacks needed — Plotly charts are interactive out of the box! "
            "Try hovering, zooming, and clicking the legend. "
            "Wrap any Plotly figure in a dcc.Graph to display it in Dash."
        ),
        html.Div(
            [
                html.A(
                    "Plotly Graphs docs",
                    href="https://plotly.com/python/",
                    target="_blank",
                ),
                html.A(
                    "Scatter plot docs",
                    href="https://plotly.com/python/line-and-scatter/",
                    target="_blank",
                ),
                html.A(
                    "Bar chart docs",
                    href="https://plotly.com/python/bar-charts/",
                    target="_blank",
                ),
            ],
            # space them out horizontally with flexbox
            style={"display": "flex", "gap": "20px"},
        ),
        # --------------
        # dcc.Graph (Scatter plot)
        # --------------
        dcc.Graph(figure=fig_scatter),
        # --------------
        # dcc.Graph (Bar)
        # --------------
        dcc.Graph(figure=fig_bar),
    ],
    style={"maxWidth": "1000px", "margin": "auto", "padding": "20px"},
)

if __name__ == "__main__":
    app.run(debug=True)
