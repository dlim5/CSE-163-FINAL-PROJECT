# Start of aggregating and evaluating datas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data


sns.set()

def netflix_top_rating_genres(data):
    netflix_covid = data[data["type"] == "Movie"]
    max_rating = netflix_covid.groupby("rating")["rating"].count().idxmax()
    data_highest_rating = netflix_covid[netflix_covid["rating"] == max_rating]
    genres = data_highest_rating["listed_in"].str.split(",")
    
    genre_dictionary = {}
    for movie in genres:
        for genre in movie:
            if genre not in genre_dictionary:
                genre_dictionary[genre] = 1
            else:
                genre_dictionary[genre] += 1
    keys = genre_dictionary.keys()
    values = genre_dictionary.values()
    plt.bar(keys, values)
    plt.gcf().autofmt_xdate()
    plt.show()


def main():
    # amazon_covid = covid_data("data/amazon_prime_titles.csv")
    # disney_covid = covid_data("data/disney_plus_titles.csv")
    netflix_covid = covid_data("data/netflix_titles.csv")
    netflix_top_rating_genres(netflix_covid)
    #sns.catplot(x="rating", kind="count", hue="rating", data=data)
    #plt.xlabel("rating", rotation="vertical")
    #plt.savefig("amazon_rating_plot")


if __name__ == '__main__':
    main()