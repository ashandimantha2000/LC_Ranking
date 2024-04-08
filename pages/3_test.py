import requests
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="LC Global Ranking",
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
    st.title('Test API Data Visualization')

    # Define API URL with parameters
    api_url = 'https://analytics.api.aiesec.org/v2/applications/analyze.json'
    access_token = '0b085db925bfe08eb8b7acbe9c53eefd26fbe6347cb943ac1da87b1204e5c8db'
    start_date = '2024-01-29'
    end_date = '2024-01-30'
    office_id = '1623'
    products='Total'
    Entity= 'Entity'
    # Construct the complete URL
    url = f"{api_url}?access_token={access_token}&start_date={start_date}&end_date={end_date}&performance_v3%5Boffice_id%5D={office_id}&products={products}&Entity={Entity}"

    # Retrieve data from the API
    data = get_api_data(url)

    # Check if data is retrieved successfully
    if data:
        st.write('Data retrieved successfully!')
        
        # Visualize data using Streamlit components
        st.write('Sample Data:')
        st.write(data)
        
        # Add more visualization components as needed
    else:
        st.error('Failed to retrieve data from the API')

if __name__ == "__main__":
    main()
