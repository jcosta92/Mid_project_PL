# Mid Project
## 1. Resume
This project intention was to analyse the premier league games in a considerable timeframe, with some football stats and also weather stats.
The goal was to create a model with those stats to check its predictions accuracy, and check the influence of weather conditions in football performance.
As each time is unique, in the end the analysis is done for each time.

## 2. Datasets
Two main datasets were used for this model:

  1. Football results data from kaggle: 
  https://www.kaggle.com/code/iliaskydyraliev/premier-league-2022-2023-winner-prediction/input?select=all_fixtures_with_str_result.csv
  
  2. Weather data from: https://www.visualcrossing.com/weather/weather-data-services#
  
  3. The data considered is dated from 2017-08-11 until 2022-11-14. CSV files used are also found in this repository.
  
### 2.1. Football stats glossary
Main stats:
- "Date" - date of the game
- "Time" - time of the game
- "Comp" - Competition
- "Round" - week of the match
- "Day" - weekday of the match
- "Venue" - if its a home or away game of Team
- "Result" - result for the Team, W: win | D: draw | L: loss
- "GF" - goals scored by the Team
- "GA" - goals allowed by the Team
- "Opponent" - opponent of Team
- "xG" - expected goals by the Team
- "xGA" - expected allowed goals by the Team
- "Poss" - possession of the ball of the Team
- "Attendance" - stadium attendies
- "Captain" - captain of the Team
- "Formation" - formation ot the Team
- "Referee" - match referee
- "Match report"
- "Notes"
- "Season"
- "Team"

Shooting stats:
- "Sh" - total number of shots
- "SoT" - shots on target
- "Dist" - average distance in yards from goal of all shots taken
- "FK" - shots from free kicks
- "PK" - penalty kicks made
- "PKatt" - penalty kicks attempted

Passing stats:

- "KP" - passes that directly lead to a shot
- "1/3" - completed passes that enter the final third of the pitch on offense
- "PPA" - completed passes into the 18-yard box not including set pieces
- "CrsPA" - completed crosse into the 18-yard box
- "Prog" - progressive passes, completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area.

Possession stats:
- "Att 3rd" - touches in attacking third of the pitch
- "Att Pen" - touches in attacking penalty area

Goal and Shot Creation stats:
- "SCA" - shot-creating actions, the two offensive actions directly leading to a shot such as passes, dribbles and drawing fouls.

Pass type stats:
- "TB" - completed pass sent between back defenders into open space.

### 2.2. Weather stats glossary
- "tempmax": Maximum temperature in degrees Celsius (ºC)
- "tempmin": Minimum temperature in degrees Celsius (ºC)
- "temp": Temperature (or mean temperature) in degrees Celsius (ºC)
- "dew": Dew Point in degrees Celsius (ºC)
- "feelslike": Feels like temperature in degrees Celsius (ºC)
- "precip": Precipitation in millimeters (mm)
- "precipprob": Precipitation chance in percentage (%)
- "precipcover": Precipitation Cover in percentage (%)
- "preciptype": Precipitation type
- "snow": Snow in centimeters (cm)
- "snowdepth": Snow Depth in centimeters (cm)
- "windspeed": Wind Speed in kilometers per hour (kph)
- "windgust": Wind Gust in kilometers per hour (kph)
- "winddir": Wind Direction in degrees (º)
- "visibility": Visibility in kilometers (km)
- "cloudcover": Cloud Cover in percentage (%)
- "humidity": Relative Humidity in percentage (%)
- "pressure": Sea Level Pressure in millibars (mb)
- "solarradiation": Solar Radiation in watts per square meter (W/m²)
- "solarenergy": Solar Energy in megajoules per square meter (MJ/m²)
- "uvindex": UV Index
- "severerisk": Severe Risk
- "sunrise": Sunrise time
- "sunset": Sunset time
- "moonphase": Moonphase
- "icon": A weather icon
- "conditions": Short text about the weather
- "description": Description of the weather for the day
- "stations": List of weather station sources

## 3. Data cleaning and modelling
Data cleaning process and modelling can be seen in the python notebook "midproject_PLresults.ipynb" in this repository.
All the functions used in it are saved on the "functions" folder.

## 4. Data visualization
Data visualization was done by Tableau Public, under the following link:
[https://public.tableau.com/views/midproject_16826138070510/Dashboard4?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link](https://public.tableau.com/views/midproject_16826138070510/Dashboard4?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

The pngs images used are in this repository under the folder "pngs".

## 5. Conclusion
- The model used was Random Forest Regressor. This was the only model that gave good results. Reason to be further checked.
- For the main data of roughly 4 seasons, the accuracy of W/L/D was of 82%.
- For the last season of data, of 101 games with prediction to Win or Loose, if we had betted on the respective prediction (W/L) + D (Draw) we would have won 85% of the bets, roughly 85 bets in this case.
- Regarding the data model, it needs to be further analysed because there may be too much accuracy in the seasons until 2021/22, maybe due to the X being that data. Nevertheless for the football stats only the mean averages of previous games were used.
- About the data analysis of the results with weather conditions, it vary in some clubs and might be usefull for themselves.
