# polishNewsTitleDatabase
Polish [news database](https://github.com/avrland/polishNewsTitleDatabase/blob/main/titles.txt) for analysis and ML purposes. Collected mostly from Google News aggregator. 
```
Line 1: Polka straciła 36 tys. zł: napastnik wykiwał zarówno ją, jak i bank
Line 2: Chrome 86 na Androida pozwoli zaplanować pobieranie. Można już testować
Line 3: Poczta Polska i cyfrowa rewolucja. Identyfikacja RFID przyspieszy wysyłki
Line 4: GOG GALAXY 2.0 łączy siły z Epic Games Store. Jest wreszcie oficjalna integracja
...
Database size: over 70k
```

Tags I used to collect newses:
```python
 newsTags = [ "swiat", "koronawirus", "pis", "polska", "sport", "apple", "samsung", "technologia", "COVID-19", "amazon", "wojna", "google", "gospodarka", "chiny", "rozrywka", "nauka"]
```
* Feel free to try how does it works in [Google Colab](https://colab.research.google.com/github/avrland/polishNewsTitleDatabase/blob/main/GoogleNews_scrapper_to_textfile.ipynb). It containts fully explaination how does it works. 
* [scrapper+scheduler.py](https://github.com/avrland/polishNewsTitleDatabase/blob/main/scrapper%2Bscheduler.py) took Jupyter Notebook to simple python script which you can run at your machine to collect newses everyday automatically. It makes backup on your machine but also sends updated database to github repo.

