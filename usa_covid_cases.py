def usa_covid_data():
    """

    Overview:
    ---------
    Downloads the USA COVID data directly from John Hopkins CSSEGISandData.
    This function merges all data from most current date to earliest date (2020-4-11) available in the repo.
    Using this function a user can conduct time series analysis on how COVID cases change in various states.

    Output:
    -------
    One uncleaned .csv file called "usa_covid_cases.csv"

    """
    from datetime import datetime, timedelta
    import pandas as pd

    # Set starting index
    i = 1

    # Earliest dataset available on GitHub
    start_date = datetime.strptime('2020-4-11', '%Y-%m-%d').date()

    # Pulling today's date minus 1 day due to delay posting on GitHub
    today = datetime.now().date() - timedelta(days=i)

    # Setting llist to store dataframe file names
    file_names = []

    # Looping until date is equal to earlist date = Start Date
    while not (start_date.day == today.day and start_date.month == today.month and start_date.year == today.year):

        # Extracting variables from current date
        day = today.day
        month = today.month
        year = today.year

        # Cleaning and converting values for formatting on GitHub URL link
        if day < 10:
            day = '0' + str(day)

        if month < 10:
            month = '0' + str(month)

        # Setting variable for each url
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}-{}-{}.csv'\
                    .format(month, day, str(year))

        # Reading each url as a datafra,
        df = pd.read_csv(url, error_bad_lines=False)

        # Saving each dataframe into the empty list
        file_names.append(df)

        # Increasing the index by 1
        i += 1

        # Subtracting the new index to increase 1 less day from the current date
        today = datetime.now().date() - timedelta(days=i)

    # Once while loop ends - concat all the files into a single dataframe
    new_df = pd.concat(file_names)

    new_df.to_csv('~/files_airflow/usa_covid_cases.csv', index=False)
