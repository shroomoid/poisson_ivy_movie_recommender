from flask import Flask
from simple_recommender import get_recommendations
from flask import render_template
from flask import request

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return render_template('withcss_index.html', title="Poisson Ivy are the best!!! ")

@app.route('/recommendations')
def recommender():
    html_form_data = dict(request.args)
    print(html_form_data)
    recs = get_recommendations()
    return render_template('recommendations.html', movies=recs)




if __name__ == '__main__':
    app.run(debug=True, port=5000)
