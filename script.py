import argparse
import logging
import pandas as pd
import random
from time import sleep
from guardian_scraper.scraper import *
from guardian_scraper.parser import *
from guardian_scraper.Db_Config import *
from guardian_scraper.models.preview import *


def main(page, api_key, scraping_all):
    # store scraper actions in a log file
    logging.basicConfig(
        filename="scraper.log", level=logging.INFO, format="%(levelname)s:%(message)s"
    )
    # starting url
    url = "https://www.theguardian.com/football/series/match-previews?page=" + str(page)
    # initialize the scraper instance.
    scraper = ScrapingTheGuardian()
    # initially we are not at the last page.
    last_page = False
    # we'll extract the previews that haven't already been extracted.
    last_preview = False
    # last extracted preview date
    last_previews_date = None

    if scraping_all == None:
        # we specify the last preview date in the previews collection on which the scraper will be turned off.
        mongoengine_client = MongoClient.connect("1")
        previews_last_date = (
            Previews.objects().order_by("-previewDate", "-gameDate").first()
        )
        # if the database is empty we will scrap all pages
        if previews_last_date != None:
            last_previews_date = previews_last_date.previewDate

    logging.info(
        "The last preview date stored in the database is: {}".format(last_previews_date)
    )
    all_previews = []
    # charging teams dictionary
    df_teams = pd.read_csv(".//datasets//final_data.csv")
    # if we are not at the last page
    # and we haven't reached an extracted preview
    # we launch the scraper
    while not last_page and not last_preview:
        # a random timer
        time = random.randint(2, 60)
        logging.info("The scraper will wait {} seconds ...".format(time))
        logging.info("The scraper will open this url: {}".format(url))
        # wait time seconds
        sleep(time)
        # get the html format of the page containing previews
        page = Parser.parse_page(url, scraper.session)
        # launch the scraper , extract previews information
        last_preview, all_previews = scraper.extract_previews(
            page, last_previews_date, last_preview, all_previews, df_teams, api_key
        )
        # get the url of the following page and verify if we are at the last page
        url, last_page = Parser.get_next_page(page)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="The Guardian Scraper")
    parser.add_argument("page", metavar="page", type=int, help="Enter the page number")
    parser.add_argument(
        "api_key", metavar="api_key", type=str, help="Enter your Guardian api key"
    )
    parser.add_argument(
        "--scraping",
        metavar="scraping",
        type=str,
        choices=["all"],
        help="Ignore the last preview date in Opta Database and scrape all previews",
    )
    args = parser.parse_args()

    page = args.page
    api_key = args.api_key  # fd4452e9-76a5-45a1-b30d-bdd156640b9c
    scraping_all = args.scraping
    main(page, api_key, scraping_all)