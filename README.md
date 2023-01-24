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
Database size: 114373
```
## Some stats
### News lenght (characters) - boxplot charts
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_lenght_raw.png)
![This is an image](https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/news_lenght_witout_outliers.png)

Outliers removed via IQR method. 

### Wordcloud
This is most used 30 words in database. I manually removed short words who brings no any meaning and context.
<img src="https://github.com/avrland/polishNewsTitleDatabase/raw/main/docs/wordcloud.png" width=35% height=35%>

### Tags used to collect newses:
```python
 newsTags = [ "swiat", "koronawirus", "pis", "polska", "sport", "apple", "samsung", "technologia", "COVID-19", "amazon", "wojna", "google", "gospodarka", "chiny", "rozrywka", "nauka"]
```
* Feel free to try how does it works in [Google Colab](https://colab.research.google.com/github/avrland/polishNewsTitleDatabase/blob/main/GoogleNews_scrapper_to_textfile.ipynb). It containts fully explaination how does it works.
