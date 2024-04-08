import requests
import streamlit as st
import datetime
import pandas as pd
import json

import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    layout="wide",
    page_title="Local Entity Rankings",
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


    #defining entity ids
    entity_id = ['222', '872', '1340', '2204', '221', '2175', '2186', '4535', '5490']

    #defining entity ids


    #select start date
    sd = st.date_input("Start Date", datetime.date(2023, 12, 31))
    # st.write('Start Date:', sd)

    #select end date
    ed = st.date_input("End Date", datetime.date(2024, 1, 31))
    # st.write('End Date:', ed)

    st.write('This may take more than a minute to load the data from the API. Please wait...')


    # Define API URL with parameters
    api_url = 'https://analytics.api.aiesec.org/v2/applications/analyze.json'
    access_token = '0b085db925bfe08eb8b7acbe9c53eefd26fbe6347cb943ac1da87b1204e5c8db'
    products='Total'

    # Construct the complete URL
    url = f"{api_url}?access_token={access_token}&start_date={sd}&end_date={ed}&performance_v3%5Boffice_id%5D={entity_id[0]}&products={products}"

    # Retrieve data from the API
    data = get_api_data(url)

    # Retrieve data from the API Spinner
    with st.spinner("Please Wait!  Data loading from the API may take a few minutes."):
        data = get_api_data(url)
    
    #geting the count of LCs
    lc_list = ['CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata']
    length = len(lc_list)

    #make a python list with above length
    entity_values = ['', '', '', '', '', '', '', '', '']

    index = 0
    while index < length:
        url = f"{api_url}?access_token={access_token}&start_date={sd}&end_date={ed}&performance_v3%5Boffice_id%5D={entity_id[index]}&products={products}"
        
        if function == 'iGV':
            value = [value for value in get_api_data(url)['i_applied_7'].values()][0]
            entity_values[index] = value
        elif function == 'iGT':
            value = [value for value in get_api_data(url)['i_applied_8'].values()][0]
            entity_values[index] = value
        elif function == 'iGTe':
            value = [value for value in get_api_data(url)['i_applied_8'].values()][0]
            entity_values[index] = value
        elif function == 'oGV':
            value = [value for value in get_api_data(url)['o_applied_7'].values()][0]
            entity_values[index] = value
        elif function == 'oGT':
            value = [value for value in get_api_data(url)['o_applied_8'].values()][0]
            entity_values[index] = value
        elif function == 'oGTe':
            value = [value for value in get_api_data(url)['o_applied_9'].values()][0]
            entity_values[index] = value
        index += 1

    #visualize entity on a bar chart by Product    
    x_values = ['CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata']
    y_values = entity_values

    # Sort the entity_values and x_values in descending order
    sorted_values, sorted_entities = zip(*sorted(zip(y_values, x_values), reverse=True))

    
    fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])

    #chart title
    st.title(function) 
    #metric
    # st.metric(label="Applied", value=value)

    fig.update_layout(title='',
        xaxis_title='Product',
        yaxis_title='Applied')

    st.plotly_chart(fig)

    st.write('The following is the ranking of the Local Entities based on the selected function and status.')

    # Preview the rank of the entities
    for rank, entity in enumerate(sorted_entities, start=1):
        st.info(f"Rank {rank}: {entity}")


    #rank entity_values
    

    # Retrieve data from the API
    data = get_api_data(url)
    # Retrieve data from the API

    
    # Check if data is retrieved successfully
    if data:
        st.write('Data retrieved successfully!')
    else:
        st.error('Failed to retrieve data from the API')
    
     
    

if __name__ == "__main__":
    main()
