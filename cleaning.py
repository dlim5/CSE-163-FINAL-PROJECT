import pandas as pd


def covid_data(file):
    data = pd.read_csv(file)
    data_covid = data[
        (data["release_year"] >= 2019) & (data["release_year"] <= 2021)]
    return data_covid


def non_covid_data(file):
    data = pd.read_csv(file)
    data_non_covid = data[(data["release_year"] != 2019) & (
        data["release_year"] != 2020) & (
            data["release_year"] != 2021)]
    return data_non_covid


def main():
    pass


if __name__ == '__main__':
    main()