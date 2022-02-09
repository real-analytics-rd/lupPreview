# AUTOGENERATED! DO NOT EDIT! File to edit: 00_scraper.ipynb (unless otherwise specified).

__all__ = ['ScrapingTheGuardian']

# Cell
import pandas as pd
import dateparser
import random
import requests
import logging
from .Db_Config import *
from .parser import *
from .extractor import *
from .mapper import *
from .models.preview import *
from typing import Dict, Union
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

# Cell
class ScrapingTheGuardian:
    """
    A class to represent a scraper from the "Guardian" website.

    ...

    Attributes
    ----------
    session : requests_html.HTMLSession
        a web session
    VENUE_REGEX : str
        venue regex expression
    REFEREE_REGEX : str
        referee regex expression
    ODDS_REGEX : str
        odds regex expression

    Methods
    -------
    calculate_betting_odds(odds)
        returns decimal odds.
    extract_preview_items(content,link,preview_date,game_date,game_id,home_team,away_team)
        returns all information of a football preview.
    extract_previews(self,page,previews_last_date,last_preview,all_previews,df_teams)
        returns the information of all extracted previews.

    """

    # venue, referee, odds pattern regex
    # in some previews, all of the information is on the same line.
    VENUE_REGEX = "Venue(.*)Tickets|Venue(.*),|Venue(.*)"
    REFEREE_REGEX = "Referee(.*)This season's|Referee(.*)Last season's|Referee(.*)Odds|Referee[\s](.*)|Ref(.*)Odds"
    # {Odds H 11-8 A 11-8 D 11-8}
    # {Odds Liverpool 11-8 Aston Villa 11-8 Draw 11-8}
    # missing label {Odds H 11-8 11-8 D 11-8}
    # missing value {Odds H 11-8 A 11-8}
    ODDS_REGEX = "Odds[\s]*[a-zA-Z' ]*(\d{1,3}-[\s]*\d{1,3})[\s]*[a-zA-Z' ]*(\d{1,3}-[\s]*\d{1,3})([\s]*[a-zA-Z']*[\s]*(\d{1,3}-[\s]*\d{1,3}))*"

    def __init__(self):

        # Initialize session to start scraping
        self.session = HTMLSession()

    @staticmethod
    def calculate_betting_odds(odds: list) -> Dict[str, object]:
        """
          returns decimal odds.

        Parameters
        ----------
        odds: list of str
            odds values

        Returns
        -------
        betting_odds: dict of object

        """
        # Initialize betting odds to n/a (not available)
        # Some previews may not include odds
        odds_home = None
        odds_away = None
        odds_draw = None

        if odds is not None:  # If odds exist
            # example of odds:
            # {H 4-6 A 43-10 D 3-1}
            # {liverpool 4-6 Tottenham 43-10 Draw 3-1}
            # {H 4-6 43-10 D 3-1}
            # {H 4-6 A 43-10}
            # The formula will be (4/6)+1 , (43/10)+1 , (3/1)+1
            # Home team odds
            betting_odds_home = odds[0]
            try:
                odds_home = (
                    int(betting_odds_home.split("-")[0])
                    / int(betting_odds_home.split("-")[1])
                ) + 1
            except ZeroDivisionError:
                logging.error("Home team odds are wrong")
                pass
            # Away team odds
            betting_odds_away = odds[1]
            try:
                odds_away = (
                    int(betting_odds_away.split("-")[0])
                    / int(betting_odds_away.split("-")[1])
                ) + 1
            except ZeroDivisionError:
                logging.error("Away team odds are wrong")
                pass
            # if we have the normal format of odds
            # we will have 3 parts(odds_home,odds_away,odds_draw)
            if len(odds) >= 3:
                odds.pop(2)
                # Draw odds
                betting_odds_draw = odds[2]
                try:
                    odds_draw = (
                        int(betting_odds_draw.split("-")[0])
                        / int(betting_odds_draw.split("-")[1])
                    ) + 1
                except ZeroDivisionError:
                    logging.error("Draw odds are wrong")
                    pass

        betting_odds = dict(
            {"odds_home": odds_home, "odds_away": odds_away, "odds_draw": odds_draw}
        )
        return betting_odds

    @staticmethod
    def extract_preview_items(
        content: BeautifulSoup,
        link: str,
        preview_date: datetime,
        game_date: datetime,
        game_id: int,
        home_team: str,
        away_team: str,
        response_type: str,
    ) -> Dict[str, object]:
        """
          returns all information of a football preview

        Parameters
        ----------
        content: bs4.BeautifulSoup
            the html format of the preview content
        link: str
            the link of the preview
        preview_date: datetime
            the preview date
        game_date: datetime
            the game date
        game_id: int
            the game id
        home_team: str
            the home team name
        away_team: str
            the away team name
        response_type: str
            the parsing method('api' or 'html')

        Returns
        -------
        preview_items: dict of object

        """

        # meth1: extract match infos (venue,referee,odds)
        match_infos = PageExtractor.extract_match_infos(
            content,
            response_type,
            ScrapingTheGuardian.VENUE_REGEX,
            ScrapingTheGuardian.REFEREE_REGEX,
            ScrapingTheGuardian.ODDS_REGEX,
        )
        venue = match_infos["venue"]
        referee = match_infos["referee"]
        odds = match_infos["odds"]
        # meth2: extract text and author of the preview
        text_author = PageExtractor.extract_text_authors(content, response_type)
        text = text_author["text"]
        author = text_author["author"]
        # meth3: calculate betting odds
        betting_odds = ScrapingTheGuardian.calculate_betting_odds(odds)
        # Home team betting odds
        odds_home_team = betting_odds["odds_home"]
        # Away team betting odds
        odds_away_team = betting_odds["odds_away"]
        # Draw betting odds
        odds_draw = betting_odds["odds_draw"]
        # Return preview items
        preview_items = dict(
            {
                "game_id": game_id,
                "home_team": home_team,
                "away_team": away_team,
                "text": text,
                "author": author,
                "venue": venue,
                "referee": referee,
                "odds": odds,
                "odds_home_team": odds_home_team,
                "odds_away_team": odds_away_team,
                "odds_draw": odds_draw,
                "preview_date": preview_date,
                "game_date": game_date,
                "preview_link": link,
            }
        )
        return preview_items

    def extract_previews(
        self,
        page: BeautifulSoup,
        previews_last_date: datetime,
        last_preview: bool,
        all_previews: list,
        df_teams: pd.DataFrame,
    ) -> Union[bool, list]:
        """
          save all browsed previews in local

        Parameters
        ----------
        page: bs4.BeautifulSoup
            the html format of the page
        previews_last_date : datetime
            the last extracted preview date in the database
        last_preview: bool
            an indicator to know when we should stop the scraper
        all_previews: list
            a list that contains all extracted previews
        df_teams: pd.DataFrame
            a dataframe that contains teams and their different names

        Returns
        -------
        bool

        """
        # We pick all of the match previews on the webpage.
        previews = page.findAll("div", {"class": "fc-item__content"})
        # for each preview we extract its information.
        for preview in previews:
            # we pick the preview date and we parse it in a date format
            preview_date = preview.find("time")["datetime"]
            preview_date = dateparser.parse(preview_date, settings={"TIMEZONE": "UTC"})
            # if the date selected from the previews database exists
            # and has been reached by the preview date, we stop the loop
            # and mark last_preview as True.
            if previews_last_date and preview_date.date() <= previews_last_date.date():
                logging.info("The scraper turned off")
                last_preview = True
                break
            # Pick the preview link
            preview_link = preview.find("a")["href"]

            # We extract the last part of the link, which corresponds to the preview api link
            api_preview_url = preview_link.replace("https://www.theguardian.com", "")
            # request the api
            response = requests.get(
                "https://content.guardianapis.com/"
                + api_preview_url
                + "?api-key=fd4452e9-76a5-45a1-b30d-bdd156640b9c&show-blocks=all"
            )
            # if the api works we get the title and the content of the preview
            # else we extract html contents
            if response:
                logging.info("The Guardian Api works")
                # get the preview data
                data = response.json()
                # preview title
                preview_title = data["response"]["content"]["webTitle"]
                # preview content
                preview_content = BeautifulSoup(
                    data["response"]["content"]["blocks"]["body"][0]["bodyHtml"],
                    "html.parser",
                )
                # preview date
                preview_date = data["response"]["content"]["blocks"]["body"][0][
                    "createdDate"
                ]
                preview_date = dateparser.parse(
                    preview_date, settings={"TIMEZONE": "UTC"}
                )
                response_type = "api"

            else:
                logging.info("The Guardian Api does not work")
                preview_content = Parser.parse_page(preview_link, self.session)
                preview_title = preview_content.find("h1").text
                response_type = "html"

            # extract team names
            names = PageExtractor.extract_teams_names(preview_title)
            # Home team and  Away Team
            home_team = names["home"]
            away_team = names["away"]
            # get teams id
            home_team_id = PreviewsMapping.get_team_id(home_team, df_teams)
            away_team_id = PreviewsMapping.get_team_id(away_team, df_teams)
            # pick the preview date
            # get the id and the date of the game
            game = PreviewsMapping.get_game_id_date(
                home_team_id, away_team_id, preview_date
            )
            # if the game exists we extract the preview information
            if game != None:
                preview_infos = ScrapingTheGuardian.extract_preview_items(
                    preview_content,
                    preview_link,
                    preview_date,
                    game.gameDate,
                    game.gameId,
                    home_team,
                    away_team,
                    response_type,
                )
                logging.info("Returned Preview information: {}".format(preview_infos))
                # connect to database
                mongoengine_client = MongoClient.connect("1")
                # preview class
                preview = Previews(
                    gameId=preview_infos["game_id"],
                    homeTeam=preview_infos["home_team"],
                    awayTeam=preview_infos["away_team"],
                    text=preview_infos["text"],
                    author=preview_infos["author"],
                    venue=preview_infos["venue"],
                    referee=preview_infos["referee"],
                    odds=preview_infos["odds"],
                    oddsHomeTeam=preview_infos["odds_home_team"],
                    oddsAwayTeam=preview_infos["odds_away_team"],
                    oddsDraw=preview_infos["odds_draw"],
                    gameDate=preview_infos["game_date"],
                    previewDate=preview_infos["preview_date"],
                    previewLink=preview_infos["preview_link"],
                )
                # Validate and save input raw data
                MongoClient.save(preview)
                all_previews.append(preview_infos)

            else:
                logging.info("The game does not exist in the Opta database")


        return last_preview, all_previews