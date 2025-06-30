# Plastic Pollution Seasonality Model: 
## Extending the Ocean Cleanup's River Pollution model to consider for seasonal rainfall


## Key Details:
- Annual Plastic Pollution is taken from The Ocean Cleanup's model:
- Rainfall Data is an external factor to the model, taken from WorldClim2
- Project focus is on **South East Asia** rivers
- Top 10 polluting rivers from South East Asian are used as the subset for my model
- **Model**:
- - Uses historical rainfall data to find an average monthly distribution of these rivers over the years 1990-2019
- - These averages are used to infer the average distribution of plastic pollution over the course of a year, for each river
- **Visualisations**:
- - Within the streamlit app, you can switch between a map view and a graph-based view of these distributions

## Outline of Ocean Cleanup's Model


## Extensions to improve model

- **Include more river features** 
- - My project focuses on the initial stage of the Ocean Cleanup's pollution method to calculate the probability of pollution emitted by the river (Mobilisation)
- - - 1) Include wind data to build a complete picture of this first stage
- - - 2) Implement data sources to include the next stages of the model (Transport to River, Transport to Ocean)
- - - 3) Include data showing Mismanaged Plastic Waste (MPW) for each river location

- **Further environmental considerations**
- - How does rainfall and plastic pollution seasonality interact with wildlife? These may be considerations for The Ocean Cleanup to take


## Steps Taken During the Project:

### Pre-processing:

- Downloading, processing and cleaning data on river pollution, geo-locations, climate rainfall data, and inital vizualisations

### Exploratory Data Analysis (EDA)

- Exploring the data in further detail.
- Vizualisation long-term rainfall trends and within-year seasonality, understanding the siginificance of the interaction between rainfall and plastic pollution

### Model Build:

- Building the model to obtain predictions for the monthly distribution of average yearly plastic pollution levels


### Streamlit App:

- Producing a User-Friendly web app to explore these predictions.
- User can view the monthly split on a map, similar to the Ocean Cleanup's own dashboard
- User can dive deeper into the monthly distributions on a distribution chart
- User can explore and interact the dataframes, of all data sources and the model predictions




