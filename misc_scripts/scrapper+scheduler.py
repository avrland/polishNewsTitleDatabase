#from github import Github
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
from logger import create_logger
from datetime import datetime
import asyncio
import dropbox_uploader

class NewsScrapper:

  newsLang = 'pl' 
  rawFileName = "titles.txt" 
  finalFileName = "titlesWithoutDuplicates.txt"
  newsTags = [ "swiat", "koronawirus", "pis", "polska", "sport", "apple", "samsung", "technologia", "COVID-19", "amazon", "wojna", "google", "gospodarka", "chiny", "rozrywka", "nauka"]

  def __init__(self):
    self.logger = create_logger("news_scrapper")
    self.logger.info(f"===== NewsScrapper started =====")
    schedule.every().day.at("05:50").do(self.job)
    self.logger.info(f"Scheduler of scrapper set at 05:50 (7:50 CEST)")

    self.db_backuper = dropbox_uploader.backuper()
    self.logger.info(f"Scheduler of backuper at 06:00 (8:00 CEST)")
    schedule.every().day.at("06:00").do(self.db_backuper.backup)

  def saveToFile(self, inputArray, outputFileName):
    file_object = open(outputFileName, 'a', encoding="utf-8")
    for count in range(0, len(inputArray['title'])):
        single_article = inputArray['title'][count]
        file_object.write('\n' + single_article)
    file_object.close()

  def removeDuplicates(self, inFileName, outFileName):
    x = 0
    lines_seen = set() # holds lines already seen
    with open(outFileName, "w", encoding="utf-8") as output_file:
        for each_line in open(inFileName, "r", encoding="utf-8"):
            if each_line not in lines_seen: # check if line is not duplicate
                output_file.write(each_line)
                lines_seen.add(each_line)
            else:
                x = x+1
    self.logger.info(f"Duplicates removed: {x}")

  def lineCounter(self, fileName):
    file = open(fileName, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    self.logger.info(f"Amount of lines in file: {line_count}")

  def print_header(self, fileName):
      with open(fileName) as fn:  
        ln = fn.readline()
        lncnt = 0
        while lncnt < 5:
            print("Line {}: {}".format(lncnt, ln.strip()))
            ln = fn.readline()
            lncnt += 1  

  def getDB(self):
      if not os.path.isfile(self.rawFileName):
        url = 'https://raw.githubusercontent.com/avrland/polishNewsTitleDatabase/main/titles.txt'
        wget.download(url, self.rawFileName)

  def backupDB(self):
      currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      # Move a file from the directory d1 to d2
      shutil.copy('/home/ubuntu/titles.txt', '/home/ubuntu/backup/titles_' + currentTime + ".txt")
      self.logger.info(f"Copied current file: {self.rawFileName} to: '/home/ubuntu/backup/titles_'{currentTime}.txt")

  def job(self):
      print("Job started...")    
      #Download current database
      self.getDB()
      self.print_header(self.rawFileName)
      self.lineCounter(self.rawFileName)
      x = 0
      for tag in self.newsTags:
        #print("Collecting newses from tag: " + tag + "...")
        self.logger.info(f"Collecting newses from tag: {tag}")
        googlenews = GoogleNews()
        googlenews.clear()
        googlenews.set_lang(self.newsLang)
        googlenews.setperiod('1d')
        googlenews.get_news(tag)
        output = googlenews.results(sort=True)
        output = pd.DataFrame(output)
        x = x + len(output['title'])
        self.saveToFile(output, self.rawFileName)
      self.logger.info(f"Collected amount of news:  {x}")
      self.removeDuplicates(self.rawFileName, self.finalFileName)

      #os.remove(rawFileName) #delete bufor file
      #logger.info(f"Removed file with duplicates:  {rawFileName}")
      os.rename(self.finalFileName, self.rawFileName) #rename final file to bufor name
      self.logger.info(f"Renamed: {self.finalFileName} to: {self.rawFileName}")
      self.backupDB()

async def main():
    ns = NewsScrapper()
    while True:
        schedule.run_pending()
        await asyncio.sleep(10)


def start_scrapper():
    asyncio.run(main())


if __name__ == "__main__":
    start_scrapper()