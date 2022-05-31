import pandas as pd


def main():
    data = pd.read_csv('data/netflix_titles.csv')
    print(data)


if __name__ == '__main__':
    main()