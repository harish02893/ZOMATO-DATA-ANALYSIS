# Import necessary modules
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly as plt
import base64

import numpy as np

# Read the files
data = pd.read_csv("zomato.csv")

# Function to encode image to base64
def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f'data:image/png;base64,{encoded_string}'

# Build the Components



# Update Home_content to include the additional content
Home_content = html.Div([
    html.Div([
        html.H1("Zomato Data Analysis Dashboard", style={'textAlign': 'center', 'color': 'navy', 'marginBottom': '30px', 'fontFamily': 'Arial, sans-serif'}),
        html.Div([
            html.H2("Welcome to the Zomato Data Analysis Dashboard!", style={'color': 'darkblue', 'marginBottom': '20px'}),
            html.P("Explore insights into customer preferences, industry trends, and more using data from Zomato.", style={'fontSize': '1.1em'}),
        ], style={'padding': '20px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'backgroundColor': '#f9f9f9', 'marginBottom': '30px'}),
        html.Div([
            html.H2("Features", style={'color': 'darkblue', 'marginBottom': '20px'}),
            html.Ul([
                html.Li("Data Engineering", style={'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Currency Comparison: Compare the currency of India (INR) with other countries.")
                ]),
                html.Li("Dashboard Development", style={'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Country-Specific Data: Explore specific data by selecting a country."),
                    html.Li("Top 10 Costly Cuisines in India: Discover the most expensive cuisines in India."),
                    html.Li("Online Delivery vs Dine-in: Visualize the proportion of online delivery orders versus dine-in options.")
                ]),
                html.Li("Dashboard Deployment", style={'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Hosted Dashboard: Deploy the dashboard on a web app server for easy access.")
                ]),
                html.Li("Project Evaluation Metrics", style={'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Modular Code: Organized into functional blocks for maintainability."),
                    html.Li("PEP8 Standards: Follows Python coding standards for readability."),
                    html.Li("GitHub Repository: Access the codebase and project documentation on GitHub."),
                    html.Li("Demo Video: Watch a demo video showcasing the working model on LinkedIn.")
                ])
            ])
        ], style={'padding': '20px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'backgroundColor': '#f9f9f9'}),
        html.Div([
            html.H2("Contact Details", style={'color': 'darkblue', 'marginBottom': '20px'}),
            html.Table([
                html.Tr([
                    html.Td("Name", style={'font-weight': 'bold'}),
                    html.Td("KESAVAN S")
                ]),
                html.Tr([
                    html.Td("Batch Code", style={'font-weight': 'bold'}),
                    html.Td("DT1819")
                ]),
                html.Tr([
                    html.Td("GitHub Link", style={'font-weight': 'bold'}),
                    html.Td(html.A("GitHub", href="https://github.com/harish02893", style={'color': 'blue', 'text-decoration': 'none', 'font-weight': 'bold'}))
                ]),
                html.Tr([
                    html.Td("LinkedIn Link", style={'font-weight': 'bold'}),
                    html.Td(html.A("LinkedIn", href="https://www.linkedin.com/in/kesavan-sekar-2aaa3325b/", style={'color': 'blue', 'text-decoration': 'none', 'font-weight': 'bold'}))
                ])
            ], style={'border-collapse': 'collapse', 'width': '100%', 'margin': 'auto'}),
        ], style={'padding': '20px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'backgroundColor': '#f9f9f9', 'marginBottom': '30px'})
    ], style={'maxWidth': '800px', 'margin': 'auto', 'background': 'linear-gradient(to right, #c9e6ff, #e2f3ff)', 'padding': '20px', 'borderRadius': '10px'})
], style={'background': '#f0f2f5', 'minHeight': '100vh', 'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'fontFamily': 'Arial, sans-serif', 'backgroundImage': 'url("https://miro.medium.com/max/1200/1*j2ATMp7LI9ZcDICPW93PHA.jpeg")'})

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
##EXPLORED ANALYSIS

Explored_component=html.H3("ZOMATO DATA ANALYSIS", style={'color': 'dark blue', 'textAlign': 'center'})

total_count = len(data['Restaurant Name'].unique())

total_count_component = dbc.Card(
    dbc.CardBody([
        html.P("Total Restaurants", className="card-text"),
        html.H2(f"{total_count}", className="card-title")
        ]),
    className="mb-3",
)
total_count1 = len(data['Cuisines'].unique())

total_count_component1 = dbc.Card(
    dbc.CardBody([
        html.P("Total Cuisines", className="card-text"),
        html.H2(f"{total_count1}", className="card-title")
        ]),
    className="mb-3",
)

total_count2 = len(data['Country'].unique())

total_count_component2 = dbc.Card(
    dbc.CardBody([
        html.P("Total Country", className="card-text"),
        html.H2(f"{total_count2}", className="card-title")
        ]),
    className="mb-3",
)

total_count3 = len(data['City'].unique())

total_count_component3 = dbc.Card(
    dbc.CardBody([
        html.P("Total City", className="card-text"),
        html.H2(f"{total_count3}", className="card-title")
        ]),
    className="mb-3",
)
##------------------------------------------------------------------------------------------------------------------------------------------------------##
country_dropdown = dcc.Dropdown(
    id='country-dropdown',
    options=[{'label': country, 'value': country} for country in data['Country'].unique()],
    value='India',  # Default value
    style={'width': '50%', 'margin': '10px'}
)

city_dropdown = dcc.Dropdown(
    id='city-dropdown',
    options=[],  # Options will be populated based on the selected country
    value='',  # Default value
    style={'width': '50%', 'margin': '10px'}
)
# Define the layout of the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server=app.server

app.layout = html.Div([
    # Dropdown menu to select different sections
    dcc.Dropdown( 

        id='section-dropdown',
        options=[
            {'label': 'Home', 'value': 'home'},
            {'label': 'Explore Data', 'value': 'explore'},
            {'label': 'Top Analysis', 'value': 'top_analysis'}
        ],
        value='home',
        style={'width': '50%', 'margin': '10px'}
    ),

    # Display the corresponding content based on the selected section
    html.Div(id='section-content'),

])

# Callback to update city dropdown options based on the selected country
@app.callback(
    Output('city-dropdown', 'options'),
    [Input('country-dropdown', 'value')]
)
def update_city_options(selected_country):
    if selected_country:
        cities = data[data['Country'] == selected_country]['City'].unique()
        return [{'label': city, 'value': city} for city in cities]
    else:
        return []

# Callback to update visualizations based on the selected country and city
# Callback to update visualizations based on the selected country and city
@app.callback(
    [Output('visualization-1', 'figure'),
     Output('visualization-4', 'figure')],
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_visualizations(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[data['City'] == selected_city]

    # Update figures based on filtered data
    fig1 = update_figure_1(filtered_data)
    fig4 = update_figure_4(filtered_data)

    return fig1, fig4

#component 1
def update_figure_1(filtered_data):
    top_10_costly_cuisines_data = filtered_data.groupby('Cuisines')['Average Cost for two'].mean().nlargest(10)
    fig = go.Figure(go.Bar(
        x=top_10_costly_cuisines_data.values,
        y=top_10_costly_cuisines_data.index,
        orientation='h'
    ))
    fig.update_layout(
        title='Top 10 Costly Cuisines',
        xaxis_title='Average Cost',
        yaxis_title='Cuisine'
    )
    return fig
#Component 2

# Count the values in the 'Has Online delivery' column
values = data['Has Online delivery'].value_counts()
labels = ['Yes', 'No']
colors = ['#1f77b4', '#ff7f0e']  # Define colors for the pie chart

# Create a pie chart using Plotly Graph Objects
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, textinfo='percent+label', marker=dict(colors=colors))])
fig2.update_layout(title='Online Delivery Acceptance', showlegend=False)

#Component 3

# Count the values in the 'Has Table booking' column
values = data['Has Table booking'].value_counts()
label = ['Yes', 'No']
colors = ['#1f77b4', '#ff7f0e']

## Create a pie chart using Plotly Graph Objects
fig3 = go.Figure(data=[go.Pie(labels=label, values=values, hole=0.3, textinfo='percent+label')])
fig3.update_layout(title='Table Booking Acceptance', showlegend=False)

#Component 4-- Average Cost and Price Range by Country

# Define function to generate figure 4 based on filtered data
# Component 4
# Define function to generate figure 4 based on filtered data
# Define function to generate figure 4 based on filtered data
def update_figure_4(filtered_data):
    fig = px.box(filtered_data, x='Country', y='Average Cost for two',
                 color='Price range', title='Average Cost and Price Range by Country',
                 labels={'x': 'Country', 'y': 'Average Cost for two', 'color': 'Price Range'})
    return fig

#component 5

# Plotting a sunburst chart
fig5= px.sunburst(data, path=['Country', 'City', 'Cuisines'], values='Aggregate rating', \
                  color='Country', color_continuous_scale=px.colors.sequential.Viridis,\
                  title = 'Click me! Sunburst Chart of Zomato Data - Country > City > Cuisines')

#component 8
dfCurrencyModified = data.copy(deep=True)

dfCurrencyModified['Average Cost for two'] = np.where(dfCurrencyModified['Currency'] == 'Indonesian Rupiah(IDR)',
                                           dfCurrencyModified['Average Cost for two'] * 0.0051,
                                           dfCurrencyModified['Average Cost for two'])
fig8= px.scatter(dfCurrencyModified, x="Votes", y="Average Cost for two", color="Rating text",
                 size="Price range", hover_data=['Restaurant Name', 'Currency'])

# Component 6
# Explore the distribution of currencies using a bar chart
currency_counts = data['Currency'].value_counts()
fig6= px.bar(currency_counts, x=currency_counts.index, y=currency_counts.values,
                                   title='Distribution of Currencies',
                                   labels={'index': 'Currency', 'y': 'Count'})

#component 7
# Assuming 'merged_data' is your DataFrame
# Assuming 'country_restaurant_count' is the DataFrame with restaurant counts per country
# Assuming 'merged_data' is your DataFrame
country_restaurant_count = data['Country'].value_counts().reset_index()
country_restaurant_count.columns = ['Country', 'Restaurant Count']
# Calculate average cost and rating text for each country
country_avg_cost_rating = data.groupby('Country').agg({'Average Cost for two': 'mean', 'Aggregate rating': 'mean'})
country_avg_cost_rating['Rating Text'] = country_avg_cost_rating['Aggregate rating'].apply(lambda x: 'High' if x >= 4 else ('Medium' if x >= 3 else 'Low'))

# Join country restaurant count with average cost and rating text
country_data = country_restaurant_count.merge(country_avg_cost_rating, left_on='Country', right_index=True)

# Get the top cuisines by country
top_cuisines_by_country = data.groupby('Country')['Cuisines'].apply(lambda x: x.value_counts().index[0])

# Join top cuisines with country data
country_data['Top Cuisine'] = country_data['Country'].map(top_cuisines_by_country)

# Calculate average cost and rating text for each city
city_avg_cost_rating = data.groupby('City').agg({'Average Cost for two': 'mean', 'Aggregate rating': 'mean'})
city_avg_cost_rating['Rating Text'] = city_avg_cost_rating['Aggregate rating'].apply(lambda x: 'High' if x >= 4 else ('Medium' if x >= 3 else 'Low'))

# Join city restaurant count with average cost and rating text
city_data = data['City'].value_counts().reset_index()
city_data.columns = ['City', 'Restaurant Count']
city_data = city_data.merge(city_avg_cost_rating, left_on='City', right_index=True)

# Load the world map data
world_geojson = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'  # Replace with the path to your GeoJSON file

# Create custom hover text for country data
country_hover_text = country_data.apply(lambda row: f"Country: {row['Country']}<br>"
                                                    f"Restaurant Count: {row['Restaurant Count']}<br>"
                                                    f"Average Cost: {row['Average Cost for two']:.2f}<br>"
                                                    f"Aggregate Rating: {row['Aggregate rating']:.2f}<br>"
                                                    f"Rating Text: {row['Rating Text']}<br>"
                                                    f"Top Cuisine: {row['Top Cuisine']}",
                                        axis=1)

# Create custom hover text for city data
city_hover_text = city_data.apply(lambda row: f"City: {row['City']}<br>"
                                              f"Restaurant Count: {row['Restaurant Count']}<br>"
                                              f"Average Cost: {row['Average Cost for two']:.2f}<br>"
                                              f"Aggregate Rating: {row['Aggregate rating']:.2f}<br>"
                                              f"Rating Text: {row['Rating Text']}",
                                  axis=1)

# Create the choropleth map for countries
fig_country = px.choropleth(country_data, 
                            geojson=world_geojson,
                            locations='Country', 
                            featureidkey='properties.name',
                            color='Restaurant Count',
                            hover_name='Country',
                            hover_data={'Country': False, 'Restaurant Count': True, 
                                        'Average Cost for two': True, 'Aggregate rating': True, 
                                        'Rating Text': True, 'Top Cuisine': True},
                            title='Number of Restaurants per Country',
                            color_continuous_scale='Viridis',  # Change to your preferred color scale
                            labels={'Restaurant Count': 'Restaurant Count', 
                                    'Average Cost for two': 'Average Cost', 
                                    'Aggregate rating': 'Aggregate Rating'}
                           )

# Update hover info to include all necessary data for countries
fig_country.update_traces(hoverinfo='text', text=country_hover_text)

# Update projection type of the map for countries
fig_country.update_geos(projection_type="natural earth")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

# TOP ANALYSIS
Header_component = html.H3("Zomato Top Analysis", style={'color': 'darkcyan', 'textAlign': 'center'})
# Define components for Top Analysis section
Component1 = dcc.Graph(id='component1')
Component2 = dcc.Graph(id='component2')
Component3 = dcc.Graph(id='component3')
Component4 = dcc.Graph(id='component4')
Component5 = dcc.Graph(id='component5')

# Define callback to update content based on the dropdown selection
@app.callback(
    Output('section-content', 'children'),
    [Input('section-dropdown', 'value')]
)
def update_section(selected_section):
    if selected_section == 'home':
        return [Home_content]
    elif selected_section == 'explore':
        return  [
            dbc.Row([
                dbc.Col(Explored_component, width=12)  # Adjust width as needed
            ]),
            dbc.Row([
                dbc.Col(total_count_component, width=3),
                dbc.Col(total_count_component1, width=3),
                dbc.Col(total_count_component2, width=3),
                dbc.Col(total_count_component3, width=3)
            ]),
            dbc.Row([
                dbc.Col(country_dropdown, width=6),
                dbc.Col(city_dropdown, width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='visualization-1'), width=6),
                dbc.Col(dcc.Graph(id='visualization-4'), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig5), width=6),
                dbc.Col(dcc.Graph(figure=fig8), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig2), width=4),
                dbc.Col(dcc.Graph(figure=fig3), width=4),
                dbc.Col(dcc.Graph(figure=fig6), width=4)
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(figure=fig_country)
                        ])
                    ]),
                    width=12
                ),
            ]),
        ]
    elif selected_section == 'top_analysis':
        return [
            dbc.Row([
                dbc.Col([Header_component])
            ]),
            dbc.Row([
                dbc.Col([country_dropdown]),
                dbc.Col([city_dropdown])
            ]),
            dbc.Row([
                dbc.Col([Component1]),  # Component 1
                dbc.Col([Component2]),  # Component 2
                dbc.Col([Component3])   # Component 3
            ]),
            dbc.Row([
                dbc.Col([Component4]),  # Component 4
                dbc.Col([Component5]),  # Component 5
                dbc.Col([dcc.Graph(figure=countfig_country)]) # Component 6
            ]),
        ]

