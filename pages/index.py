# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(

            """
        
            ## How does the Court decide?


            In the US, there is no higher court of authority than the Supreme Court. It has the power to overturn decades of precedence, its jurisdiction covering the over 330 million people of the US (and beyond, i.e. with regard to immigration and refugee policies). 
            
            Just 9 Justices wield this power at any given time. As such, it is vitally important to understand what factors could impact the ruling of the Court.
            

            """
        ),
        dcc.Link(dbc.Button("Predict a Case", color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])