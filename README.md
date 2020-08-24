# FLUFFY-GUIDE

A guide to help you scrap news articles

## Use:
```
git clone https://github.com/swainsubrat/fluffy-guide.git
cd fluffy-guide
scrapy crawl IndiaToday -a topic=trending
```
NOTE: The topic can be modified according to get the news of required tag.

## To Use the Scrapper
```
cd FluffyGuide/spiders/
```
1. Copy the IndiaToday python file.
2. Create a scrapy project using:
```
scrapy startproject <project-name>
```
3. Place the copied python file in the folder spider inside project folder.
4. Run the same way as before.