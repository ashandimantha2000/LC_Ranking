import requests
import streamlit as st
import plotly.express as px

# Function to retrieve data from the API
def get_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main function to run Streamlit app
def main():
    st.title('API Data Visualization')

    # Define API URL with parameters
    api_url = 'https://analytics.api.aiesec.org/v2/applications/analyze.json'
    access_token = '0b085db925bfe08eb8b7acbe9c53eefd26fbe6347cb943ac1da87b1204e5c8db'
    start_date = '2024-01-29'
    end_date = '2024-01-30'
    office_id = '222'
    # Construct the complete URL
    url = f"{api_url}?access_token={access_token}&start_date={start_date}&end_date={end_date}&performance_v3%5Boffice_id%5D={office_id}"

    # Retrieve data from the API
    data = get_api_data(url)

    # Check if data is retrieved successfully
    if data:
        st.write('Data retrieved successfully!')
        
        # Visualize data using bar chart
        labels = [key for key in data['some_key']]
        values = [value for value in data['some_key'].values()]
        
        fig = px.bar(x=labels, y=values, title='Sample Bar Chart')
        st.plotly_chart(fig)
        
    else:
        st.error('Failed to retrieve data from the API')

if __name__ == "__main__":
    main()
