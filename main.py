# Start of aggregating and evaluating datas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data


def top_rating_genres(data):
    data_covid = data[data["type"] == "Movie"]
    max_rating = data_covid.groupby("rating")["rating"].count().idxmax()
    data_highest_rating = data_covid[data_covid["rating"] == max_rating]
    genres = data_highest_rating["listed_in"].str.split(",")
    genre_dictionary = {}
    for movie in genres:
        for genre in movie:
            if genre not in genre_dictionary:
                genre_dictionary[genre] = 1
            else:
                genre_dictionary[genre] += 1
    return genre_dictionary


def netflix_genre_plot(dic):
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Netflix Genre Comparison During Covid")
    plt.savefig("netflix_genre_comparison.png")
    plt.close()


def disney_genre_plot(dic):
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Disney Genre Comparison During Covid")
    plt.savefig("disney_genre_comparison.png")
    plt.close()
    

def amazon_genre_plot(dic):
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Amazon Genre Comparison During Covid")
    plt.savefig("amazon_genre_comparison.png")
    plt.close()


def compare_implement_foreign(data_covid, data_non_covid):
    data_covid = data_covid.dropna(subset=["country"])
    data_non_covid = data_non_covid.dropna(subset=["country"])
    countries = data_covid["country"].str.split(",")
    for i in countries:
        if len(i) > 1:
            data_covid["country"] = data_covid["country"].replace(i, "Foreign")
        #     for j in i:
        #         if j == "United States":
        #             data_covid["country"] = data_covid["country"].replace(i, "Domestic")
        #         else:
        #             data_covid["country"] = data_covid["country"].replace(i, "Foreign")
        # elif len(i) > 1:
        #     data_covid["country"] = data_covid["country"].replace(i, "Foreign")
    print(data_covid["country"])




def main():
    # Q1
    disney_covid = covid_data("data/disney_plus_titles.csv")
    disney_genres = top_rating_genres(disney_covid)
    disney_genre_plot(disney_genres)
    netflix_covid = covid_data("data/netflix_titles.csv")
    netflix_genres = top_rating_genres(netflix_covid)
    netflix_genre_plot(netflix_genres)
    amazon_covid = covid_data("data/amazon_prime_titles.csv")
    amazon_genres = top_rating_genres(amazon_covid)
    amazon_genre_plot(amazon_genres)
    # Q3
    disney_non_covid = non_covid_data("data/disney_plus_titles.csv")
    compare_implement_foreign(disney_covid, disney_non_covid)

if __name__ == '__main__':
    main()