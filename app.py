# streamlit_app/app.py

# ---- 0. Imports and Paths ----
import streamlit as st
from streamlit_super_slider import st_slider
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
from branca.colormap import linear
from matplotlib import pyplot as plt
import plotly.express as px
from PIL import Image



# Getting relative paths for data files
import os
import sys

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(repo_root)


from src.paths import get_data_path

# add a tab for extension ideas

# ---- 1. Streamlit UI ----
st.set_page_config(layout="wide")
tab1, tab2, tab3, tab4 = st.tabs([":earth_asia: Welcome!", ":world_map: Map", ":bar_chart: Pollution Distribution", ":mag: Dataframe"])

# TAB 1: Welcome
with tab1:
    BACKGROUND_paragraph = """
    Ocean Cleanup researchers found: **the top 1000 polluting rivers are responsible for 80% of the plastic pollution** entering  the ocean from rivers.
    \n\n They built a model to better understand the levels of pollution from these rivers.
    \n\n The **map visualisation** for their predictions can be found here: https://theoceancleanup.com/sources/ 
    \n\n For each river, their model predicts the **annual** levels of pollution.
    """

    MY_MODEL_paragraph = """
    This **baseline model** introduces **seasonality** into the paradigm, by considering **rainfall**.
    \n\n This influences pollution rates as shown in the first part of the model (below) – through **Mobilization**.
    \n\n Focuses on the top 10 polluters in **South East Asia** – a high polluting area with dramatic seasonal shifts in rainfall.
    \n\n Aggregates historical rainfall patterns to predict the **average monthly** pollution levels of each river.
    """

    AREAS_FOR_ENHANCEMENT_paragraph = """
    This is a **baseline** model, which can be extended in various ways:
    \n\n 1. Collecting data for **each step of the model** shown below for a more accurate prediction of the **probability of plastic emission** per river  starting with **wind data* to complete the **Mobilization** step.
    \n\n 2. Collecting data for Mismanaged Plastic Waste (MPW) – shown below.
    \n\n 3. Proximity to Large cities and areas of human activity.
    \n\n 4. **Time-series predictions**:  can long-term climate and economic data be used to predict trends in river pollution? This could serve particularly useful when considering where to place interceptors.
    """

    # Function to resize an image
    def resize_image(image_path, size):
        img = Image.open(image_path)
        resized_img = img.resize(size)
        return resized_img

    # Function for normal sized column on its own, within the wide layout I set at the start of the script
    def st_normal():
        _, col, _ = st.columns([1, 2, 1])
        return col
    
    # User Instructions
    st.write("*Toggle through the tabs above to explore the model results! Data sources can be found in the final tab, along with the underlying data used for the model.*")

    # Titles and Introduction
    st.title(":ocean: *Top 10 Plastic Polluting Rivers in South East Asia: Seasonality Model*")
    st.write("**Aim**: To Extend Ocean Cleanup's model, by adding **seasonality** to The Ocean Cleanup's Top Polluting Rivers Model")
    st.write("**Purpose:** To introduce a simple prediction of how rainfall can influence pollution rates from rivers into the Ocean.")

    col1, col2, col3 = st.columns(3)

    with col1:
        tile = col1.container(height=350)
        tile.write("#### *Ocean Cleanup's Model*")
        tile.write(BACKGROUND_paragraph)

    with col2: 
        tile = col2.container(height=350)
        tile.write("#### *My Seasonal Model*")
        tile.write(MY_MODEL_paragraph)

    with col3:
        tile = col3.container(height=350)
        tile.write("#### *Areas for Enhancement*")
        tile.write(AREAS_FOR_ENHANCEMENT_paragraph)


    image_path = "images/plastic_emissions_model.png"  
    new_size = (600, 400) 
    resized_image = resize_image(image_path, new_size)
    st_normal().write("#### The Ocean Cleanup's Model for calculating River Emission Rates")
    st_normal().image(resized_image, caption = "Source: The Ocean Cleanup's Model, from Meijer et al. (2021). Link here: https://www.science.org/doi/10.1126/sciadv.aaz5803", use_container_width=True)
    
