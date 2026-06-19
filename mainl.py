import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

job=requests.get("https://realpython.github.io/fake-jobs/")
soup=BeautifulSoup(job.text,"html.parser")

job_title=soup.find_all("h2",class_="title is-5")
company_name=soup.find_all("h3",class_="subtitle is-6 company")
job_location=soup.find_all("p",class_="location")
job_detail=soup.find_all("a",class_="card-footer-item")

data=[]

for title, company, location, detail in zip(job_title, company_name, job_location, job_detail):
    data.append({

        "title":title.text,
        "company":company.text,
        "location":location.text,
        "detail":detail.get("href")
    })


pprint(data)

with open("Job.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=["title","company","location","detail"])
    writer.writeheader()
    writer.writerows(data)