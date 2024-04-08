import requests
import streamlit as st
import datetime
import pandas as pd
import json

import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    layout="wide",
    page_title="Local Entity Global Rankings",
)

# Function to retrieve data from the API
def get_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main function to run Streamlit app
def main():
    st.title('Local Entity Global Rankings')

    # Select function
    function = st.selectbox(
        'Function',
        ('iGV', 'iGT', 'iGTe', 'oGV', 'oGT', 'oGTe')
    )

    # Select status
    status = st.selectbox(
        'Status',
        ('Applied', '')
    )

    # Select entity
    entity = st.selectbox(
        'Entity',
        ('CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata')
    )

    #defining entity ids
    entity_id = ['222', '872', '1340', '2204', '221', '2175', '2186', '4535', '5490']

    #select start date
    sd = st.date_input("Start Date", datetime.date(2023, 12, 31))
    st.write('Start Date:', sd)

    #select end date
    ed = st.date_input("End Date", datetime.date(2024, 1, 31))
    st.write('End Date:', ed)

    # Define API URL with parameters
    api_url = 'https://analytics.api.aiesec.org/v2/applications/analyze.json'
    access_token = '0b085db925bfe08eb8b7acbe9c53eefd26fbe6347cb943ac1da87b1204e5c8db'
    products='Total'

    # Main loop for each entity
    for entity_index, entity_name in enumerate(entity):
        st.title(entity_name)

        # Construct the complete URL
        url = f"{api_url}?access_token={access_token}&start_date={sd}&end_date={ed}&performance_v3%5Boffice_id%5D={entity_id[entity_index]}&products={products}"

        # Retrieve data from the API
        data = get_api_data(url)

        # Check if data is retrieved successfully
        if data:
            st.write('Data retrieved successfully!')

            # Visualize entity on a bar chart by Product
            x_values = ['CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata']
            y_values = [10, 20, 15, 12, 2, 23, 1, 5, 12]

            fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])

            fig.update_layout(title='LC Global Ranking by Product',
                xaxis_title='Local Committee',
                yaxis_title='Ranking')

            st.plotly_chart(fig)

        else:
            st.error('Failed to retrieve data from the API')

if __name__ == "__main__":
    main()
