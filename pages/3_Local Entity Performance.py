import requests
import streamlit as st
import plotly.express as px
import datetime
import plotly.graph_objects as go
import pandas as pd
import json

st.set_page_config(
    layout="wide",
    page_title="Local Entity Performance",
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
    st.title('Local Entity Performance')

    # Select function
    # option = st.selectbox(
    #     'Function',
    #     ('iGV', 'iGT', 'iGTe', 'oGV', 'oGT', 'oGTe')
    # )

    # Select status
    # status = st.selectbox(
    #     'status',
    #     ('Applied', 'Approved', 'iGTe', 'oGV', 'oGT', 'oGTe')
    # )


    # Select function - test
    # function = st.selectbox(
    #     'Function',
    #     ('iGV', 'iGT', 'iGTe', 'oGV', 'oGT', 'oGTe')
    # )

    
   
    #Functional Parsing
    # if option == 'iGV':
    #     function = '/^i_.*_[7]$/'
    # elif option == 'iGT':
    #     function = '/^i_.*_[8]$/'
    # elif option == 'iGTe':
    #     function = '/^i_.*_[9]$/'
    # elif option == 'oGV':
    #     function = '/^o_.*_[7]$/'
    # elif option == 'oGT':
    #     function = '/^o_.*_[8]$/'
    # elif option == 'oGTe':
    #     function = '/^o_.*_[9]$/'



    # Select entity
    entity = st.selectbox(
        'Entity',
        ('CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata')
    )

    if entity == 'CC':
        lc_id = '222'
    elif entity == 'CN':
        lc_id = '872'
    elif entity == 'CS':
        lc_id = '1340'
    elif entity == 'Kandy':
        lc_id = '2204'
    elif entity == 'USJ':
        lc_id = '221'
    elif entity == 'Ruhuna':
        lc_id = '2175'
    elif entity == 'NSBM':
        lc_id = '2186'
    elif entity == 'NIBM':
        lc_id = '4535'
    elif entity == 'Rajarata':
        lc_id = '5490'

    # Select status - Test
    status = st.selectbox(
        'Status',
        ('Applied', '')
    )
    
    #select start date
    sd = st.date_input("Start Date", datetime.date(2023, 12, 31))
    st.write('Start Date:', sd)

    #select end date
    ed = st.date_input("End Date", datetime.date(2024, 1, 31))
    st.write('End Date:', ed)




    # Define API URL with parameters
    api_url = 'https://analytics.api.aiesec.org/v2/applications/analyze.json'
    access_token = '0b085db925bfe08eb8b7acbe9c53eefd26fbe6347cb943ac1da87b1204e5c8db'
    # lc_id = '1623'
    products='Total'
    

    # Construct the complete URL
    url = f"{api_url}?access_token={access_token}&start_date={sd}&end_date={ed}&performance_v3%5Boffice_id%5D={lc_id}&products={products}"

    # Retrieve data from the API
    data = get_api_data(url)

    
    # Check if data is retrieved successfully
    if data:
        st.write('Data retrieved successfully!')
        
        #status check
        # if status == 'Applied':
        #     #get the count of i_applied_8 from data
        #     values = [value for value in data['i_applied_8'].values()]
        #     value = values[0]
        #     st.write(value)
        # elif status == 'Realized':
        #     #get the count of i_applied_9 from data
        #     values = [value for value in data['i_realized_9'].values()]
        #     value = values[0]
        #     st.write(value)

        #function check
        # if function == 'iGV':
        #     #get the count of o_applied_8 from data
        #     # values = [value for value in data['i_applied_7'].values()]
        #     # value = values[0]
        #     valueiGV = [value for value in data['i_applied_7'].values()][0]
        #     # st.write(value)
        # elif function == 'iGT':
        #     valueiGT = [value for value in data['i_applied_8'].values()][0]
        #     # st.write(value)
        # elif function == 'iGTe':
        #     valueiGTe = [value for value in data['i_applied_8'].values()][0]
        #     # st.write(value)
        # elif function == 'oGV':
        #     valueoGV = [value for value in data['o_applied_7'].values()][0]
        #     # st.write(value)
        # elif function == 'oGT':
        #     valueoGT = [value for value in data['o_applied_8'].values()][0]
        #     # st.write(value)
        # elif function == 'oGTe':
        #     valueoGTe = [value for value in data['o_applied_9'].values()][0]
        #     # st.write(value)
        

        valueiGV = [value for value in data['i_applied_7'].values()][0]
        valueiGT = [value for value in data['i_applied_8'].values()][0]
        valueiGTe = [value for value in data['i_applied_8'].values()][0]
        valueoGV = [value for value in data['o_applied_7'].values()][0]
        valueoGT = [value for value in data['o_applied_8'].values()][0]
        valueoGTe = [value for value in data['o_applied_9'].values()][0]
            # st.write(value)
        
        
        # Visualize data using bar chart
        labels = [key for key in data['i_applied_8'] ]
        #get the count of i_applied_8 from data
        # values = [value for value in data['i_applied_8'].values()]
                
        # fig = px.bar(x=labels, y=values, title='Global Ranking Bar Chart')
        # st.plotly_chart(fig)

        #visualize entity on a bar chart by product
        # x_values = ['CC', 'CN', 'CS', 'Kandy', 'USJ', 'Ruhuna', 'NSBM', 'NIBM', 'Rajarata']
        # y_values = [10, 20, 15, 12, 2, 23, 1, 5, 12]  

        # fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])

        # fig.update_layout(title='LC Global Ranking by Product',
        #     xaxis_title='Local Committee',
        #     yaxis_title='Ranking')

        # st.plotly_chart(fig)

        
        
        #visualize entity on a bar chart by Product    
        x_values = ['iGV', 'iGT', 'iGTe', 'oGV', 'oGT', 'oGTe']
        y_values = [valueiGV, valueiGT, valueiGTe, valueoGV, valueoGT, valueoGTe]  

        fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])

        #entity title
        st.title(entity) 
        #metric
        # st.metric(label="Applied", value=value)

        fig.update_layout(title='Productwise Local Entity Performances',
            xaxis_title='Product',
            yaxis_title='Global Rank')

        st.plotly_chart(fig)

   
    else:
        st.error('Failed to retrieve data from the API')

if __name__ == "__main__":
    main()
