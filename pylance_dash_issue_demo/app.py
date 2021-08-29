import dash
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

rows = [{'subsystem_name': 'name'}]

subsystem_records = [
    html.Tr(children=[
        html.Td(row['subsystem_name'])
    ]) for row in rows
]
lst = [
    html.Tr(children=[
        html.Th("Subsystem")
    ])
] + subsystem_records

app.layout = html.Div(children=lst)


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
