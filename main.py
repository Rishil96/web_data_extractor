# Books Web Scrape

import bs4
import requests

# Generator
generate_integer = (x for x in range(1, 101))


# main logic
def main():
    is_scraping = True

    while is_scraping:

        books_url = f"http://books.toscrape.com/catalogue/page-{next(generate_integer)}.html"
        print(books_url)
        response = requests.get(books_url)

        try:
            response.raise_for_status()

        except requests.exceptions.HTTPError:
            print("No more pages left to scrape.")
            is_scraping = False
            continue

        # Start Scraping the Book Store


if __name__ == "__main__":
    main()
