import webbrowser
from threading import Timer
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, callback

# This will default to a flask server
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP], #This will give better styling options - try different dbc.themes.* 
    title="Demo App", # Just a tab title
)

app.layout = dbc.Container(
    [
        # Use this and other variations of html.H<x> to display text of different sizes
        html.H1("This is the header"),
        
        # Use this to create a group of input elements to be displayed together
        dbc.InputGroup(
            [
                dbc.InputGroupText("1st Number"), # Just a label
                dbc.Input(id='num-1', value=0), # Actual text input field - 'id' will be used to create actions/callbacks
                dbc.InputGroupText("2nd Number"),
                dbc.Input(id='num-2', value=0),
                dbc.Button('Add', id='add-button') # Button used to perform an action - 'Add' is the label
            ]
        ),
        dbc.Label('The text below this should change when new numbers are added and the button is clicked.'),
        html.Br(), # this creates the equivalent of a line break on the page
        html.Span(id='result-label')
    ]
)

@callback(
    Output("result-label", "children"),
    Input('add-button', 'n_clicks'),
    [
        State("num-1", "value"),
        State("num-2", "value"),
    ]
)
def add_inputs(n, num1, num2):
    if n is None:
        return 'Do math!'
    else:
        result = float(num1) + float(num2)
        return '%.6f' % result
    
def run():
    host = "localhost" # says to run this on your machine
    port = 8080 # says to use this specific port on your machine
    url = f"http://{host}:{port}" # the full url where your page can be viewed
    Timer(10, webbrowser.open_new(url)) # open a new browser tab pointed at your url

    # run app
    app.run(host=host, port=port, debug=False) # if you see problems change 'False' to 'True' and send me the output

# this prevents the app from running unintentionally (if you import something from this script but don't want to run)
if __name__ == "__main__":
    run()