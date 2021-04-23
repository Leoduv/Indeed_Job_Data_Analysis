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

    # https: // www.youtube.com / watch?v = eN_3d4JrL_w

    len(cards)
    print(cards[0])

    card = cards[0]

    print(card)
