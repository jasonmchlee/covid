#!/usr/bin/env python
# coding: utf-8

# In[65]:
import pandas as pd
import datetime



# Read data from WHO website
def covid_data():

    url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    df = pd.read_csv(url)
    df.to_csv('~/files_airflow/WHO-COVID-19-global-data.csv')




# Converting tables into pivot tables
def covid_pivots():

    # Reading URL
    file = '~/files_airflow/WHO-COVID-19-global-data.csv'
    df = pd.read_csv(file)

    # Converting to datetime
    df['Date_reported'] = pd.to_datetime(df['Date_reported']).dt.date.astype('datetime64')

    # Cleaning column names for trailing white spaces
    cols = []
    for col in df.columns:
        cols.append(col.strip().lower())

    df.columns = cols

    # New col and filling for 0 values
    df['mortality_rate'] = ((df['cumulative_deaths']/df['cumulative_cases'])*100).round(2).fillna(0)


    # Saving .csvs
    columns = ['new_cases', 'cumulative_cases', 'new_deaths', 'cumulative_deaths', 'mortality_rate']

    for col in columns:
        dfs = df.pivot_table(index = 'country', columns = 'date_reported', values = col)
        dfs.to_csv('~/files_airflow/covid_report_{0}.csv'.format(col))




# Dataset for most current data case, deaths and mortality_rate
def mortality_data():

    file = '~/files_airflow/WHO-COVID-19-global-data.csv'
    df = pd.read_csv(file)

    # Remove unwated column
    for col in df.columns:
        if col == 'Unnamed: 0':
            df.drop('Unnamed: 0', axis = 1, inplace = True)

    # Clean column name
    cols = []

    for col in df.columns:
        clean = col.strip().lower()
        cols.append(clean)

    df.columns = cols

    # Convert to datetime
    df['date_reported'] = pd.to_datetime(df['date_reported']).dt.date.astype('datetime64')

    # Recent data
    recent_date = max(df['date_reported'].dt.date)
    recent_data = df[df['date_reported'] == recent_date].reset_index(drop = True)

    # Saving relevant_data
    cols = ['country', 'cumulative_cases', 'cumulative_deaths']
    relevant_data = recent_data.loc[:, cols]
    relevant_data['mortality_rate'] = ((relevant_data['cumulative_deaths']/relevant_data['cumulative_cases']) * 100).round(2).fillna(0)
    mortality_rate_data = relevant_data.sort_values('mortality_rate', ascending = False).reset_index(drop = True)

    mortality_rate_data.to_csv('~/files_airflow/mortality_rate_data.csv')
