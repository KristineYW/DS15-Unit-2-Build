# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

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
            """),
        
        html.Img(
            src='assets/eli.png', className='mb-3'),
        
        dcc.Markdown(
            """
            #### Transition to New Target 
            So what factors are the most important in a case that reaches the Court? What determines if it is the petitioner or the respondent that succeeds in swaying the Justices in their favor? In order to investigate this question, I changed the target of my predictive modeling from the political direction of each Justice’s vote to how the Court votes overall, namely whether the petitioner or the respondent would be the prevailing party on any given case presented to the Court. 

            The majority baseline (before any modeling is applied) reveals that the petitioning party wins in about 62% of all Supreme Court cases. In order to determine which features would be most relevant in creating a predictive model that beats the probabilities of guessing with a 62% accuracy rate, I used a chart for permutation importance and chose the top 10 most relevant features to create the model on. From the chart, I used only the features that were not bound to the outcome (in order to avoid data leakage) or a specific year or cohort of Justices (which may not apply to future predictions once old Justices are replace by new ones--another way of preventing an overfit model). 

            #### Analysis

            Three different types of models were applied to the data sets. All evaluation metrics used beat the baseline, some more drastically than others (RandomForestClassifier and XGBoost models reported accuracy scores over 90% while an AUC model yielded a test accuracy of only 80%). These findings indicate that with just a few pieces of information, the Supreme Court decision, whether in favor of the petitioner or respondent, is predictable. 

            Further investigation into specific variables reveal that even within the top 10 features, certain features may be exponentially more important for predictive models than others. 

            #### Conclusions and Caveats
            Since our model assumes a generally balanced Court, its predictive power may be limited when applied to a heavily skewed Court with an overwhelming majority of Justices that may lean toward one political ideology or another. 
            Individual records show that the Justices have varying proclivities to voting in accordance with their political ideologies, so a Court with even 7 liberal or 7 conservative Justices can dramatically change the lives of hundreds of millions of people.  

            """
        ),

    ],
)

layout = dbc.Row([column1])