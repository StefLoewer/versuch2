import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np


'''
erfolgsfaktoren=pd.read_csv('/Users/stefanieloewer/PythonTraining/MeinErsterDashCode/erfolgsfaktoren.csv')

erfolgsfaktoren=erfolgsfaktoren.sort_values('Standardized Beta N1=310 Validation')
'''

successfactors=['Team atmosphere',
                'User involvement',
                'Strength of projectleader',
                'Availability of team',
                'Sales activities',
                'Creative contribution of team',
                'Distance of team',
                'Milestones' ]

complex_domains=[0.307, 0.265, 0.205, 0.182, 0.202, 0.061, 0.109, 0.1]
other_domains=[0.362, 0.275, 0.182, 0.194, 0.148, 0.184, 0.145, 0.069]
all_summe=[0.342, 0.265, 0.196, 0.194, 0.17, 0.118, 0.117, 0.081]

trace2 = go.Bar(
    y=successfactors,
    x=complex_domains,
    name='Complex domains (N1=310)',
    marker=dict(color='rgb(0, 154, 218)'),
    orientation = 'h'
)
trace1 = go.Bar(
    y=successfactors,
    x=other_domains,
    name='Other domains (N2=311)',
    marker=dict(color='rgb(192,192,192)'),
    orientation = 'h'
)

trace3 = go.Scatter(
    y=successfactors,
    x=all_summe,
    mode='lines+markers',
    line=dict(color='rgb(128, 0, 128)'),
    name='Success factors over all evaluated projects',
    orientation = 'h'
)

success_data = [trace1, trace2, trace3]

success_layout = go.Layout(
    title = 'Success factors of software development', # Graph title
    yaxis = dict(showticklabels=True,
                title = '',
                 titlefont = dict(
                    family='Arial, sans-serif',
                    size=12,
                    color='rgb(0, 0, 0)'
            )),

    xaxis = dict(title = 'Standardized Beta coefficients',
                 titlefont = dict(
                    family='Arial, sans-serif',
                    size=12,
                    color='rgb(0, 0, 0)'
            ))
)

success_fig = go.Figure(data=success_data, layout=success_layout)


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('SWsuccessfactor'),
    dcc.Graph(
        id='LoewerProject',
        figure=success_fig
    )])

if __name__ == '__main__':
    app.run_server()
