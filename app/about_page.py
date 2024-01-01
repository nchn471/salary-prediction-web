import streamlit as st 

def show_about_page():
    #Data Pull and Functions
    st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    

    st.title('Data')
    #st.subheader('All data for this project was publicly sourced from:')
    col1,col2,col3=st.columns(3)
    col1.subheader('Source')
    col2.subheader('Description')
    col3.subheader('Link')
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('census_graphic.png',width=150)
        col1.write(':blue[U.S. Census Bureau]')
        col2.write('Demographic, housing, industry at zip level')
        #col2.write('American Community Survey, 5-Year Profiles, 2021, datasets DP02 - DP05')
        col3.write('https://data.census.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('cdc.png',width=150)
        col1.write(':blue[Centers for Disease Control and Prevention]')
        col2.write('Environmental factors at county level')
        col3.write('https://data.cdc.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('hud.png',width=150)\
        col1.write(':blue[U.S. Dept Housing and Urban Development]')
        col2.write('Mapping zip to county')
        col3.write('https://www.huduser.gov/portal/datasets/')

    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('ods.png',width=150)
        col1.write(':blue[OpenDataSoft]')
        col2.write('Mapping zip to USPS city')
        col3.write('https://data.opendatasoft.com/pages/home/')
    
    st.divider()
    
    st.title('Creator')
    with st.container():
        col1,col2=st.columns(2)
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**    Kevin Soderholm')
        col1.write('**Education:**    M.S. Applied Statistics')
        col1.write('**Experience:**    8 YOE in Data Science across Banking, Fintech, and Retail')
        col1.write('**Contact:**    kevin.soderholm@gmail.com or [linkedin](https://www.linkedin.com/in/kevin-soderholm-67788829/)')
        col1.write('**Thanks for stopping by!**')
        # col2.image('kevin8.png')