# Scraping The Guardian
> scraping Premier League previews from the Guardian.


.

## Install

`pip install guardian_scraper`

## How to use

Use case

```
data.head()
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
      <th>preview_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arsenal</td>
      <td>Burnley</td>
      <td>Arsenal have no excuses if their dismal form i...</td>
      <td>Graham Searles</td>
      <td>Emirates Stadium</td>
      <td>David Coote</td>
      <td>[2-5, 9-1, 4-1]</td>
      <td>1.400000</td>
      <td>10.000000</td>
      <td>5.000000</td>
      <td>2022-01-22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chelsea</td>
      <td>Tottenham</td>
      <td>The dynamic has changed before Chelsea and Tot...</td>
      <td>Jacob Steinberg</td>
      <td>Stamford Bridge</td>
      <td>Paul Tierney</td>
      <td>[13-18, 9-2, 13-4]</td>
      <td>1.722222</td>
      <td>5.500000</td>
      <td>4.250000</td>
      <td>2022-01-22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Crystal Palace</td>
      <td>Liverpool</td>
      <td>Liverpool have already dispelled most of the d...</td>
      <td>Stephen Hollis</td>
      <td>Selhurst Park</td>
      <td>Kevin Friend</td>
      <td>[5-1, 8-13, 10-3]</td>
      <td>6.000000</td>
      <td>1.615385</td>
      <td>4.333333</td>
      <td>2022-01-22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Leicester</td>
      <td>Brighton</td>
      <td>Brendan Rodgers blamed naivety for the extraor...</td>
      <td>Paul Doyle</td>
      <td>King Power Stadium</td>
      <td>Martin Atkinson</td>
      <td>[8-5, 9-2, 12-5]</td>
      <td>2.600000</td>
      <td>5.500000</td>
      <td>3.400000</td>
      <td>2022-01-22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Manchester United</td>
      <td>West Ham</td>
      <td>This is a genuine six-pointer in which Manches...</td>
      <td>Jamie Jackson</td>
      <td>Old Trafford</td>
      <td>Jon Moss</td>
      <td>[10-11, 3-1, 11-4]</td>
      <td>1.909091</td>
      <td>4.000000</td>
      <td>3.750000</td>
      <td>2022-01-21</td>
    </tr>
  </tbody>
</table>
</div>


