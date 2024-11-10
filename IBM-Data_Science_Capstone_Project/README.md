# IBM Data Science Capstone Project

This repository contains the final project for the IBM Data Science Specialization.

The goal of this project is to analyze and predict the success of SpaceX rocket launches using data science techniques. This includes everything from data collection and cleaning to interactive visualization and machine learning modeling.

## Project Structure

```
IBM-Data_Science_Capstone_Project/
├── data/                       # Data files used in the project
│   ├── 01_data_falcon9.csv
│   ├── 02_df.csv
│   ...                         # (list of other data files)
│   └── spacex_launch_geo.csv
├── plots/                      # Visualizations generated during analysis
│   ├── FlightNumberVsLaunchSite.png
│   ├── FlightNumberVSOrbitType.png
│   ...                         # (list of other plot files)
│   └── SuccessRateByOrbitType.png
├── 01_SpaceX_data_collection_api.ipynb              # Data collection via API
├── 02_SpaceX_data_collection_web_scraping.ipynb     # Data collection via web scraping
├── 03_SpaceX_Data_wrangling.ipynb                   # Data cleaning and wrangling
├── 04_SpaceX_eda_sql.ipynb                          # Exploratory Data Analysis with SQL
├── 05_SpaceX_eda_dataviz.ipynb                      # Exploratory Data Analysis with visualization
├── 06_SpaceX_interactive_visual_analitics_with_folium.ipynb   # Interactive visual analysis
├── 07_SpaceX_dash_app.py                            # Interactive dashboard with Dash
├── 08_SpaceX_Machine_Learning_Prediction.ipynb      # Machine learning model for predictions
└── Winning_Space_Race_With_Data_Science.pptx        # Project presentation
````

### Main Files Description

    data/: Contains all data files used in the project, including original datasets, processed data, and SQLite databases.
    plots/: Folder for storing visualizations created during analysis and modeling.
    Notebooks:
        01_SpaceX_data_collection_api.ipynb: Retrieves SpaceX data via API.
        02_SpaceX_data_collection_web_scraping.ipynb: Gathers SpaceX data through web scraping.
        03_SpaceX_Data_wrangling.ipynb: Data cleaning and preparation for analysis.
        04_SpaceX_eda_sql.ipynb: Exploratory Data Analysis (EDA) using SQL queries.
        05_SpaceX_eda_dataviz.ipynb: EDA with visualizations.
        06_SpaceX_interactive_visual_analitics_with_folium.ipynb: Interactive mapping analysis using Folium.
        08_SpaceX_Machine_Learning_Prediction.ipynb: Machine learning modeling and prediction.
    07_SpaceX_dash_app.py: Script for an interactive dashboard built with Plotly Dash.
    Winning_Space_Race_With_Data_Science.pptx: Project presentation summarizing processes and findings.

### Requirements

To run the notebooks and scripts in this project, the following libraries are needed:

    pandas
    numpy
    plotly
    dash
    sqlite3
    folium
    scikit-learn

Install these libraries with:

```Bash
pip install -r requirements.txt
```

### Execution Instructions

    Data Collection and Cleaning: Run the data collection and cleaning notebooks (01_ and 02_) to generate the required datasets in the data folder.
    Exploratory Data Analysis (EDA): Execute the EDA notebooks (04_ and 05_) to analyze and visualize the data.
    Interactive Mapping Analysis: Use 06_SpaceX_interactive_visual_analitics_with_folium.ipynb for interactive mapping analysis.
    Interactive Dashboard: Run 07_SpaceX_dash_app.py to launch the interactive dashboard.
    Machine Learning Prediction: Use 08_SpaceX_Machine_Learning_Prediction.ipynb for machine learning model predictions.

Results

This project analyzes SpaceX's success rates and creates predictive models for future mission outcomes. Insights obtained are visualized through the interactive dashboard application and summarized in the Winning_Space_Race_With_Data_Science.pptx presentation.

Author
Roberto Baladrón Pardo
This project was completed as part of the IBM Data Science Specialization.