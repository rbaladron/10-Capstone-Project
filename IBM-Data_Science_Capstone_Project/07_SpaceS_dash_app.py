"""
SpaceX Launch Records Dashboard

This Python script creates a Dash application that displays interactive visualizations of SpaceX launch data. 
Users can explore launch success rates by launch site and analyze the correlation between payload mass and launch success.

Data Source: spacex_launch_dash.csv 

"""

# Import required libraries
import pandas as pd
import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("data/spacex_launch_dash.csv")
max_payload = int(spacex_df['Payload Mass (kg)'].max())
min_payload = int(spacex_df['Payload Mass (kg)'].min())

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(
    style={'display': 'flex', 'justify-content': 'center', 'backgroundColor': '#f4f4f4', 'padding': '20px'},
    children=[
        html.Div(
            style={'maxWidth': '1000px', 'width': '100%', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'},
            children=[
                html.H1(
                    'SpaceX Launch Records Dashboard', 
                    style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
                ),
                # TASK 1: Add a dropdown list to enable Launch Site selection
                # The default select value is for ALL sites
                dcc.Dropdown(
                    id='site-dropdown',
                    options=[
                        {'label': 'All Sites', 'value': 'ALL'},
                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                        {'label': 'CCAFS SLC-40', 'value':'CCAFS SLC-40'},
                    ],
                    value='ALL',
                    placeholder="Select a Launch Site here",
                    searchable=True,
                    style={'marginBottom': '20px'}
                ),
                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                html.Div(
                    style={'display': 'flex', 'justify-content': 'center'},
                    children=[
                        dcc.Graph(id='success-pie-chart', style={'width': '90%'})
                    ]
                ),

                html.P("Payload range (Kg):" , style={'textAlign': 'center'}),

                # TASK 3: Add a slider to select payload range
                dcc.RangeSlider(
                    id='payload-slider',
                    min=0,
                    max=10000,
                    step=1000,
                    value=[min_payload ,max_payload],
                    marks={i: f'{i} Kg' for i in range(min_payload, max_payload + 1000, 2000)}
                ),

                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                html.Div(
                    style={'display': 'flex', 'justify-content': 'center'},
                    children=[
                        dcc.Graph(id='success-payload-scatter-chart', style={'width': '90%'})
                    ]
                ),
            ]
        )        
    ]
)    

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    """
    Generates a pie chart that displays the total number of successful launches for each launch site 
    or the success and failure counts for a specific site based on user selection.

    Args:
        entered_site (str): The selected launch site from the dropdown menu ('ALL' for all sites).

    Returns:
        plotly.express.Figure: The pie chart figure to be displayed in the dashboard.
    """
    # if ALL sites are selected
    filtered_df = spacex_df[spacex_df['class'] == 1]
    if entered_site == 'ALL':
        fig = px.pie(
            filtered_df, 
            names='Launch Site',
            title='Total Success Launches by Site',
        )
    else:
        # Filter the datea for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]

        #Create the pie chart sowhing success and failure counts
        fig = px.pie(
            filtered_df,
            names='class',
            title=f'Total Launches from site {entered_site}',
        )
    # Return the figure to update the pie chart componenent in the dashboard
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def update_scatter_chart(selected_site, payload_range):
    """
    Generates a scatter chart that shows the correlation between payload mass and launch success.

    Args:
        selected_site (str): The selected launch site from the dropdown menu ('ALL' for all sites).
        payload_range (tuple): A tuple containing the lower and upper payload mass limits selected by the user.

    Returns:
        plotly.express.Figure: The scatter chart figure to be displayed in the dashboard.
    """
    # Unpack the payload range
    low, high = payload_range
    
    # Filter data based on payload range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]

    # Check if a specific site is selected
    if selected_site == 'ALL':
        # Use all sites data
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between PayLoad an success for All Sites',
            labels={'class': 'class', 'Payload Mass (kg)': 'Payload Mass (kg)'},
            hover_data=['Launch Site']
        )
    else:
        # Filter the dataframe for the selected site
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        # Create scatter plot with payload on x-axis, mission outcome on y-axis, and booster version as color
        fig = px.scatter  (
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation between PayLoad an success for Site {selected_site}',
            labels={'class': 'Mission Outcome', 'Payload Mass (kg)': 'Payload Mass (kg)'},
            hover_data=['Launch Site']
        )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
