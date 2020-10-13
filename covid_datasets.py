#!/usr/bin/env python
# coding: utf-8

# In[65]:
import pandas as pd
import datetime

def world_covid_data():


    # Reading URL
    url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    df = pd.read_csv(url)

    # Converting to datetime
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])

    # Cleaning column names for trailing white spaces
    cols = []
    for col in df.columns:
        cols.append(col.strip())

    df.columns = cols

    # New col and filling for 0 values
    df['Mortality_rate'] = ((df['Cumulative_deaths']/df['Cumulative_cases'])*100).round(2).fillna(0)


    # Saving .csvs
    columns = ['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths', 'Mortality_rate']

    for col in columns:
        dfs = df.pivot_table(index = 'Country', columns = 'Date_reported', values = col)
        dfs.to_csv('~/files_airflow/covid_report_{0}.csv'.format(col))


# In[ ]:
