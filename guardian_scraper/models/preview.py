# AUTOGENERATED! DO NOT EDIT! File to edit: 05_DataStruct_Previews.ipynb (unless otherwise specified).

__all__ = ['Previews']

# Cell
from mongoengine import Document
from mongoengine import IntField
from mongoengine import FloatField
from mongoengine import StringField
from mongoengine import DateTimeField
from mongoengine import ListField

# Cell
class Previews(Document):
    """
        A class to represent the extracted previews from the guardian.

    ...

    Attributes
    ----------
    gameId : int
        the opta game id
    homeTeam : str
        home team name
    awayTeam : str
        away_team name
    text : str
        preview text
    author : str
        preview author
    venue : str
        match venue
    referee : str
        match referee
    odds : str
        betting odds
    oddsHomeTeam : float
        decimal betting odds for home team
    oddsAwayTeam : float
        decimal betting odds for away team
    oddsDraw : float
        decimal betting odds for draw
    gameDate : datetime
        the date of the match
    previewDate : datetime
        the date of the preview
    previewLink : str
        the Guardian preview link

    """

    gameId = IntField(db_field="gameId", required=True)
    homeTeam = StringField(db_field="homeTeam", required=True)
    awayTeam = StringField(db_field="awayTeam", required=True)
    text = StringField(db_field="text", required=False)
    author = StringField(db_field="author", required=False)
    venue = StringField(db_field="venue", required=False)
    referee = StringField(db_field="referee", required=False)
    #odds = StringField(db_field="odds", required=False)
    odds=ListField(StringField(),db_field="odds",required=False)
    oddsHomeTeam = FloatField(db_field="oddsHomeTeam", required=False)
    oddsAwayTeam = FloatField(db_field="oddsAwayTeam", required=False)
    oddsDraw = FloatField(db_field="oddsDraw", required=False)
    gameDate = DateTimeField(db_field="gameDate", required=False)
    previewDate = DateTimeField(db_field="previewDate", required=False)
    previewLink = StringField(db_field="previewLink", required=True)