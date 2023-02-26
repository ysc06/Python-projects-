import requests 
from bs4 import BeautifulSoup


def main():
	url = "https://www.imdb.com/chart/top/"
	response = requests.get(url)
	print(response)
	html = response.text  # huge string
	soup = BeautifulSoup(html)
	items = soup.find_all("td", {"class": "titleColumn"})
	for item in items:
		year = item.span.text
		print(year)


if __name__ == '__main__':
	main()
