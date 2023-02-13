import csv
from flask import Flask
from flask import render_template
app = Flask(__name__) # double underscores

def get_csv():
    csv_path = './static/balt911.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<call_number>/')
def detail(call_number):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['callNumber'] == call_number:
            return render_template(template, object=row)

if __name__ == '__main__':
    # turn on test server
    app.run(debug=True, use_reloader=True)