# Callback to update Component 1 based on the selected country and city
@app.callback(
    Output('component1', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_component1(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    cuisine_counts = filtered_data['Cuisines'].value_counts().head(10)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=cuisine_counts.index, y=cuisine_counts.values, marker_color='darkmagenta'))
    fig.update_layout(title='Top 10 Cuisines', xaxis_title='Cuisine', yaxis_title='Number of Restaurants')
    return fig

# Callback to update Component 2 based on the selected country and city
@app.callback(
    Output('component2', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_component2(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    city_counts = filtered_data['City'].value_counts().head(10)

    fig = go.Figure()
    fig.add_bar(x=city_counts.index, y=city_counts.values)
    fig.update_layout(title='Top 10 Cities with Most Restaurants', xaxis_title='City', yaxis_title='Number of Restaurants')
    return fig

# Callback to update Component 3 based on the selected country and city
@app.callback(
    Output('component3', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_component3(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    top_restaurants = filtered_data.nlargest(15, 'Votes')
    fig = px.scatter(top_restaurants, x='Restaurant Name', y='Aggregate rating', color='Votes',
                     size='Votes', title='Top 15 Restaurants - Highest Rating',
                     labels={'Aggregate rating': 'Aggregate Rating', 'Average Cost for two': 'Average Cost'},
                     color_continuous_scale='Inferno')
    return fig

# Callback to update Component 4 based on the selected country and city
@app.callback(
    Output('component4', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_component4(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    chains = filtered_data['Restaurant Name'].value_counts().head(15)
    fig = px.bar(x=chains.index, y=chains.values, labels={'x': 'Restaurant Name', 'y': 'Number of Outlets'},
                  title="Top 15 Restaurants by Number of Outlets", color=chains.values, color_continuous_scale='deep')
    return fig

# Callback to update Component 5 based on the selected country and city
@app.callback(
    Output('component5', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_component5(selected_country, selected_city):
    filtered_data = data[data['Country'] == selected_country]
    if selected_city:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    voting_rating = filtered_data.groupby('Restaurant Name')[['Votes']].mean().sort_values('Votes', ascending=False)
    bad_count = filtered_data[(filtered_data["Aggregate rating"] < 3) & (filtered_data["Aggregate rating"] > 0)]
    bad_restaurants = (
        bad_count[bad_count['Votes'] > 500]
        .groupby('Restaurant Name', as_index=False)
        .agg({'Aggregate rating': 'mean', 'Votes': 'mean'})
        .sort_values(by='Aggregate rating', ascending=True)
    )
    fig = px.bar(
        bad_restaurants,
        x='Aggregate rating',
        y='Restaurant Name',
        orientation='h',
        color='Votes',
        title='Least Rated Restaurants with Votes > 500',
        labels={'Aggregate rating': 'Aggregate Rating', 'Restaurant Name': 'Restaurant Name'},
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        xaxis_title='Aggregate Rating',
        yaxis_title='Restaurant Name',
        coloraxis_colorbar_title='Votes'
    )
    return fig

# Component6 
# Get the count of restaurants in each country
country_rest = data["Country"].value_counts()

# Get the counts for India and the United States
india_count = country_rest.get('India', 0)
us_count = country_rest.get('United States', 0)

# Filter to exclude India and the United States
filtered_country_rest = country_rest[~country_rest.index.isin(['India', 'United States'])]

# Get the total count for all other countries
other_count = filtered_country_rest.sum()

# Create a new series including counts for India, the United States, and all other countries
combined_country_rest = pd.Series({'India': india_count, 'United States': us_count, 'Other Countries': other_count})

# Plot the pie chart
countfig_country = px.pie(combined_country_rest, values=combined_country_rest.values, names=combined_country_rest.index, title="Country Distribution of Restaurants")


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

if __name__ == '__main__':
    app.run_server(debug=True)

