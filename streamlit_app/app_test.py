# streamlit_app/app.py

# ---- 0. Imports ----
import streamlit as st
from streamlit_super_slider import st_slider
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
from branca.colormap import linear
from matplotlib import pyplot as plt
import plotly.express as px


# add a tab for extension ideas

# ---- 1. Streamlit UI ----
st.set_page_config(layout="wide")
tab1, tab2, tab3, tab4 = st.tabs(["Welcome!", "Map", "Pollution Distribution", "Dataframe"])
with tab1:
    st.title(":ocean: :recycle: The Ocean Cleanup Top Polluting Rivers")
    st.subheader("Adding Seasonality to The Ocean Cleanup's Top 10 Polluting Rivers in Southeast Asia")
    st.write("Changes in weather patterns have a huge influence on plastic pollution going from rivers into the ocean.")
    st.write("This app visualizes the seasonal pollution levels of the top 10 rivers in Southeast Asia, as ranked by The Ocean Cleanup.")
    st.write("Use the tabs above to explore the map, pollution distribution, and underlying data.")
with tab2:
    st.title(":earth_asia: Seasonal River Pollution in SE Asia")
    st.subheader("Visualizing the seasonal pollution levels of the top 10 rivers in Southeast Asia, ranked by The Ocean Cleanup. " \
    "The seasonality is informed by my own modelling of the data, which is based on the average changing rainfall levels across SE Asia throughout the year.")
    st.write("Use the slider to select a month and toggle between raw and normalized pollution data.")
    st.write("The map shows the pollution levels of each river for the selected month, with circle markers sized by the pollution volume and colored by the pollution level.")
    st.write("The Raw data makes for a more accurate representation of the pollution levels across time, while the Normalized data allows for a more intuitive comparison of pollution levels between rivers.")


    # ---- 2. Load Data  ----
    @st.cache_data
    def load_data():
        df = pd.read_pickle(r'C:\\Users\\liamr\\OneDrive\\Documents\\Playground\\river_plastic\\data\\monthly_pollution_gdf.pkl')
        

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


    # Setting up the map to centre on Southeast Asia
    # map_center = [9.4581963681147, 120.76606274396]


    map_center = [5.285153, 105.76606274396]


    m = folium.Map(location=map_center, zoom_start=4.5,tiles='CartoDB dark_matter') # Add zoom_start for initial view
    # tiles='CartoDB positron'

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
    st.dataframe(df_month, use_container_width=True)    



    # ---- 9. Data Sources ----
    st.write("### Data Sources")
    st.write("This is the underlying data for the top 10 rivers in Southeast Asia, ranked by The Ocean Cleanup. " \
    "\n\nThe monthly pollution levels are produced by my own modelling of the data, which is based on the average changing rainfall levels across SE Asia throughout the year. " )
    st.write("The average yearly plastic pollution data is sourced from The Ocean Cleanup's [Global River Plastic Pollution Ranking](https://theoceancleanup.com/rivers/). "
    "\n\nThe monthly rainfall data is sourced from [World Bank Climate Data](https://climateknowledgeportal.worldbank.org/download-data). " \
    "\n\nThe river locations are sourced from [OpenStreetMap](https://www.openstreetmap.org/). " \
    "\n\nFor more information on the data sources, please refer to the [GitHub repository](https://github.com/lemrob/river_plastic_pollution).")
