# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Imports from this application
from app import app


court = ['C1301','C1303','C1401','C1402','C1403',
         'C1404','C1405','C1406','C1407','C1408',
         'C1409','C1410','C1411','C1501','C1502',
         'C1503','C1504','C1505','C1506','C1507',
         'C1601','C1602','C1603','C1604','C1605',
         'C1606','C1607','C1701','C1702','C1703',
         'C1704','C1705','C1706','C1707']

fig = go.Figure()
fig.add_trace(go.Bar(x=court,
                y=[3537,2466,576,360,1323,
                  322,2138,3546,634,4696,
                  2502,2988,424,624,1269,
                  154,4158,40,5723,4806,
                  1260,88,2709,647,1387,
                  459,5603,153,1376,513,
                  2259,464,567,342],
                name='Liberal',
                marker_color='rgb(0,0,255)'
                ))
fig.add_trace(go.Bar(x=court,
                y=[2817,3752,729,168,657,
                   258,1258,2601,152,1557,
                   1539,1476,144,623,1179,
                   140,4671,72,7506,6381,
                   1278,192,2853,756,1742,
                   756,6626,135,1914,531,
                   2250,336,693,351],
                name='Conservative',
                marker_color='rgb(255,0,0)'
                ))

fig.update_layout(
    title='Total Liberal/Conservative Votes by Natural Court',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgb(255, 255, 255, 0)',
        bordercolor='rgb(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.1, 
    bargroupgap=0.2
)

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights


            #### Introduction
            In the US, there is no higher court of authority than the Supreme Court. It has the power to overturn decades of precedence, its jurisdiction covering the over 330 million people of the US (and beyond, i.e. with regard to immigration and refugee policies). Just 9 Justices wield this power at any given moment; as such, it is vitally important to understand what factors could impact the decisions of the Court.

            #### Political Leanings of the Justices
            It should come as no surprise that each Justice has his or her own political philosophy. Policy preferences may even evolve to become more extreme over time. With so much at stake, it would be remiss to disregard the potential influence that personal ideologies could have on individual voting patterns. Though most Justices choose to privatize their voting records on political issues, a closer look at the way Justices have voted in Court cases over the past several decades reveals that some Justices do indeed vote substantially more conservatively or more liberally than others. 

            """),
        
        html.Img(
            src='assets/votes.png', className='img-fluid'
            ),
        
        dcc.Markdown(
            """
            The dataset I used did not contain any information on the Justices’ political party affiliation, so I introduced three new features to examine whether a Justice’s voting direction (liberal or conservative) may be influenced by: 
                1) the political party of the President in power, 
                2) the majority party controlling the Senate, or 
                3) the political party of each Justice’s appointing President.

            Individual voting patterns aside, thankfully the associations were paltry when viewed from a holistic perspective. This indicates that as long as the Court remains relatively balanced in terms of liberal vs conservative inclinations, the cumulative votes for the cases should not be swayed one way or another by the Justices’ political leanings. 
        
        dcc.Graph(figure=fig), 
        
        dcc.Markdown(
            #### Transition to New Target 
            So what factors are the most important in a case that reaches the Court? What determines if it is the petitioner or the respondent that succeeds in swaying the Justices in their favor? In order to investigate this question, I changed the target of my predictive modeling from the political direction of each Justice’s vote to how the Court votes overall, namely whether the petitioner or the respondent would be the prevailing party on any given case presented to the Court. 

            The majority baseline (before any modeling is applied) reveals that the petitioning party wins in about 62% of all Supreme Court cases. In order to determine which features would be most relevant in creating a predictive model that beats the probabilities of guessing with a 62% accuracy rate, I used a chart for permutation importance and chose the top 10 most relevant features to create the model on. From the chart, I used only the features that were not bound to the outcome (in order to avoid data leakage) or a specific year or cohort of Justices (which may not apply to future predictions once old Justices are replace by new ones--another way of preventing an overfit model). 

            #### Analysis

            Three different types of classification models were applied to the data sets. All evaluation metrics used beat the baseline, some more drastically than others (RandomForestClassifier and XGBoost models reported accuracy scores over 90% while an AUC model yielded a test accuracy of only 80%). These findings indicate that with just a few pieces of information, the Supreme Court decision, whether in favor of the petitioner or respondent, is predictable. 

            """),
        
        html.Img(
            src='assets/con_mat.png', className='mb-3'),
        
        dcc.Markdown(
            """
            Further investigation into specific variables reveal that even within the top 10 features, certain features may be exponentially more important for predictive models than others. 
            For instance, taken individually, the variables may have different levels of impact on which party wins before the Supreme Court.
            """),
        
        html.Img(
            src='assets/pdp.png', className='mb-3'),
        
        dcc.Markdown(
            """
            We can even take a look at how the variables interact in determining the predictive power of the models. 
            """),
        
        html.Img(
            src='assets/interact.png', className='mb-3'),
        
        dcc.Markdown(
            """

            #### Conclusions and Caveats
            Since our model assumes a generally balanced Court, its predictive power may be limited when applied to a heavily skewed Court with an overwhelming majority of Justices that may lean toward one political ideology or another. 
            Individual records show that the Justices have varying proclivities to voting in accordance with their political ideologies, so a Court with even 7 liberal or 7 conservative Justices can dramatically change the lives of hundreds of millions of people.  

            """
        ),

    ],
)

layout = dbc.Row([column1])
