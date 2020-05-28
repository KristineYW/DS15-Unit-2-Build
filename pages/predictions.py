# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app

#Load pipeline
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Decision Predictor

            Select or enter the following inputs to find out which party will win. 

            Follow this [link](heroku.com) to find out what values to input for text fields. 

            """,
            className='mb-5'
        ),

        dcc.Markdown('#### [Petitioner (Party or Entity)](heroku.com)', className='mt-1'),
        dcc.Input(
            id='petitioner',
            placeholder=' Enter a value',
            type='text',
            value=''
            ), 
        
        dcc.Markdown('#### [Respondent (Party or Entity)](heroku.com)', className='mt-3'),
        dcc.Input(
            id='respondent',
            placeholder=' Enter a numeric value',
            type='text',
            value=''
            ), 
              
        dcc.Markdown('#### [Case Source](heroku.com)', className='mt-3'),
        dcc.Input(
            id='caseSource',
            placeholder=' Enter a numeric value',
            type='text',
            value=''
            ), 
        
        dcc.Markdown('#### [Case Origin](heroku.com)', className='mt-3'),
        dcc.Input(
            id='caseOrigin',
            placeholder=' Enter a numeric value',
            type='text',
            value=''
            ), 

        dcc.Markdown('#### Reason for Certiorari', className='mt-3'),
        dcc.Dropdown(
            id='certReason',
            options=[
            {'label': '1 - Case did not arise on cert or cert not granted', 'value': '1.0'},
            {'label': '2 - Federal court conflict', 'value': '2.0'},
            {'label': '3 - Federal court conflict and to resolve important or significant question', 'value': '3.0'},
            {'label': '4 - Putative conflict', 'value': '4.0'},
            {'label': '5 - Conflict between federal court and state court', 'value': '5.0'},
            {'label': '6 - State court conflict', 'value': '6.0'},
            {'label': '7 - Federal court confusion or uncertainty', 'value': '7.0'},
            {'label': '8 - State court confusion or uncertainty', 'value': '8.0'},
            {'label': '9 - Federal court and state court confusion or uncertainty', 'value': '9.0'},
            {'label': '10 - To resolve important or significant question', 'value': '10.0'},
            {'label': '11 - To resolve question presented', 'value': '11.0'},
            {'label': '12 - No reason given', 'value': '12.0'},
            {'label': '13 - Other reason', 'value': '13.0'},
            {'label': '12 - No reason given', 'value': 'nan'}
            ],
        value=''
        ),
    
        dcc.Markdown('#### Lower Court Disposition', className='mt-3'),
        dcc.Dropdown(
            id='lcDisposition',
            options=[
            {'label': '1 - Stay, petition, or motion granted', 'value': '1.0'},
            {'label': '2 - Affirmed', 'value': '2.0'},
            {'label': '3 - Reversed', 'value': '3.0'},
            {'label': '4 - Reversed and remanded', 'value': '4.0'},
            {'label': '5 - Vacated and remanded', 'value': '5.0'},
            {'label': '6 - Affirmed and reversed (or vacated) in part', 'value': '6.0'},
            {'label': '7 - Affirmed and reversed (or vacated) in part and remanded', 'value': '7.0'},
            {'label': '8 - Vacated', 'value': '8.0'},
            {'label': '9 - Petition denied or appeal dismissed', 'value': '9.0'},
            {'label': '10 - Modify', 'value': '10.0'},
            {'label': '11 - Remand', 'value': '11.0'},
            {'label': '12 - Unusual disposition', 'value': '12.0'},
            {'label': '13 - Unspecified', 'value': 'nan'}
            ],
        value=''
        ),
            
        dcc.Markdown('#### Issue Area', className='mt-3'),
        dcc.Dropdown(
            id='issueArea',
            options=[
            {'label': '1 - Criminal Procedure', 'value': '1.0'},
            {'label': '2 - Civil Rights', 'value': '2.0'},
            {'label': '3 - First Amendment', 'value': '3.0'},
            {'label': '4 - Due Process', 'value': '4.0'},
            {'label': '5 - Privacy', 'value': '5.0'},
            {'label': '6 - Attorneys', 'value': '6.0'},
            {'label': '7 - Unions', 'value': '7.0'},
            {'label': '8 - Economic Activity', 'value': '8.0'},
            {'label': '9 - Judicial Power', 'value': '9.0'},
            {'label': '10 - Federalism', 'value': '10.0'},
            {'label': '11 - Interstate Relations', 'value': '11.0'},
            {'label': '12 - Federal Taxation', 'value': '12.0'},
            {'label': '13 - Miscellaneous', 'value': '13.0'},
            {'label': '14 - Private Action', 'value': '14.0'},
            {'label': '13 - Miscellaneous', 'value': 'nan'}
            ],
        value=''
        ),
        dcc.Markdown("",id='out1'),

    dcc.Markdown('#### [Specific Issue](heroku.com)', className='mt-3'),
    dcc.Input(
        id='issue',
        placeholder=' Enter a numeric value',
        type='text',
        value=''
        ), 

    dcc.Markdown('#### Legal Provision', className='mt-3'),
    dcc.Dropdown(
        id='lawType',
        options=[
            {'label': '1 - Constitution', 'value': '1.0'},
            {'label': '2 - Constitutional Amendment', 'value': '2.0'},
            {'label': '3 - Federal statute', 'value': '3.0'},
            {'label': '4 - Court rules', 'value': '4.0'},
            {'label': '5 - Other', 'value': '5.0'},
            {'label': '6 - Infrequently litigated statutes', 'value': '6.0'},
            {'label': '8 - State or local law or regulation', 'value': '8.0'},
            {'label': '9 - No legal provision', 'value': '9.0'},
            {'label': '10 - Unspecified', 'value': 'nan'}
            ],
        value=''
        ),

    dcc.Markdown('#### [Specific Legal Provision](heroku.com)', className='mt-3'),
    dcc.Input(
        id='lawSupp',
        placeholder=' Enter a numeric value',
        type='float',
        value=''
        ), 

    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.H2('Predicted Prevailing Party', className='mb-3'),
        html.Div(id='prediction-content', className='lead'),

        daq.Gauge(
            id='my-daq-gauge',
            max=100,
            value=50,
            min=0
        ),

    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output(component_id='prediction-content', component_property='children'),
    [
        Input(component_id='petitioner', component_property='value'),
        Input(component_id='respondent', component_property='value'),
        Input(component_id='caseSource', component_property='value'),
        Input(component_id='caseOrigin', component_property='value'),
        Input(component_id='certReason', component_property='value'),
        Input(component_id='lcDisposition', component_property='value'),
        Input(component_id='issueArea', component_property='value'),
        Input(component_id='issue', component_property='value'),
        Input(component_id='lawType', component_property='value'),
        Input(component_id='lawSupp', component_property='value')
        
        ]
)
def update_output_div(petitioner, respondent, caseSource, caseOrigin, certReason, lcDisposition, issueArea, issue, lawType, lawSupp):
    return ' '.join([petitioner, respondent, caseSource, caseOrigin, certReason, lcDisposition, issueArea, issue, lawType, lawSupp])