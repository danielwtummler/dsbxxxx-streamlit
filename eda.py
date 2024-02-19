import streamlit as st
import plotly.express as px

from modules.funciones_ml import read_data


def eda():

    st.title("Exploratory Data Analysis :bar_chart:")

    df = read_data()

    with st.expander(label = "DataFrame", expanded = False):
        st.dataframe(df)

    # Year
    year_options = ["All"] + list(df["Model Year"].unique())
    year = st.sidebar.selectbox(label = "Model Year",
                                options = year_options)

    df_sidebar = df[df["Model Year"] == year] if year != "All" else df

    # Make
    make_options = list(df_sidebar["Make"].value_counts().index)
    make = st.sidebar.multiselect(label = "Make", options = make_options,
                                  default = make_options[:10])
    
    df_sidebar = df_sidebar[df_sidebar["Make"].isin(make)]

    # Vehicle Class
    
    vehicle_options = ["All"] + list(df_sidebar["Vehicle Class"].value_counts().index)
    vehicle = st.sidebar.selectbox(label = "Vehicle Class",
                                   options = vehicle_options)

    df_sidebar = df_sidebar[df_sidebar["Vehicle Class"] == vehicle] if vehicle != "All" else df_sidebar

    # Columnas

    col1, col2 = st.columns([1, 1])

    # Scatter Plot
    fig_scatter = px.scatter(data_frame = df_sidebar,
                             x          = "Fuel Consumption City",
                             y          = "CO2 Emissions",
                             color      = "Fuel Type",
                             # size       = "Engine Size",
                             #title      = f"{make} Cars - Year: {model_year}",
                             opacity    = 0.5)
    

    df_group = df_sidebar.groupby(by = "Fuel Type").agg({"Fuel Type" : ["count"]})
    df_group.columns = ["Fuel Type Count"]
    df_group.reset_index(inplace = True)

    # Bar Chart
    fig_bar = px.bar(data_frame = df_group,
                     x          = "Fuel Type Count",
                     y          = "Fuel Type",
                     color      = "Fuel Type",
                     text_auto  = True)
    fig_bar.update_yaxes(categoryorder = "total ascending")
    fig_bar.update_xaxes(title_text = "Total Cars")
    fig_bar.update_yaxes(title_text = "")

    # Pie Chart
    fig_pie = px.pie(data_frame = df_group,
                     names       = "Fuel Type",
                     values      = "Fuel Type Count",
                     color       = df_group.columns[0])
    
    # Violin Plot
    fig_violin = px.violin(data_frame = df_sidebar,
                            x          = "CO2 Emissions",
                            color      = "Fuel Type")
    # line plot

    df_group_line = df[df["Make"].isin([m.split()[0] for m in make])].groupby(by = ["Model Year", "Make"], as_index = False)\
                                                                     .agg({"CO2 Emissions" : ["min", "mean", "max"]})
    df_group_line.columns = ["Model Year", "Make", "min", "mean", "max"]

    fig_line = px.line(data_frame = df_group_line,
                        y          = "mean",
                        x          = "Model Year",
                        color      = "Make",
                        title      = "CO2 Emissions (Avg) per Year")
    
    fig_line.update_xaxes(title_text = "Year")
    fig_line.update_yaxes(title_text = "CO2 Emissions (Avg)")
    
    col1.plotly_chart(figure_or_data = fig_scatter, use_container_width = True)
    col1.plotly_chart(figure_or_data = fig_bar, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig_pie, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig_violin, use_container_width = True)
    st.plotly_chart(figure_or_data = fig_line, use_container_width = True)

if __name__ == "__eda__":

    eda()