with tab2:
    st.title(":world_map: Seasonal River Pollution in SE Asia")
    # st.write("Switch to the Normalized data to view a more intuitive comparison of pollution levels between rivers.")
    st.write("Note: The baseline pollution estimates are based on the original Meijer et al. dataset. The Ocean Cleanup’s online map uses updated sources, so numbers may differ")


    # ---- 2. Load Data  ----
    @st.cache_data
    def load_data():
        df = pd.read_pickle(get_data_path("monthly_pollution_gdf.pkl"))
        

        # Ensure normalized values exist
        if 'pollution_norm' not in df.columns:
            df['pollution_norm'] = df.groupby('month')['monthly_pollution'].transform(
                lambda x: (x - x.min()) / (x.max() - x.min())
            )
        return df

    gdf = load_data()

    # ---- 3. Toggle and Slider ----

    pollution_type = st.radio(
        "Pollution Data Type",
        ['Raw', 'Normalized'],
        index=0,
        horizontal=True
    )


    # iterating through the months so the first slider dot is January and last is December
    month_list = [
        "Blank", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]


    month = st_slider(values = month_list, 
                    default_value=1, dots=True, key="month_slider")

    st.write("Selected month:", month_list[month])


    # ---- 4. Data Selection ----
    col = 'monthly_pollution' if pollution_type == 'Raw' else 'pollution_norm'

    # Filter the GeoDataFrame for the selected month of the slider
    df_month = gdf[gdf['month'] == month]
    max_pollution = gdf[col].max()
    min_pollution = gdf[col].min()


    colormap = linear.YlOrRd_09.scale(min_pollution, max_pollution)
    colormap.text_color = 'white'
    colormap.caption = 'Pollution Level'


    # Slider for month (you can customize with real month names if needed)


    # ---- 5. Setting up map ----

    # Create a geometry list from the GeoDataFrame
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]


    map_center = [5.285153, 105.76606274396]


    m = folium.Map(location=map_center, zoom_start=4.5,tiles='CartoDB dark_matter') # Add zoom_start for initial view

    # ---- 6. Plotting the Data ----
    # Looping through to plot a map for each month

    # Plot each river
    for _, row in df_month.iterrows():
        pollution_value = row[col]
        normalized = (pollution_value - min_pollution) / (max_pollution - min_pollution)
        color = colormap(pollution_value)
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius = 5 + normalized * 15,  # Now radius is always between 5 and 20
            color='color',
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"<b>Country:</b>	 <i>{row['country']}</i><br><br><b>Pollution Rank:</b> <i>{row['rank']}</i><br><br><b>Pollution Volume:</b> <i>{pollution_value:.2f}</i>"
        ).add_to(m)
        m.add_child(colormap)


    # Use st_folium to render the map
    st_data = st_folium(m, width=1300, height=700)

# TAB 3: Pollution Distribution
with tab3:
    st.title(":bar_chart: Pollution Distribution")
    st.subheader("Visualizing the distribution of pollution levels across the top 10 rivers in Southeast Asia.")

    # ---- 7. Pollution Distribution ----
    # Create a histogram of the pollution data

    # Starting with the dropdown list for user to select which river to view
    option = st.selectbox(
        'Select a River',
        options=gdf['rank'].unique(),
        index=0
    )

    st.write(f"Selected River: Polluter Rank #{option}")

    # Filter the GeoDataFrame for the selected river
    river = gdf[gdf['rank'] == option]

    # Create a bar chart of the monthly pollution levels for the selected river
    pollution_distribution = px.bar(river, x='month', y='monthly_pollution', title=f'Monthly Pollution levels for the river polluter #{option}, located in {river["country"].values[0]}')
    pollution_distribution.update_traces(marker_color='indianred')  
    pollution_distribution.update_layout(xaxis_title='Month', yaxis_title='Pollution Level (kg)')

    # Show the bar chart in Streamlit
    st.plotly_chart(pollution_distribution, use_container_width=True)


    
# TAB 4: Dataframe
with tab4:
    st.title(":mag: Dataframe View and Data Sources")
    st.subheader("Visualizing the underlying data for the top 10 rivers in Southeast Asia.")

    # ---- 8. Dataframe ----
    # Create a dataframe of the top 10 rivers in Southeast Asia, that the users can interact with

    # Deleting the geometry column for display as I already have lon and lat columns
    df_month_display = df_month.copy()
    df_month_display = df_month_display.drop(columns='geometry')

    st.dataframe(df_month_display, use_container_width=True)



    # ---- 9. Data Sources ----
    st.write("### Data Sources")
    st.write("This is the underlying data for the top 10 rivers in Southeast Asia, ranked by The Ocean Cleanup. " 
    "\n\nThe monthly pollution levels are produced by my own modelling of the data, which is based on the average changing rainfall levels across SE Asia throughout the year." )
    st.write("The average yearly plastic pollution data is sourced from The Ocean Cleanup's [Global River Plastic Pollution Ranking](https://theoceancleanup.com/rivers/)."
    "\n\nThe monthly rainfall data is sourced from [World Bank Climate Data](https://climateknowledgeportal.worldbank.org/download-data). " 
    "\n\nThe river locations are sourced from [OpenStreetMap](https://www.openstreetmap.org/). " 
    "\n\nFor more information on the data sources, please refer to the [GitHub repository](https://github.com/lemrob/river_plastic_pollution).")
