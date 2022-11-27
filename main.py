# Books Web Scrape

import bs4
import requests

# All books scraped from the site as articles
books_list = []
all_5_star_books = []
all_4_star_books = []

# Generator
generate_integer = (x for x in range(1, 101))


# Get books of specific rating
def get_books_by_rating(book_list, rating):
    """
    This function takes a list of beautiful soup book articles and returns the title
    of the books with the entered stars.
    :param book_list: a list of all scraped books
    :param rating: rating by which the books should be filtered
    :return: list of books with the specified rating
    """

    all_books = []

    for book in book_list:
        five_star_book = book.select_one(f"p.star-rating.{rating}")
        if five_star_book is not None:
            book_5_star = book.select_one("h3 a")
            all_books.append(book_5_star.get("title"))

    return all_books


# main logic
def main():
    is_scraping = True

    while is_scraping:

        books_url = f"http://books.toscrape.com/catalogue/page-{next(generate_integer)}.html"
        print("Scraping on: ", books_url)
        response = requests.get(books_url)

        try:
            response.raise_for_status()

        except requests.exceptions.HTTPError:
            print("No more pages left to scrape.")
            is_scraping = False
            continue

        # Start Scraping the Book Store
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        books_list.extend(soup.select(".product_pod"))

        break

    # After getting all books from the bookstore now filter the books using the stars
    for book in books_list:
        five_star_book = book.select_one("p.star-rating.Five")
        if five_star_book is not None:
            book_5_star = book.select_one("h3 a")
            print(book_5_star.get("title"))


if __name__ == "__main__":
    main()
