
# Scraping The Guardian
> scraping Premier League previews from the Guardian.


.

## Install

`pip install TheGuardianScraper`

## How to use

Use case

```
page_link = "https://www.theguardian.com/football/series/match-previews"
scraper = ScrapingTheGuardian()
previews_infos=[]
page = Parser.parse_page(page_link,scraper.session)
previews_infos = scraper.extract_previews(page)
```

```
pd.DataFrame(previews_infos)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>home_team</th>
      <th>away_team</th>
      <th>text</th>
      <th>author</th>
      <th>venue</th>
      <th>referee</th>
      <th>odds</th>
      <th>odds_home_team</th>
      <th>odds_away_team</th>
      <th>odds_draw</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Leeds</td>
      <td>Newcastle</td>
      <td>Can Eddie Howe choreograph Newcastle’s second ...</td>
      <td>Louise Taylor</td>
      <td>Elland Road</td>
      <td>Chris Kavanagh</td>
      <td>(1-1, 3-1, 5-2)</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>3.500000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tottenham</td>
      <td>Arsenal</td>
      <td>For the first time in a while more than just b...</td>
      <td>Stephen Hollis</td>
      <td>Tottenham Hotspur Stadium</td>
      <td>Chris Kavanagh</td>
      <td>(8-5, 2-1, 12-5)</td>
      <td>2.600000</td>
      <td>3.000000</td>
      <td>3.400000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Liverpool</td>
      <td>Brentford</td>
      <td>Albert Stubbins, the only footballer to featur...</td>
      <td>Andy Hunter</td>
      <td>Anfield</td>
      <td>Jon Moss</td>
      <td>(1-3, 21-2, 5-1)</td>
      <td>1.333333</td>
      <td>11.500000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Ham</td>
      <td>Leeds</td>
      <td>West Ham regained fourth place by beating Norw...</td>
      <td>Jacob Steinberg</td>
      <td>London Stadium</td>
      <td>Mike Dean</td>
      <td>(4-6, 43-10, 3-1)</td>
      <td>1.666667</td>
      <td>5.300000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Newcastle</td>
      <td>Watford</td>
      <td>Moussa Sissoko returns to Newcastle in Watford...</td>
      <td>Louise Taylor</td>
      <td>St James’ Park</td>
      <td>Paul Tierney</td>
      <td>(19-17, 27-10, 27-10)</td>
      <td>2.117647</td>
      <td>3.700000</td>
      <td>3.700000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Manchester City</td>
      <td>Chelsea</td>
      <td>Manchester City would surely finish off Chelse...</td>
      <td>Jamie Jackson</td>
      <td>Etihad Stadium</td>
      <td>Craig Pawson</td>
      <td>(8-11, 22-5, 3-1)</td>
      <td>1.727273</td>
      <td>5.400000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Aston Villa</td>
      <td>Manchester United</td>
      <td>The extent of the problems Ralf Rangnick has i...</td>
      <td>Stephen Hollis</td>
      <td>Villa Park</td>
      <td>David Coote</td>
      <td>(2-1, 19-13, 13-5)</td>
      <td>3.000000</td>
      <td>2.461538</td>
      <td>3.600000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Norwich</td>
      <td>Everton</td>
      <td>If Norwich have any hope of staging an unlikel...</td>
      <td>Stephen Hollis</td>
      <td>Carrow Road</td>
      <td>Andy Madley</td>
      <td>(37-13, 19-17, 18-7)</td>
      <td>3.846154</td>
      <td>2.117647</td>
      <td>3.571429</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Wolves</td>
      <td>Southampton</td>
      <td>Southampton were excellent in their 4-1 stroll...</td>
      <td>Graham Searles</td>
      <td>Molineux</td>
      <td>Michael Salisbury</td>
      <td>(11-8, 5-2, 9-4)</td>
      <td>2.375000</td>
      <td>3.500000</td>
      <td>3.250000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Everton</td>
      <td>Brighton</td>
      <td>Everton bid to start the year with a much-need...</td>
      <td>Simon Mail</td>
      <td>Goodison Park</td>
      <td>John Brooks</td>
      <td>(7-4, 15-8, 9-4)</td>
      <td>2.750000</td>
      <td>2.875000</td>
      <td>3.250000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Manchester United</td>
      <td>Wolves</td>
      <td>Can Manchester United start 2022 with their mo...</td>
      <td>Jamie Jackson</td>
      <td>Old Trafford</td>
      <td>Mike Dean</td>
      <td>(3-5, 11-2, 10-3)</td>
      <td>1.600000</td>
      <td>6.500000</td>
      <td>4.333333</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Brentford</td>
      <td>Aston Villa</td>
      <td>Steven Gerrard returns to the touchline for As...</td>
      <td>Tim Knowles</td>
      <td>Brentford Community Stadium</td>
      <td>Craig Pawson</td>
      <td>(2-1, 6-4, 2-1)</td>
      <td>3.000000</td>
      <td>2.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Chelsea</td>
      <td>Liverpool</td>
      <td>After threatening a three-way title race, Chel...</td>
      <td>Jacob Steinberg</td>
      <td>Stamford Bridge</td>
      <td>Anthony Taylor</td>
      <td>(2-1, 7-5, 13-5)</td>
      <td>3.000000</td>
      <td>2.400000</td>
      <td>3.600000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Leeds</td>
      <td>Burnley</td>
      <td>The bad news for Marcelo Bielsa and Leeds is t...</td>
      <td>Louise Taylor</td>
      <td>Elland Road</td>
      <td>Kevin Friend</td>
      <td>(6-5, 5-2, 13-5)</td>
      <td>2.200000</td>
      <td>3.500000</td>
      <td>3.600000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Crystal Palace</td>
      <td>West Ham</td>
      <td>A victory against Norwich in the absence of Pa...</td>
      <td>Ed Aarons</td>
      <td>Selhurst Park</td>
      <td>Michael Oliver</td>
      <td>(23-10, 15-11, 5-2)</td>
      <td>3.300000</td>
      <td>2.363636</td>
      <td>3.500000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Arsenal</td>
      <td>Manchester City</td>
      <td>Arsenal are undoubtedly in much better shape t...</td>
      <td>Graham Searles</td>
      <td>Emirates Stadium</td>
      <td>Stuart Attwell</td>
      <td>(5-1, 4-7, 15-4)</td>
      <td>6.000000</td>
      <td>1.571429</td>
      <td>4.750000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Watford</td>
      <td>Tottenham</td>
      <td>Watford attempt to arrest their alarming slump...</td>
      <td>Simon Mail</td>
      <td>Vicarage Road</td>
      <td>Robert Jones</td>
      <td>(9-2, 4-6, 3-1)</td>
      <td>5.500000</td>
      <td>1.666667</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Newcastle</td>
      <td>Manchester United</td>
      <td>Manchester United’s Ralf Rangnick has experien...</td>
      <td>Luke McLaughlin</td>
      <td>St James’ Park</td>
      <td>Craig Pawson</td>
      <td>(6-1, 4-9, 7-2)</td>
      <td>7.000000</td>
      <td>1.444444</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>West Ham</td>
      <td>Southampton</td>
      <td>Southampton are on a winless run of six matche...</td>
      <td>Alex Reid</td>
      <td>London Stadium</td>
      <td>Kevin Friend</td>
      <td>(5-6, 3-1, 11-4)</td>
      <td>1.833333</td>
      <td>4.000000</td>
      <td>3.750000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Tottenham</td>
      <td>Crystal Palace</td>
      <td>Tottenham looked energised in the 2-2 draw wit...</td>
      <td>Luke McLaughlin</td>
      <td>Tottenham Hotspur Stadium</td>
      <td>Jonathan Moss</td>
      <td>(3-4, 4-1, 11-4)</td>
      <td>1.750000</td>
      <td>5.000000</td>
      <td>3.750000</td>
    </tr>
  </tbody>
</table>
</div>


