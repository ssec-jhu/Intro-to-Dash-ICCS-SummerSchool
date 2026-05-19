# This is a simple Dash application that demonstrates how to use callbacks 
# to create interactivity.
from dash import Dash, html, Input, Output, callback


# Create a Dash application instance - consider this as the main 
# entry point of your Dash app.
app = Dash()

app.layout = html.Div(
    [
        # Define a button and a div to display the output. 
        # The button has an id of "btn"
        html.Button("Click Me", id="id-btn"),
        html.Div(id="id-output")
    ])


@callback(
    # The Output() function specifies that the output of this callback will be
    # the "children" property of the div with id "id-output".
    Output("id-output", "children"),
    # the Input() function specifies that this callback should be triggered
    # whenever the "n_clicks" property of the button with id "id-btn"
    Input("id-btn", "n_clicks")
)
def update_output(clicks):
    # This function will be called whenever the button is clicked.
    if clicks is None:
        return "Button not clicked yet"

    return f"Clicked {clicks} times"


if __name__ == "__main__":
    app.run(debug=True)
