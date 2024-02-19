import streamlit as st

from page_app import page_app_func
from ml import ml
from eda import eda
from about import about

from modules.funciones_ml import PAGE_CONFIG

st.set_page_config(**PAGE_CONFIG)

def main():

    menu = ["Main App", "Exploratory Data Analysis", "Machine Learning Model", "About"]

    page = st.sidebar.selectbox(label = "Menu", options = menu)

    if page == "Main App":

        page_app_func()

        pass

    elif page == "Exploratory Data Analysis":
        
        eda()
        pass

    elif page == "Machine Learning Model":

        ml()

        pass

    else:

        about()

        pass

if __name__ == "__main__":
    main()