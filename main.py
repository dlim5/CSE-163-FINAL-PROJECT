# Start of aggregating and evaluating datas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data


sns.set()


def main():
    data = covid_data("data/amazon_prime_titles.csv")
    sns.catplot(x="rating", kind="count", hue="rating", data=data)
    plt.xlabel("rating", rotation="vertical")
    plt.savefig("amazon_rating_plot")



if __name__ == '__main__':
    main()