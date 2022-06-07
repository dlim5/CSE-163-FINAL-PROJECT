"""
Jason Lim
Jasmine Mae Alindayu
CSE 163

This file contains all of the functions that analyzes
the data sets of the three streaming services: Netflix,
Disney+ and Amazon Prime Video. The functions also
produce visualizations for each of the research
questions of our project.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import covid_data, non_covid_data, read_file
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

def top_rating_genres(data):
    """
    Takes in a data set of a streaming service
    with information during COVID-19 (2019 - 2021).
    The function then filters out the data set
    for movies and returns a dictionary of the
    most popular rating for movies in the
    given streaming platform.
    """
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
    """
    Takes in the pre-computed dictionary from the
    top_rating_genres function. Returns a bar graph
    visualization of the different genres associated
    with the most popular rating of movies on Netflix.
    """
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Netflix Genre Comparison During Covid for TV-MA Movie Rating")
    plt.savefig("netflix_genre_comparison.png")
    plt.close()


def disney_genre_plot(dic):
    """
    Takes in the pre-computed dictionary from the
    top_rating_genres function. Returns a bar graph
    visualization of the different genres associated
    with the most popular rating of movies on Disney+.
    """
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Disney Genre Comparison During Covid for G Movie Rating")
    plt.savefig("disney_genre_comparison.png")
    plt.close()


def amazon_genre_plot(dic):
    """
    Takes in the pre-computed dictionary from the
    top_rating_genres function. Returns a bar graph
    visualization of the different genres associated
    with the most popular rating of movies on
    Amazon Prime Video.
    """
    keys = dic.keys()
    values = dic.values()
    plt.bar(keys, values)
    plt.xticks(fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.title("Amazon Genre Comparison During Covid for 13+ Movie Rating")
    plt.savefig("amazon_genre_comparison.png")
    plt.close()


def netflix_years(data):
    """
    Takes in a time series data set for Netflix and
    returns a line graph visualization that represents
    the trend of added TV shows and movies on Netflix
    over time. The graph also illustrates the release
    years of the TV shows and movies.
    """
    data.plot()
    plt.title("Trend of Added TV Shows & Movies on Netflix Over Time With"
              " Release Year")
    plt.show()
    plt.close()


def disney_years(data):
    """
    Takes in a time series data set for Disney+ and
    returns a line graph visualization that represents
    the trend of added TV shows and movies on Netflix
    over time. The graph also illustrates the release
    years of the TV shows and movies.
    """
    data.plot()
    plt.title("Trend of Added TV Shows & Movies on Disney+ Over Time With"
              " Release Year")
    plt.show()
    plt.close()


def amazon_years(data):
    """
    Takes in a time series data set for Amazon Prime Video
    and returns a line graph visualization that represents
    the trend of added TV shows and movies on Netflix
    over time. The graph also illustrates the release
    years of the TV shows and movies.
    """
    data.plot()
    plt.title("Trend of Added TV Shows & Movies on Amazon Prime Video Over"
              " Time With Release Year")
    plt.show()
    plt.close()


def netflix_statistical_analysis(data):
    """
    "ETS(Error/Trend/Seasonality) Model"
    """
    filtered_data = data.groupby(pd.Grouper(freq="Y"))["title"]
    count = filtered_data.count()
    count_df = count.to_frame()
    result_add = seasonal_decompose(count_df["title"], model="add")
    result_add.plot()
    plt.savefig("netflix_analysis.png")
    plt.close()


def disney_compare_implement_foreign(data):
    """
    Takes in a data set of a streaming service
    with information during COVID-19 (2019 - 2021).
    This function then drops all the missing values
    and filters the data to produce a pie chart to represent
    all the TV shows and movies added in Disney+
    that were produced outside of the United States.
    """
    data = data.dropna(subset=["country"])
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie", autopct='%1.2f%%', shadow=True)
    plt.title("Proportion of Added Foreign Movie/TV show in Disney Per Year")
    plt.savefig("disney_foreign_implementation.png")
    plt.close()


def netflix_compare_implement_foreign(data):
    """
    Takes in a data set of a streaming service
    with information during COVID-19 (2019 - 2021).
    This function then drops all the missing values
    and filters the data to produce a pie chart to represent
    all the TV shows and movies added in Netflix
    that were produced outside of the United States.
    """
    data = data.dropna(subset=["country"])
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie", autopct='%1.2f%%', shadow=True)
    plt.title("Proportion of Added Foreign Movie/TV show in Netflix Per Year")
    plt.savefig("netflix_foreign_implementation.png")
    plt.close()


def amazon_compare_implement_foreign(data):
    """
    Takes in a data set of a streaming service
    with information during COVID-19 (2019 - 2021).
    This function then drops all the missing values
    and filters the data to produce a pie chart to represent
    all the TV shows and movies added in Amazon Prime Video
    that were produced outside of the United States.
    """
    data = data.dropna(subset=["country"])
    filter_country = ["United States"]
    filtered_data = data[~data.country.isin(filter_country)]
    filtered_data = filtered_data.groupby(pd.Grouper(freq="Y"))
    result_df = filtered_data["country"].count()
    result_df.plot(kind="pie", autopct='%1.2f%%', shadow=True)
    plt.title("Proportion of Added Foreign Movie/TV show in Amazon"
              " Prime Per Year")
    plt.savefig("amazon_foreign_implementation.png")
    plt.close()


def main():
    # Data
    NETFLIX = "data/netflix_titles.csv"
    DISNEY = "data/disney_plus_titles.csv"
    AMAZON = "data/amazon_prime_titles.csv"
    # Q1
    # disney_covid = covid_data(DISNEY)
    # disney_genres = top_rating_genres(disney_covid)
    # disney_genre_plot(disney_genres)
    # netflix_covid = covid_data(NETFLIX)
    # netflix_genres = top_rating_genres(netflix_covid)
    # netflix_genre_plot(netflix_genres)
    # amazon_covid = covid_data(AMAZON)
    # amazon_genres = top_rating_genres(amazon_covid)
    # amazon_genre_plot(amazon_genres)
    # # Q2
    # netflix_years(read_file(NETFLIX))
    # disney_years(read_file(DISNEY))
    # amazon_years(read_file(AMAZON))
    netflix_statistical_analysis(read_file(NETFLIX))
    # Q3
    # disney_compare_implement_foreign(read_file(DISNEY))
    # netflix_compare_implement_foreign(read_file(NETFLIX))
    # amazon_compare_implement_foreign(read_file(AMAZON))


if __name__ == '__main__':
    main()
