# COVID Resources

This repo contains a function `covid_data()` in the file `covid_cases.py`. In this function it pulls in all the available data from the [John Hopkins CSSEGISandData repository](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us).

The function merges all the data into a single csv file, iterating over each available csv in the original repo. The final output csv is useful to conduct timeseries analysis and to understand how covid cases in the US have changed since April.

The second file `covid_DAG.py` is an DAG ([Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)), I use in [Apace Airflow](https://airflow.apache.org/). The DAG runs daily on my local machine to automatically generate the most up to date merged data.

After extracting the dataset, the results are piped into Tableau for visualization. You can view the [dashboard](https://public.tableau.com/profile/jasonmchlee#!/vizhome/COVID-19_15853665003940/CovidDashboard?publish=yes) here.
