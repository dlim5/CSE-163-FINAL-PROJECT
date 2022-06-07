"""
Jason Lim
Jasmine Mae Alindayu
CSE 163

This file has functions that pre-computes and cleans
the data sets for three streaming services: Netflix,
Disney+ and Amazon Prime Video.
"""
import pandas as pd


def covid_data(file):
    """
    Filters for the years 2019-2021 (COVUD-19) for both movies and TV shows
    and produces a time series data set.
    """
    data = pd.read_csv(file, index_col="date_added", parse_dates=True)
    data_covid = data.loc["2019":"2021"]
    return data_covid


def non_covid_data(file):
    """
    Filters non-covid years for both movies and TV shows and produces
    a time series data set.
    """
    data = pd.read_csv(file, index_col="date_added", parse_dates=True)
    data_non_covid = data.drop(data.loc["2019":"2021"].index)
    return data_non_covid


def read_file(file):
    """
    Reads the entire file and produces a time series data set.
    """
    data = pd.read_csv(file, index_col="date_added", parse_dates=True)
    return data


def main():
    pass


if __name__ == '__main__':
    main()
