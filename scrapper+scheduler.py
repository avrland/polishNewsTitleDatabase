from github import Github
from GoogleNews import GoogleNews
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
import hashlib
import os
import wget
import shutil
import schedule
import time

newsLang = 'pl' 
rawFileName = "titles.txt" 
finalFileName = "titlesWithoutDuplicates.txt"
newsTags = [ "swiat", "koronawirus", "pis", "polska", "sport", "apple", "samsung", "technologia", "COVID-19", "amazon", "google", "gospodarka", "chiny", "rozrywka", "nauka"]
        
def saveToFile(inputArray, outputFileName):
  file_object = open(outputFileName, 'a', encoding="utf-8")
  for count in range(0, len(inputArray['title'])):
      single_article = inputArray['title'][count]
      file_object.write('\n' + single_article)
  file_object.close()

def removeDuplicates(inFileName, outFileName):
  x = 0
  lines_seen = set() # holds lines already seen
  with open(outFileName, "w", encoding="utf-8") as output_file:
      for each_line in open(inFileName, "r", encoding="utf-8"):
          if each_line not in lines_seen: # check if line is not duplicate
              output_file.write(each_line)
              lines_seen.add(each_line)
          else:
              x = x+1
  print("Duplicates removed: " + str(x))

def lineCounter():
  file = open(rawFileName, "r")
  line_count = 0
  for line in file:
      if line != "\n":
          line_count += 1
  return str(line_count)

def job():    
    #Download current database
    url = 'https://raw.githubusercontent.com/avrland/polishNewsTitleDatabase/main/titles.txt'
    wget.download(url, 'titles.txt')
    filename = 'titles.txt'  
    with open(filename) as fn:  
      ln = fn.readline()
      lncnt = 0
      while lncnt < 5:
           print("Line {}: {}".format(lncnt, ln.strip()))
           ln = fn.readline()
           lncnt += 1   
        #Fetching news section
    x = 0
    for tag in newsTags:
      print("Collecting newses from tag: " + tag + "...")
      googlenews = GoogleNews()
      googlenews.clear()
      googlenews.set_lang(newsLang)
      googlenews.setperiod('1d')
      googlenews.get_news(tag)
      output = googlenews.results(sort=True)
      output = pd.DataFrame(output)
      x = x + len(output['title'])
      saveToFile(output, rawFileName)
    print("Collected amount of news: " + str(x))
    removeDuplicates(rawFileName, finalFileName)

    os.remove(rawFileName) #delete bufor file
    print("Removed file with duplicates: " + rawFileName)
    os.rename(finalFileName,rawFileName) #rename final file to bufor name
    print("Renamed:" + finalFileName + " to: " + rawFileName)

    #Github upload section
    g = Github("INSERT TOKEN HERE")
    repo = g.get_repo("avrland/polishNewsTitleDatabase")
    currentFile = repo.get_contents("/titles.txt")

    newFile = open("titles.txt").read()

    # update
    repo.update_file("titles.txt", "Titlebase update, current size: " + lineCounter() + " newses", newFile, currentFile.sha)

    #Pobierz dzisiejszą datę i godzinę
    from datetime import datetime
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Move a file from the directory d1 to d2
    shutil.move('/home/ubuntu/titles.txt', '/home/ubuntu/backup/titles_' + currentTime + ".txt")
print("schedule.every().day.at(""09:50"").do(job)")
schedule.every().day.at("09:50").do(job)
#schedule.every(10).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
