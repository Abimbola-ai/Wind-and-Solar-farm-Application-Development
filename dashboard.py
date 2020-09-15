import dash
import dash_table
import numpy
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from automate import final_merged_data
#from sms import send_message
from subprocess import call
from dash.exceptions import PreventUpdate
#final_merged_data.to_dict()
from twilio.rest import Client
from datetime import datetime

final_merged_data['Total MW'] = final_merged_data['Power_Solar'] + final_merged_data['Power_Wind']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

Wind_Output = final_merged_data['Power_Wind'].values
Solar_Output = final_merged_data['Power_Solar']
Total_Output = final_merged_data['Total MW']
branches = final_merged_data['Day']

trace1 = go.Bar(x=branches,y = Wind_Output, name = 'Wind')
trace2 = go.Bar(x=branches,y = Solar_Output, name = 'Solar')
trace3 = go.Bar(x=branches,y = Total_Output, name = 'Wind and Solar')

data = [trace1, trace2]
layout = go.Layout(barmode = 'group',xaxis_title="Day of the month", yaxis_title="Power Generated in MW")
fig = go.Figure(data = data, layout = layout)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello George',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Predicted output from your wind and solar plants', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=go.Figure(data=[trace3], layout=go.Layout(xaxis_title="Day of the month", yaxis_title="Total Power Generated in MW"))),

    html.Button('Send SMS', 
            id='button1',
            style={'display':'block', 'padding':'5', 'background-color':'#aabbcc'}),
            html.Div(id='output-container-button',
                            children='Hit the button to send sms.'),           
        html.Label('…', 
            id='label1', 
            style={'display':'inline-block', 'margin':'10'} )
])

#@app.callback(
#dash.dependencies.Output('output-container-button', 'children'),
#[dash.dependencies.Input('button1', 'n_clicks')])
#def run_script_onClick(n_clicks):
    # Don't run unless the button has been pressed...
    #if not n_clicks:
        #raise PreventUpdate

    #script_path = '~/Documents/AIIP/AppDev/Summative/sms.py'
    # The output of a script is always done through a file dump.
    # Let's just say this call dumps some data into an `output_file`
    #call(["python3", script_path])

    # Load your output file with "some code"
    #output_content = send_message('output.csv')
    # Now return.
    #script_fn = 'sms.py'
    #exec(open(script_fn).read())
    #return output_content

if __name__ == '__main__':
    app.run_server(debug=True)