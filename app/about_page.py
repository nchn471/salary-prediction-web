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
    

    st.title('About project')

    st.markdown("##### Predicting developer's salary from Stack Overflow Developer Survey 2023 (https://insights.stackoverflow.com/survey)")
    st.markdown("##### This is the project we've chosen for the final assignment in the Python for Data Science course")

    st.divider()
    
    st.title('Our team')
    st.markdown('##### We are student of **Ho Chi Minh University of Science** ')
    st.markdown('##### Major: **Data Science** | Class: **21KDL1**')
    l, r = st.columns((4,6))

    with l:
        with st.container():
            st.divider()
            col1,col2 = st.columns(2)
            with col1:
                st.subheader('FULL NAME')
                st.write('##### Nguyễn Công Hoài Nam')
                st.write('##### Lê Nguyễn Hoàng Uyên')
                st.write('##### Trần Thị Uyên Nhi')
                st.write('##### Huỳnh Công Đức')

            with col2:
                st.subheader('ID')
                st.write('##### 21280099')
                st.write('##### 21280xxx')
                st.write('##### 21280xxx')
                st.write('##### 21280xxx')

    with r:
        st.image('./app/static/hcmus.png', width=350)


