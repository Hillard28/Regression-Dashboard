import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from sklearn.preprocessing import PolynomialFeatures
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def format_coefs(coefs):
    coef_string = "yhat = "

    for order, coef in enumerate(coefs):
        if coef >= 0:
            sign = ' + '
        else:
            sign = ' - '
        if order == 0:
            coef_string += f'{coef}'
        elif order == 1:
            coef_string += sign + f'{abs(coef):.3f}*x'
        else:
            coef_string += sign + f'{abs(coef):.3f}*x^{order}'

    return coef_string

# Create array of available variables
available_indicators = np.array([
    'quarters_since_vintage',
    'called_pct',
    'rvpi_pct',
    'dpi_pct',
    'net_multiple_x'],
    dtype = object
)

# Create array of available models
models = {
    'Regression': linear_model.LinearRegression,
    'Lasso': linear_model.Lasso,
    'Decision Tree': tree.DecisionTreeRegressor,
    'k-NN': neighbors.KNeighborsRegressor
}

available_asset_classes = df_fig['asset_class'].unique()
available_vintages = df_fig['vintage_inception_year'].sort_values().unique()

# Create graph object
app = dash.Dash(__name__)

# Set parameters for graph
app.layout = html.Div([
    html.Div([
        html.Div([
            # Creates dropdown to select x variable
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='quarters_since_vintage',
                searchable = False
            ),
            # Creates dropdown to select y variable
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='called_pct',
                searchable = False
            ),
            # Select asset class
            dcc.Dropdown(
                id='sector-name',
                options=[{'label': i, 'value': i} for i in available_asset_classes],
                value='Private Equity',
                searchable = False
            ),
            # Select vintage year
            dcc.Dropdown(
                id='vintage-year',
                options=[{'label': i, 'value': i} for i in available_vintages],
                value=2015,
                searchable = False
            ),
            # Select model type
            dcc.Dropdown(
                id='model-name',
                options=[{'label': x, 'value': x} 
                         for x in models],
                value='Regression',
                searchable=False
            ),
            # Select polynomial degree
            dcc.Slider(
                id='polynomial-degree-slider',
                min=1,
                max=10,
                step=1,
                value=1,
                marks = {i: str(i) for i in range(1,11)}
            ),
            # Set alpha for lasso regression
            dcc.Slider(
                id='alpha-slider',
                min=-4,
                max=3,
                value=0,
                marks = {i: '{}'.format(10**i) for i in range(-4,4)}
            )
        ])
    ]),
    # Create graph object
    dcc.Graph(id='graph')
])

# Set inputs and outputs
@app.callback(
    Output('graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('sector-name', 'value'),
    Input('vintage-year', 'value'),
    Input('model-name', 'value'),
    Input('polynomial-degree-slider', 'value'),
    Input('alpha-slider', 'value')
)

# Generate dash plot
def update_graph(xaxis_column_name,
                 yaxis_column_name,
                 sector,
                 vintage,
                 name,
                 degree,
                 alpha
                 ):
    # Load x and y datasets
    x = df_fig.loc[(df_fig['asset_class'] == sector)
                   & (df_fig['vintage_inception_year'] == vintage),
                   xaxis_column_name].to_numpy().reshape(-1,1)
    y = df_fig.loc[(df_fig['asset_class'] == sector)
                   & (df_fig['vintage_inception_year'] == vintage),
                   yaxis_column_name]
    # Show empty plot if dataset empty or too small
    if len(x) < 2 or len(y) < 2:
        fig = go.Figure()
    else:
        # Generate training dataset
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            random_state = 30
        )
        # Set range for predicting y
        x_range = np.linspace(x.min(), x.max(), 300)
        
        # Generate poly dataset (only relevant if poly > 1)
        poly = PolynomialFeatures(degree = degree)
        x_train_poly = poly.fit_transform(x_train)
        x_test_poly = poly.fit_transform(x_test)
        x_range_poly = poly.fit_transform(x_range.reshape(-1,1))
        
        # Sets parameters for linear regressions
        if name == 'Regression':
            model = models[name](normalize = True)
        elif name == 'Lasso':
            model = models[name](alpha = 10**alpha, normalize = True)
        else:
            model = models[name]()
        
        # Fit model
        model.fit(x_train_poly, y_train)
        
        # Predict y using model
        y_range = model.predict(x_range_poly)
        
        # Generate scatter of training and testing data
        trace0 = go.Scatter(x=x_train.squeeze(), y=y_train, 
                       name='train', mode='markers')
        trace1 = go.Scatter(x=x_test.squeeze(), y=y_test, 
                       name='test', mode='markers')
        
        # Add coefficients on hover if linear regression is used
        if name == 'Regression' or name == 'Lasso':
            trace2 = go.Scatter(x=x_range, y=y_range, 
                                name='prediction', mode = 'lines',
                                hovertext = format_coefs(model.coef_))
        else:
            trace2 = go.Scatter(x=x_range, y=y_range, 
                                name='prediction', mode = 'lines')
        # Combine traces
        data = [trace0, trace1, trace2]
        
        # Add score in title
        layout = go.Layout(title = f'Score: {model.score(x_test_poly, y_test):.5f}',
                           hovermode = 'closest')

    return go.Figure(data = data, layout = layout)

# Run debug server
if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)












