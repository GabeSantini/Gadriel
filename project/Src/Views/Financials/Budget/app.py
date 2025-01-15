# Dash app entry point
import dash
import dash_core_components as dcc
import dash_html_components as html
from components import layout, callbacks

app = dash.Dash(__name__)
app.layout = layout.create_layout()
callbacks.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)