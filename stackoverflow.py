import requests
from bs4 import BeautifulSoup

#https://stackoverflow.com/jobs?q=python&pg=2

base_url = "https://stackoverflow.com/jobs?"

def search_so(keyword):
  url = f"{base_url}q={keyword}"

  request = requests.get(url)

  html_so = request.text

  soap = BeautifulSoup(html_so, 'html.parser')

  pagination = soap.find('div', class_='s-pagination').find_all('a')
  
  
  total_pages = pagination[-2].find('span').string
  print(total_pages)
  job_urls = []

  for no_page in range(1, int(total_pages)):
    if no_page == 1:
      url = f"{base_url}q={keyword}"
    else:
      url = f"{base_url}q={keyword}&pg={no_page}"
    
    job_urls.append(url)
  
  return scrapping_so(job_urls)
  
def scrapping_so(urls):
  for url in urls:
    print("Comecando uma url...")
    #url + request
    request = requests.get(url)
    
    #save html onto html_stackoverflow
    html_result = request.text

    #BeautifulSoup parses the whole html
    soap = BeautifulSoup(html_result, 'html.parser')

    #gets all divs with class grid
    cards = soap.find_all('div', class_='-job')
    #list where all jobs will be stored
    job_list = []
    for card in cards:
      jobs = {
        'title': card.find('a', class_='s-link').get('title'),
        'company': card.find('h3', class_='mb4').find_all('span')[0].string,
        'location': card.find('h3', class_='mb4').find_all('span')[1].string,
         'link': f"https://stackoverflow.com/{card.find('a', class_='s-link').get('href')}",
        'job_date': card.find('ul', class_='mt4').find('li').string
      }
      job_list.append(jobs)
  return job_list