from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = [html.Div(children='Hello JH')]

if __name__ == '__main__':
    app.run_server(debug=True)
