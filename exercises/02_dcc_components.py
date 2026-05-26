# Exploring Dash Core Components (dcc)
# =====================================
# Dash ships with a set of interactive UI components called
# Dash Core Components (dcc). These include dropdowns, sliders,
# checklists, text inputs, and more.
#
# This exercise is a playground — run the app and see how each
# component renders. Then start tweaking!
#
# There are NO callbacks here — these components just display
# on the page. In a later exercise we'll wire them up to make
# the app respond to user input.

from dash import Dash, html, dcc
from datetime import date

app = Dash()

app.layout = html.Div(
    # this style centers the content and adds some padding around the edges
    style={"maxWidth": "800px", "margin": "auto", "padding": "20px"},
    children=[
        # --------------
        # dcc.Markdown
        # --------------
        # dcc.Markdown lets you write rich text using Markdown syntax.
        dcc.Markdown("""
            ## ICCS Summer School
            Welcome! This page demonstrates various **Dash Core Components**.  
            None of these are wired up yet — they just *look pretty*.  
            Your mission: **play with the code** and see what changes! 
            This text is written using dcc.Markdown.

            ---
            ### Try these out:
            - Can you add a **second Dropdown** for lunch preference?
            - Can you change the **Slider marks** to show actual coffee cup counts?
            - Try wrapping components in `html.Div` with a coloured background (`style={'backgroundColor': '#f0f8ff'}`)
        """),
        # This adds a spacing between the current component and the next component.
        html.Br(),
        # --------------
        # dcc.Dropdown
        #
        # --------------
        html.H3("dcc.dropdown"),
        html.A(
            "Dropdown docs",
            href="https://dash.plotly.com/dash-core-components/dropdown",
            target="_blank",
        ),
        html.Div("Which workshop track interests you?"),
        dcc.Dropdown(
            options=[
                "Machine Learning",
                "Data Visualisation",
                "High-Performance Computing",
                "Research Software Engineering",
                "Climate Modelling",
                "Intor to Git and GitHub",
            ],
            value="Data Visualisation",
            # multi=True,           # Try: set multi=True to allow selecting multiple tracks
            # clearable = False,    # Try: add clearable=False to prevent clearing the selection
            # placeholder = "Pick a track...", # Try: add placeholder="Pick a track..." and remove the value
        ),
        html.Br(),
        # --------------
        # dcc.Slider
        # --------------
        html.H3("dcc.Slider"),
        html.A(
            "Slider docs",
            href="https://dash.plotly.com/dash-core-components/slider",
            target="_blank",
        ),
        html.Div("Caffeine level today (1 = herbal tea, 10 = pure espresso IV drip):"),
        dcc.Slider(
            min=1,
            max=10,
            step=1,
            value=6,
            # marks={1: "😴", 3: "🍵", 5: "☕", 7: "☕☕", 10: "🚀"},
            marks={1: "😴", 3: "🍵", 5: "☕", 7: "☕☕", 10: "🚀"},
            # Try: change the marks dict — use numbers, words, or more emojis
            # Try: set tooltip={"placement": "bottom", "always_visible": True}
        ),
        html.Br(),
        # --------------
        # dcc.RangeSlider
        # --------------
        html.H3("dcc.RangeSlider"),
        html.A(
            "RangeSlider docs",
            href="https://dash.plotly.com/dash-core-components/rangeslider",
            target="_blank",
        ),
        html.Div("Preferred session hours (24h clock):"),
        dcc.RangeSlider(
            min=8,
            max=20,
            step=1,
            value=[9, 17],
            marks={h: f"{h}:00" for h in range(8, 21, 2)},
            # Try: narrow the range (min=9, max=18)
            # Try: change step=0.5 for half-hour granularity
        ),
        html.Br(),
        # --------------
        # dcc.RadioItems
        # --------------
        html.H3("dcc.RadioItems"),
        html.A(
            "RadioItems docs",
            href="https://dash.plotly.com/dash-core-components/radioitems",
            target="_blank",
        ),
        html.Div("Favourite programming language:"),
        dcc.RadioItems(
            options=["Python", "R", "Julia", "C++", "Fortran"],
            value="Python",
            # Try: set inline=True to display horizontally
            # Try: add a new language to the list
        ),
        html.Br(),
        # --------------
        # dcc.Checklist
        # --------------
        html.H3("dcc.Checklist"),
        html.A(
            "Checklist docs",
            href="https://dash.plotly.com/dash-core-components/checklist",
            target="_blank",
        ),
        html.Div("Topics you'd like to explore (select all that apply):"),
        dcc.Checklist(
            options=[
                "Neural Networks",
                "Bayesian Inference",
                "Parallel Computing",
                "Reproducibility",
                "Scientific Workflows",
            ],
            value=["Neural Networks", "Reproducibility"],
            inline=True,
            # Try: set inline=False to stack them vertically
            # Try: remove the value list — what happens on load?
        ),
        html.Br(),
        # --------------
        # dcc.Input
        # --------------
        html.H3("dcc.Input"),
        html.A(
            "Input docs",
            href="https://dash.plotly.com/dash-core-components/input",
            target="_blank",
        ),
        html.Div("Your name:"),
        dcc.Input(
            placeholder="e.g. Ada Lovelace",
            type="text",
            value="",
            style={"width": "100%"},
            # Try: change type to "password" or "email"
            # Try: add debounce=True (useful when paired with callbacks later)
        ),
        html.Br(),
        html.Br(),
        html.Div("Years of coding experience:"),
        dcc.Input(
            placeholder="0",
            type="number",
            min=0,
            max=50,
            value=3,
            # Try: change min/max bounds
            # Try: add step=0.5 for half-year increments
        ),
        html.Br(),
        html.Br(),
        # --------------
        # dcc.Textarea
        # --------------
        html.H3("dcc.Textarea"),
        html.A(
            "Textarea docs",
            href="https://dash.plotly.com/dash-core-components/textarea",
            target="_blank",
        ),
        html.Div("Tell us about your research project:"),
        dcc.Textarea(
            placeholder="Describe your project in a few sentences...",
            value="",
            style={"width": "100%", "height": "100px"},
            # Try: change the height to 200px
            # Try: pre-fill with a default value
        ),
        html.Br(),
        # --------------
        # dcc.DatePickerSingle
        # --------------
        html.H3("dcc.DatePickerSingle"),
        html.A(
            "DatePickerSingle docs",
            href="https://dash.plotly.com/dash-core-components/datepickersingle",
            target="_blank",
        ),
        html.Div("Arrival date:"),
        dcc.DatePickerSingle(
            date=date(2026, 7, 14),
            display_format="DD/MM/YYYY",
            # Try: change display_format to "YYYY-MM-DD" or "MMMM D, YYYY"
            # Try: add min_date_allowed and max_date_allowed
        ),
        html.Br(),
        html.Br(),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
