import csv

def save_to_csv(jobs):
  file = open('jobs.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['TITLE', 'COMPANY', 'LOCATION', 'LINK', 'POSTED'])
  
  for job in jobs:
    writer.writerow(list(job.values()))

 

   


