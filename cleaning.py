import pandas as pd


def main():
    netflix = pd.read_csv('data/netflix_titles.csv')
    disney = pd.read_csv('data/disney_plus_titles.csv')
    amazon = pd.read_csv('data/amazon_prime_titles.csv')
    print(disney)


if __name__ == '__main__':
    main()