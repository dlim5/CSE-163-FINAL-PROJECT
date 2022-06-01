import pandas as pd


def covid_data(file):
    """
    Filters 2019-2021 year(covid) for both movies and TV shows
    """
    data = pd.read_csv(file, index_col="date_added", parse_dates=True)
    data_covid = data.loc["2019":"2021"]
    return data_covid


def non_covid_data(file):
    """
    filters non-covid year for both movies and TV shows
    """
    data = pd.read_csv(file, index_col="date_added", parse_dates=True)
    data_non_covid = data.drop(data.loc["2019":"2021"].index)
    return data_non_covid


def main():
    pass


if __name__ == '__main__':
    main()