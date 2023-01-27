# polishNewsTitleDatabase
Polish [news titles database](https://github.com/avrland/polishNewsTitleDatabase/blob/main/titles.txt) for analysis and ML purposes. 
* scrapped between 2020 and 2022 year (yeah, covid and war are included)
* **titles.txt** - titles database line by line in raw .txt
* collected mostly from Google News aggregator using [GoogleNews Python](https://pypi.org/project/GoogleNews/) library
* no obvious duplicates
```
Line 1: Polka straciła 36 tys. zł: napastnik wykiwał zarówno ją, jak i bank
Line 2: Chrome 86 na Androida pozwoli zaplanować pobieranie. Można już testować
Line 3: Poczta Polska i cyfrowa rewolucja. Identyfikacja RFID przyspieszy wysyłki
Line 4: GOG GALAXY 2.0 łączy siły z Epic Games Store. Jest wreszcie oficjalna integracja
...
File Size is: 8.677 MB
Titles amount: 114952
Amount of words totally: 1213788
```
## Some stats
### News title lenght (characters) - boxplot charts
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_lenght_raw.png)
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_lenght_witout_outliers.png)

Outliers (1315) removed via IQR method. 

### News title lenght (words) - boxplot charts
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_words_raw.png)
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_words_outliers.png)

Outliers (1691) removed via IQR method. 

### Characters vs words
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/chars_words_with_outliers.png)
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/chars_words_without_outliers.png)

Outliers removed via IQR method. 

### Wordcloud
This is most used 30 words in database. I manually removed short words who brings no any meaning and context.

<img src="https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/wordcloud.png" width=35% height=35%>

### Tags used to collect newses:
```python
 newsTags = [ "swiat", "koronawirus", "pis", "polska", "sport", "apple", "samsung", "technologia", "COVID-19", "amazon", "wojna", "google", "gospodarka", "chiny", "rozrywka", "nauka"]
```
* You can check how data was fetched in [Google Colab notepad](https://colab.research.google.com/github/avrland/polishNewsTitleDatabase/blob/main/GoogleNews_scrapper_to_textfile.ipynb).
* You can also try working with stats in [Google Colab notepad](https://github.com/avrland/polishNewsTitleDatabase/blob/main/Stats_and_visualization.ipynb)
