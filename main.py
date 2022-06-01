# Start of aggregating and evaluating datas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data


sns.set()

def top_rating_genres(amazon, disney, netflix):
    print(amazon)

def main():
    amazon_covid = covid_data("data/amazon_prime_titles.csv")
    disney_covid = covid_data("data/disney_plus_titles.csv")
    netflix_covid = covid_data("data/netflix_titles.csv")
    top_rating_genres(amazon_covid, disney_covid, netflix_covid)
    #sns.catplot(x="rating", kind="count", hue="rating", data=data)
    #plt.xlabel("rating", rotation="vertical")
    #plt.savefig("amazon_rating_plot")



if __name__ == '__main__':
    main()