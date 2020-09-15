
import dash
import dash_core_components as dcc #This library will give us the dashboard elements (pie charts, scatter plots, bar graphs etc)
import dash_html_components as html #This library allows us to arrange the elements from dcc in a page as is done using html/css 

#Fancy Styles and fonts provided to us by nice people
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May'] #Will form our x-axis later
total_prod = [125,134,140,136,113]
p1_prod = [21,22,27,29,20]
p2_prod = [10,19,24,22,16]	#production of p2 as a list
p3_prod = [56,50,47,12,41]
p4_prod = [30,31,25,60,27]
p5_prod = [8,12,17,13,9] #production of p5 as a list

# This structure represents the bar graph
# id: The html id of the bar graph
# figure: info that actually goes into the bar graph. It is a python dictionary
# data: The data for the x and y axis. The type of the graph and the name of the graph. Different types and names documented by plotly (https://plot.ly/python/bar-charts/) or (https://plot.ly/python/)
# layout: A dict containing various attributes. The full list of possibilities lives in dcc code(https://github.com/plotly/plotly.py/blob/master/plotly/graph_objs/layout/__init__.py) <If you actually make it here, search the document for the word "setter" and should see other properties that you can set as font, color, gridcolor, gridwidth etc>
bar = dcc.Graph(
        id='barChart-p1-p5',
        figure={
            'data': [
                {'x': months, 'y': total_prod, 'type': 'bar', 'name': 'prod_bar'},
                    ],
            'layout': {
                'title': 'Total production Jan-May '
            }
        }
    )
pie = dcc.Graph(
        id='pieChart-p1-p5',
        figure={
            'data': [
                {'labels': ['p1', 'p2', 'p3', 'p4','p5'], 'values': [sum(p1_prod),sum(p2_prod),sum(p3_prod),sum(p4_prod),sum(p5_prod)], 'type': 'pie', 'name': 'prod_pie'},
                    ],
            'layout': {
                'title': 'Total Jan-May production'
            }
        }
    )
#This structure draws the layout of the dashboard page itself. An HTML page is drawn as a series of boxes. If box C is inside box P, box C is said to be a child of the box P. The overall "box" is called an html.div

#In this case, the structure is:
	# *html.h1
	# *html.Div
	# *bar2
# In future labs, you shall see boxes inside boxes. To draw the layout of the page, it is important which elements are children of which other elements
app.layout = html.Div(children=[
    html.H1(children='ALU AIIP'),

    html.Div(children='''
        ACME inc's web dashboard. Built using Dash: A web application framework for Python.
    '''),bar,
    pie
])
if __name__ == '__main__':
    app.run_server(debug=True)