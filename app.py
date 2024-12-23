from dash import Dash, html
from Pages import test

app = Dash(__name__)
server = app.server

#app.layout = [html.Div(children='Hello JH')]
app.layout = [html.Div(children=test.message())]

if __name__ == '__main__':
    app.run_server(debug=True)