import pandas as pd


def covid_data(file):
    data = pd.read_csv(file)
    data_covid = data[
        (data["date_added"] >= 2019) & (data["date_added"] <= 2021)]
    return data_covid


def non_covid_data(file):
    data = pd.read_csv(file)
    data_non_covid = data[(data["date_added"] != 2019) & (
        data["date_added"] != 2020) & (
            data["date_added"] != 2021)]
    return data_non_covid


def main():
    pass


if __name__ == '__main__':
    main()