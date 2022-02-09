# AUTOGENERATED! DO NOT EDIT! File to edit: 01_parser.ipynb (unless otherwise specified).

__all__ = ['Parser']

# Cell
import logging
from typing import Tuple
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Cell
class Parser:
    """
    A class to represent previews pages parser.

    ...

    Methods
    -------
    parse_page(page_url, session)
        returns the html format of the page.
    get_next_page(page)
        returns the link of the following page and if it's the last page.
    """

    @staticmethod
    def parse_page(page_url: str, session: HTMLSession) -> BeautifulSoup:
        """
            returns the html format of the page.

        Parameters
        ----------
        page_url: str
            the url of the page
        session: requests_html.HTMLSession
            the scraper session

        Returns
        -------
        page: bs4.BeautifulSoup
              the html format of the page

        """
        try:
            # Request the url
            request = session.get(page_url)
            # Get the html document of the page
            page = BeautifulSoup(request.text, "html.parser")
            return page
        except Exception as e:
            logging.error("We cannot parse the specified page")

    @staticmethod
    def get_next_page(page: BeautifulSoup) -> Tuple[str, bool]:
        """
            returns the link of the following page and if it's the last page.

        Parameters
        ----------
        page : bs4.BeautifulSoup
            the html format of the page

        Returns
        -------
        url: str
          the url of the next page
        last_page: bool
          True if it's the last page, False otherwise.

        """
        # If we are at the last page , last_page = True else last_page = False
        last_page = False
        # Pick up the pagination HTML part
        pagination_section = page.find("div", {"class": "pagination__list"})
        # If we don't find the "next" button (it's the last page)
        # We are in the last page
        if not page.find("a", {"rel": "next"}):
            # We pick up the number of the page and we return the link
            html_location = dict({"aria-label": "Current page"})
            page_number = page.find("span", html_location).text
            url = (
                "https://www.theguardian.com/football/series/match-previews?page="
                + page_number
            )
            last_page = True
            logging.info("The Guardian last page")
            return url, last_page
        # If it's not the last page, we pick up the link of the following page
        else:
            url = page.find("a", {"rel": "next"})["href"]
            return url, last_page