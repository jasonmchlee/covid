# COVID Resources
This repo contains two functions that pulls data from websites, then cleans and formats the data into multiple csv files to be used for analysis. Csv files are only updated whenever I push from my local machine into this repository.

### World Data
The function `world_covid_data()` from the file [`covid_datasets.py`](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_datasets.py) pulls in all the available data from the [World Health Organization - WHO](https://covid19.who.int/WHO-COVID-19-global-data.csv). It creates multiple pivoted csv files to analysis country specific metrics.
  - [new daily cases](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_report_New_cases.csv)
  - [new daily deaths](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_report_New_deaths.csv)
  - [cumulative cases](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_report_Cumulative_cases.csv)
  - [cumulative deaths](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_report_Cumulative_deaths.csv)
  - [moving average mortality rate](https://github.com/jasonmchlee/covid/blob/covid_branch/covid_report_Mortality_rate.csv)

### USA Data
The function `usa_covid_data()` from the file [`usa_covid_cases.py`](https://github.com/jasonmchlee/covid/blob/covid_branch/usa_covid_cases.py) pulls in all the available data from the [John Hopkins CSSEGISandData repository](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us) and saves output into this [file](https://github.com/jasonmchlee/covid/blob/covid_branch/usa_covid_cases.csv).

The function merges all the data into a single csv file, iterating over each available csv in the original repo. The final output csv is useful to conduct timeseries analysis and to understand how covid cases in the US have changed since April.

### DAG File
The file `covid_DAG.py` is an DAG ([Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)), I use in [Apace Airflow](https://airflow.apache.org/). The DAG runs daily on my local machine to automatically generate the most up to date merged dat using both the functions discussed.

### Dashboard
After extracting the dataset, the results from the World Data function are piped into Tableau for visualization. You can view the [Tableau dashboard](https://public.tableau.com/profile/jasonmchlee#!/vizhome/COVID-19_15853665003940/CovidDashboard?publish=yes) here.
