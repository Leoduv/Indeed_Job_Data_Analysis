from datetime import datetime
from bs4 import BeautifulSoup
import requests

URL = "https://fr.indeed.com/jobs?q={}&l={}"


def get_url(job, location):
    indeed = "https://fr.indeed.com/jobs?q={}&l={}"
    url = indeed.format(job, location)
    return url


if __name__ == "__main__":
    test = get_url("CTO", "France")
    response = requests.get(test)

    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.findAll('div', 'jobsearch-SerpJobCard')

    print(len(cards))

    card = cards[0]

    jobatag = card.h2.a

    job_title = jobatag.get('title')

    job_url = f"https://fr.indeed.com{jobatag.get('href')}"

    # strip to remove spacing after or before the text
    company = card.find('span', {'class': 'company'}).text.strip()

    job_location = card.find('div', {'class': 'recJobLoc'}).get('data-rc-loc')

    job_summary = card.find('div', {'class': 'summary'}).text.strip()

    job_post_date = card.find('span', {'class': 'date date-a11y'}).text

    today_date = datetime.today().strftime('%d-%m-%Y')

    print(job_url)

    response_job = requests.get(job_url)

    soup_job = BeautifulSoup(response_job.text, 'html.parser')

    job_presentation = soup_job.find('div', {'class': "jobsearch-ViewJobLayout"})

    job_description = job_presentation.find('div', {'id': 'jobDescriptionText'}).text.strip()

    print(job_description)
    # job_full_description = job_description_detail.find('div', {'id': 'jobDescriptionText'}).text.strip()


