# This is a simple Dash application that displays 
# "Hello Dash" as a heading. To run this code, 
# make sure you have the Dash library installed in 
# your Python environment. 
# You can install required dependencies using the requirements.txt 
# file provided in the repository: 
# run `pip install -r requirements.txt` in your terminal.
from dash import Dash, html

# Create a Dash application instance - consider this as the main 
# entry point of your Dash app.
app = Dash()

# Create the layout of the app using HTML components provided by Dash.
app.layout = html.Div(
    [
        # Define what coponents will be displayed on the webpage. 
        # In this case, we are displaying a simple heading.
        html.H1("Hello Dash")
    ])

if __name__ == "__main__":
    # setting debug=True will allow the app to automatically 
    # reload when you make changes to the code. 
    # This is useful during development.
    app.run(debug=True)
