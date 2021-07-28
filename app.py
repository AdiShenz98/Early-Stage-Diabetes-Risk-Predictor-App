# Core Packages
import streamlit as st

# Applets
from eda_app import eda_main
from ml_app import ml_main

# Page Configuration
PAGE_CONFIG = {"page_title":"Early Stage Diabetes Risk Predictor","page_icon":"images/favicon.png"}
st.set_page_config(**PAGE_CONFIG,)


# Page Styling
def page_styling():
    page_style = '''
    <style>
    .stButton{
        text-align: center;
        font-size: 110%;
        }
    .stAlert{
    text-align: center;
        }
    
    </st
    '''
    return page_style

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Heading html
def title_html(heading):
    heading_html = '''
    <p style="
            text-align: center;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; 
            border: #f63366;
            border-style: double;
            border-radius: 10px;
            padding: 10px;
            font-size: 140%;
            ">
        {}
    </p>
    '''
    return heading_html.format(heading)

# Sub-heading html
def header_html(heading):
    heading_html = '''
    <h2 style="
            text-align: left;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            color: #055052;
            ">
        {}
    </h2>
    
    '''
    return heading_html.format(heading)

# Main Function
def main():
    page_style = page_styling()
    st.markdown(page_style,unsafe_allow_html=True)

    st.image("images/Diabetes_App_Title.png")

    Menu = ['Home', 'EDA', 'About']
    choice = st.sidebar.selectbox('Menu',Menu) 

    if choice == 'Home':
        st.write("")
        st.markdown(title_html('Home'),unsafe_allow_html=True)
        ml_main()
    elif choice == 'EDA':
        st.write("")
        st.markdown(title_html('Exploratory Data Analysis'),unsafe_allow_html=True)
        eda_main()
    elif choice == 'About':
        st.write("")
        st.markdown(title_html('About'),unsafe_allow_html=True)

        # About the App
        st.markdown(header_html("Early Stage Diabetes Risk Predictor App"),unsafe_allow_html=True)
        st.write('Individuals can use this Web-App to estimate their risk of developing diabetes at an early stage.')

        # Motivation
        st.markdown(header_html('Motivation'),unsafe_allow_html=True)
        motivation = ''' 
        Diabetes represents a spectrum of metabolic disorders, which has become a major health challenge worldwide. 
        The unprecedented economic development and rapid urbanization in Asian countries, particularly in India has led to a shift in health problems from communicable to non-communicable diseases. 
        Of all the non-communicable diseases, diabetes lead the list.
        \n
        **India** has a high prevalence of diabetes mellitus and the numbers are increasing at an alarming rate. 
        In India alone, diabetes is expected to increase from **40.6 million** in **2006** to **79.4 million** by **2030**. 
        Studies have shown that the prevalence of diabetes in urban Indian adults is about **12.1%**, the onset of which is about a decade earlier than their western counterparts and the prevalence of Type 2 diabetes is **4–6** times higher in urban than in rural areas. 
        The risk factors peculiar for developing diabetes among Indians include high familial aggregation, central obesity, insulin resistance and life style changes due to urbanization
        \n
        The rising incidence of diabetes and its complications are going to pose a grave health care burden on our country. 
        Timely effective interventions/measures and screening tests for complications at the time of diagnosis becomes imperative not only for early detection, 
        but also to prevent progression to end stage disease.
        \n
        > **This App can thus serve as an initial detection tool which can help in an early diagnosis**
        '''
        st.markdown(motivation)

        # Datasource
        st.markdown(header_html("Datasource"),unsafe_allow_html=True)
        source = '''
        The data was taken from **UCL** Machine Learning Repository
        > https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset./
        '''
        st.markdown(source)

        # About the Dataset
        st.markdown(header_html('About the Dataset'), unsafe_allow_html=True)
        st.markdown('The dataset was collected using direct questionnaires from the patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh and approved by a doctor.')



if __name__ == '__main__':
    main()
