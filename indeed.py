import requests
from bs4 import BeautifulSoup

def search_keyword(keyword):
  results_per_page = 50
  base_url = f"https://ie.indeed.com/jobs?"

  url = f"{base_url}q={keyword}&limit=50&start=0"

  #https://ie.indeed.com/jobs?q=.net+developer&l=Dublin&start=10

  #url is passed and given to the request
  request = requests.get(url)

  #gets the raw text content from the html
  html_result = request.text

  #BeautifulSoap get this html text and parse it in order to make it
  #readable and "Beautiful" to read by parsing it
  soap = BeautifulSoup(html_result, 'html.parser')

  #returns the total number of pages by getting all ul element
  pagination = soap.find('ul', class_="pagination-list").find_all('a')
  #creates a list of pages initialized by 0 and 1
  number_of_pages = [0, 1]

  #foreach ul element in the list pagination gets the number of pages
  for link in pagination:
    n_page = link.string
    if n_page == None:
      continue
    number_of_pages.append(n_page)
  
  #printing the lenght of number of pages
  print(len(number_of_pages))

  url_list = []

  for pages in range(0, len(number_of_pages)):
    build_url = f"{base_url}q={keyword}&limit=50&start={results_per_page * pages}".strip()
    url_list.append(build_url)
  #print(url_list)
  
  return get_jobs_indeed(url_list)

def get_jobs_indeed(urls):
  all_jobs = []
  for url in urls:
    print("Comecando uma url...")
    indeed = requests.get(url)

    indeed_text = indeed.text
    indeed_html = BeautifulSoup(indeed_text, 'html.parser')

    card_result = indeed_html.find_all('div', class_="result")

    for card in card_result:

      salary = card.find('span', class_='salaryText')
      if salary is None:
        salary = "No salary available for this position"
      else:
        salary = card.find('span', class_='salaryText').string.replace(",", ".").replace('"', "")
      #'salary': salary,
      job = {
        'title': card.find('a').get('title'),
        'company': card.find('span', class_='company').get_text().replace("\n", ""),
        'location': card.find('span', class_='location').string,
        'link': f"https://ie.indeed.com{card.find('a').get('href')}",
        'job_date': card.find('span', class_='date').string
      }
      all_jobs.append(job)
  return all_jobs


  #https://ie.indeed.com/jobs?q=c%23&limit=50&start=350
  #return number_of_pages[:-1]
    