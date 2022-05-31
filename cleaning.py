import pandas as pd


def main():
    netflix = pd.read_csv('data/netflix_titles.csv')
    netflix_covid = netflix[
        (netflix["release_year"] >= 2019) & (netflix["release_year"] <= 2021)]
    netflix_non_covid = netflix[
        (netflix["release_year"] != 2019) & (
            netflix["release_year"] != 2020) & (
                netflix["release_year"] != 2021)]
    disney = pd.read_csv('data/disney_plus_titles.csv')
    disney_covid = disney[
        (disney["release_year"] >= 2019) & (disney["release_year"] <= 2021)]
    disney_non_covid = disney[
        (disney["release_year"] != 2019) & (
            disney["release_year"] != 2020) & (
                disney["release_year"] != 2021)]
    amazon = pd.read_csv('data/amazon_prime_titles.csv')
    amazon_covid = amazon[
        (amazon["release_year"] >= 2019) & (amazon["release_year"] <= 2021)]
    amazon_non_covid = amazon[
        (amazon["release_year"] != 2019) & (
            amazon["release_year"] != 2020) & (
                amazon["release_year"] != 2021)]
    
    print(netflix_non_covid)


if __name__ == '__main__':
    main()