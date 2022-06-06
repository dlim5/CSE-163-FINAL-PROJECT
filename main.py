# Start of aggregating and evaluating datas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data, read_file


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
    plt.title("Netflix Genre Comparison During Covid for TV-MA Movie Rating")
    plt.savefig("netflix_genre_comparison.png")
    plt.close()


def disney_genre_plot(dic):
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Disney Genre Comparison During Covid for G Movie Rating")
    plt.savefig("disney_genre_comparison.png")
    plt.close()
    

def amazon_genre_plot(dic):
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Amazon Genre Comparison During Covid for 13+ Movie Rating")
    plt.savefig("amazon_genre_comparison.png")
    plt.close()


def netflix_years(data):
    pass


def disney_years(data):
    data.plot()
    plt.show()
    plt.close()


def amazon_years(data):
    pass


def disney_compare_implement_foreign(data):
    data = data.dropna(subset=["country"])  
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie")
    plt.title("Proportion of Added Foreign Movie/TV show in Disney Per Year")
    plt.savefig("disney_foreign_implementation.png")
    plt.close()


def netflix_compare_implement_foreign(data):
    data = data.dropna(subset=["country"])
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie")
    plt.title("Proportion of Added Foreign Movie/TV show in Netflix Per Year")
    plt.savefig("netflix_foreign_implementation.png")
    plt.close()


def amazon_compare_implement_foreign(data):
    data = data.dropna(subset=["country"])
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie")
    plt.title("Proportion of Added Foreign Movie/TV show in Amazon Prime Per Year")
    plt.savefig("amazon_foreign_implementation.png")
    plt.close()


def main():
    # Data
    NETFLIX = "data/netflix_titles.csv"
    DISNEY = "data/disney_plus_titles.csv"
    AMAZON = "data/amazon_prime_titles.csv"
    # Q1
    disney_covid = covid_data(DISNEY)
    disney_genres = top_rating_genres(disney_covid)
    disney_genre_plot(disney_genres)
    netflix_covid = covid_data(NETFLIX)
    netflix_genres = top_rating_genres(netflix_covid)
    netflix_genre_plot(netflix_genres)
    amazon_covid = covid_data(AMAZON)
    amazon_genres = top_rating_genres(amazon_covid)
    amazon_genre_plot(amazon_genres)
    # Q2
    netflix_years(netflix_covid)
    disney_years(disney_covid)
    # Q3
    disney_compare_implement_foreign(read_file(DISNEY))
    netflix_compare_implement_foreign(read_file(NETFLIX))
    amazon_compare_implement_foreign(read_file(AMAZON))

if __name__ == '__main__':
    main()