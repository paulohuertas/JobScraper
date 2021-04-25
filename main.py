# from save import save_to_csv
from flask import Flask, render_template, request, redirect
from scrapping import get_jobs, total_results

app = Flask("MaratonaScrapping")

@app.route('/')
def hello_world():
  return "Hello, World!"

@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/result')
def result():
  keyword = request.args.get('keyword')
  keyword.upper()
  if keyword:
    search_result = get_jobs(keyword)
  else:
    return redirect('/index')
  
  total = total_results(search_result)
  return render_template('result.html', keyword=keyword, jobs=search_result, all_results=total)
  

app.run(host='0.0.0.0')

