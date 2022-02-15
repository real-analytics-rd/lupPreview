import argparse
import logging
import random
import dateparser
import sys
import os
import pandas as pd
from time import sleep
package_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(package_dir))
from guardian_scraper.scraper import *
from guardian_scraper.parser import *
from guardian_scraper.Db_Config import *
from guardian_scraper.models.preview import *


def load_file(file_path):
    # charging the file content in a dataframe
    df = pd.read_csv(file_path)
    return df


def main(page, api_key, scraping_all, file_path):

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
    # if the argument is not "all"
    if scraping_all == None:
        # we specify the last preview date in the previews collection on which the scraper will be turned off.
        mongoengine_client = MongoClient.connect("1")
        previews_last_date = (
            Previews.objects().order_by("-previewDate", "-gameDate").first()
        )
        # if the database is empty we will scrap all pages
        if previews_last_date != None:
            last_previews_date = previews_last_date.previewDate

    logging.info("The scraper started: {}".format(dateparser.parse("now")))
    logging.info(
        "The last preview date stored in the database is: {}".format(last_previews_date)
    )
    # charging english teams file which contains teams and their different names
    df_teams = load_file(file_path)
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
            page, last_previews_date, last_preview, df_teams, api_key
        )
        # get the url of the following page and verify if we are at the last page
        url, last_page = Parser.get_next_page(page)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="The Guardian Scraper")
    parser.add_argument(
        "--page", metavar="page", type=int, default=1, help="Enter the page number"
    )
    parser.add_argument(
        "--api_key",
        metavar="api_key",
        type=str,
        default="fd4452e9-76a5-45a1-b30d-bdd156640b9c",
        help="Enter your Guardian api key",
    )
    parser.add_argument(
        "--scraping",
        metavar="scraping",
        type=str,
        default=None,
        choices=["all"],
        help="Ignore the last preview date in Opta Database and scrape all previews",
    )
    parser.add_argument(
        "--file_path",
        metavar="file_path",
        type=str,
        default="..//teams_mapping_datasets//english_teams.csv",
        help="Enter the path of the teams mapping file",
    )
    args = parser.parse_args()
    # page number input
    page = args.page
    # api key input
    api_key = args.api_key
    # scraping method input
    scraping_all = args.scraping
    # teams mapping file path
    file_path = args.file_path
    # store scraper actions in a log file
    logging.basicConfig(
        filename="..//logs//scraper.log",
        level=logging.INFO,
        format="%(levelname)s:%(message)s",
    )
    # launch the scraper
    main(page, api_key, scraping_all, file_path)