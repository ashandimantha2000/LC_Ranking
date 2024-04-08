import streamlit as st

# Main function to run Streamlit app
def main():
    st.set_page_config(
    layout="wide",
    page_title="Dashboard - Local Entity Global Rankings",
)
    st.title('Hey AIESEC in Sri Lanka 💙')

    st.write('Welcome to the AIESEC in Sri Lanka Local Entity Global Rankings. Here, you can explore and compare the performance of Local Committees (LCs) of AIESEC in Sri Lanka.')

    st.title('Features')
    st.success('🌍 View Global Rankings: Select the function and status to see how different LCs in Sri Lanka are performing globally.')
    st.success('📊 Entity Performance: Analyze the performance of products and local entities of AIESEC in Sri Lanka.')

    st.title('Limitations')
    st.warning("⏳ Currently, only LCs (Local Committees) of AIESEC in Sri Lanka are accessible. Including global entities in the ranking requires more time to retrieve data from the Expa API. Can just add the global entities to the app by inserting the office_id/lc_id in the python data list")
    st.warning("⌛ Data Retrieval Time: The data is retrieved from the Expa API, which may take some time. Please be patient while the data is being fetched.")
    st.warning("⌛ Currently this application is works only for the 'Applied' state of the funnel. ")

    st.markdown('---')
    st.subheader('About the Developer')
    # st.image('https://avatars.githubusercontent.com/u/85834813?v=4', width=200)
    st.write('Hello! I am Ashan Dimantha Herath, MCVP Applicant 24.25 for AIESEC in Sri Lanka.')
    st.write('If you have any questions or feedback about this application, please reach out to me:')
    st.write(' Website: https://ashandimantha.vercel.app/')
    st.write(' Email: ashan.herath16@aiesec.net')
    st.markdown('---')
if __name__ == "__main__":
    main()
