from indeed import search_keyword
from stackoverflow import search_so

def get_jobs(keyword):
  result_so = search_so(keyword)
  result_indeed = search_keyword(keyword)

  all_results = list(result_so + result_indeed)
  total_results(all_results)
  return all_results

def total_results(results):
  total = len(results)
  return total