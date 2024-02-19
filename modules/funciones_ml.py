import pandas as pd
import pickle
import base64
import sklearn

PAGE_CONFIG = {"page_title"             : "CO2 Emissions Model - Streamlit",
                "page_icon"             : ":robot_face:",
                "layout"                : "wide",
                "initial_sidebar_state" : "expanded"}

def read_data():

    df = pd.read_csv(filepath_or_buffer = "sources/emisiones.csv")

    return df



def load_model(fuel_type):

    fuel_type = fuel_type.replace(" ", "_")

    with open(file = f"sources/model_{fuel_type}.pkl", mode = "br") as file:
        model = pickle.load(file)

    with open(file = f"sources/x_scaler_{fuel_type}.pkl", mode = "br") as file:
        x_scaler = pickle.load(file)

    with open(file = f"sources/y_scaler_{fuel_type}.pkl", mode = "br") as file:
        y_scaler = pickle.load(file)

    return model, x_scaler, y_scaler


def download_file(df, fuel_type = "all"):

    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}' download='{fuel_type}_data.csv'>Download CSV File</a>"

    return href

