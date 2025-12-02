# Plastic Pollution Seasonality Model: 
### Extending The Ocean Cleanup’s river pollution model with seasonal rainfall dynamics


## 🌍 Project Overview

This project builds on [The Ocean Cleanup](https://theoceancleanup.com/)'s model of river-based plastic pollution by introducing **seasonal rainfall as a key factor**. 

Focusing on **South East Asia**, the region with many of the world's most polluting rivers, this model:

- Uses historical rainfall data from **WorldClim2** (1990–2019)
- Applies average monthly rainfall profiles to distribute annual plastic pollution over the year
- Analyzes the **top 10 plastic-polluting rivers in the region**
- Visualizes the seasonality using both interactive maps and distribution graphs in a Streamlit Web App


## 🚀 Try the App

👉 [Launch the Streamlit App](https://riverplasticpollution-7btcohpfepcb4yhizbstac.streamlit.app/)

Explore monthly plastic pollution distributions, switch between interactive map and graph views, and interact with the raw data behind the model.



## 🔬 Model Summary
- Annual Plastic Pollution is taken from The Ocean Cleanup's model
- Rainfall Data is an external factor to the model, taken from WorldClim2
- Applies rainfall proportions to estimate **monthly plastic emission profiles**
- Project focus is on **South East Asia** rivers
- Top 10 polluting rivers from South East Asian are used as the subset for my model
- **Outputs**:
  - Monthly split of plastic pollution per river
  - Interactive geospatial and graph-based visualizations


## The Ocean Cleanup's Model
Their main dashboard can be found at https://theoceancleanup.com/sources/.
An outline of their model is shown on the home page of my web app!


## 📝 Extensions to Improve the Model

- **Include more river features** 
    - My project focuses on the initial stage of the Ocean Cleanup's pollution method to calculate the probability of pollution emitted by the river (Mobilisation)
        - 1) Include wind data to build a complete picture of this first stage
        - 2) Implement data sources to include the next stages of the model (Transport to River, Transport to Ocean)
        - 3) Include data showing Mismanaged Plastic Waste (MPW) for each river location

- **Further environmental considerations**
    - How does rainfall and plastic pollution seasonality interact with wildlife? These may be considerations for The Ocean Cleanup to take


## 🧪 Steps Taken During the Project

### Pre-processing:

- Downloading, processing and cleaning data on river pollution, geo-locations, climate rainfall data, and inital visualizations

### Exploratory Data Analysis (EDA)

- Exploring the data in further detail.
- Vizualisation long-term rainfall trends and within-year seasonality, understanding the siginificance of the interaction between rainfall and plastic pollution

### Model Build:

- Building the model to obtain predictions for the monthly distribution of average yearly plastic pollution levels


### Streamlit App:

- Producing a User-Friendly web app to explore these predictions.
- User can view the monthly split on a map, similar to the Ocean Cleanup's own dashboard
- User can dive deeper into the monthly distributions on a distribution chart
- User can explore and interact with the dataframes, of all data sources and the model predictions


## 📦 Requirements

To run the project locally:

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows

2. Install dependencies:

    pip install -r requirements.txt

3. Launch the app:

    streamlit run app/app.py

4. You need to input the data sources to run the code - Please check the data/README_data.md file!

    **Note:** Processed data files (*.pkl) that are required as inputs for the Streamlit app are included for convenience. To fully reproduce or update these files, please run the preprocessing notebooks in the prescribed order.



