from datetime import datetime
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import requests


def get_url(job, location):
    indeed = "https://fr.indeed.com/jobs?q={}&l={}"
    url = indeed.format(job, location)
    return url


def get_job_info(job_card):
    job_atag = job_card.h2.a
    job_title = job_atag.get('title')
    job_url = f"https://fr.indeed.com{job_atag.get('href')}"
    job_company = job_card.find('span', {'class': 'company'}).text.strip()
    job_location = job_card.find('div', {'class': 'recJobLoc'}).get('data-rc-loc')
    job_summary = job_card.find('div', {'class': 'summary'}).text.strip()
    job_post_date = job_card.find('span', {'class': 'date date-a11y'}).text
    today_date = datetime.today().strftime('%d-%m-%Y')
    try:
        job_salary = job_card.find('span', {'class': 'salaryText'}).text.strip()
    except AttributeError:
        job_salary = ''

    job_info = {'job_title': job_title,
                'job_url': job_url,
                'job_company': job_company,
                'job_location': job_location,
                'job_summary': job_summary,
                'job_post_date': job_post_date,
                'today_date': today_date,
                'job_salary': job_salary
                }

    return job_info


def check_next_page(soup):
    try:
        next_page_url = soup.find('a', {'aria-label': 'Suivant'})
    except AttributeError:
        next_page_url = None

    return next_page_url


def scrap_job_info(search):
    page_url = search
    job_infos = []

    while page_url:
        results = requests.get(search)

        soup = BeautifulSoup(results.text, 'html.parser')
        cards = soup.findAll('div', 'jobsearch-SerpJobCard')

        for job_card in cards:
            info = get_job_info(job_card)
            job_infos.append(info)

            # get job detailed description

        # random sleep to not get blocked
        print("Short nap")
        num_deci = randint(1, 5)
        sleep(num_deci / 10)
        page_url = check_next_page(soup)

        # print(page_url)
        # print(len(job_infos))

    return job_infos


URL = "https://fr.indeed.com/jobs?q={}&l={}"

if __name__ == "__main__":
    new_search = get_url("Data", "France")
    result = scrap_job_info(new_search)
    print(len(result))
