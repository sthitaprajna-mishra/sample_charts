from flask import Flask
from flask import render_template
from datetime import time
import os
 
 
app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT"))
 
 
@app.route("/")
def chart():
    legend = 'Feature Importance'

    firstChartOne = [530, 264]
    firstChartTwo = [1647, 1300]

    labels = ['CreditScore',
 'Geography',
 'Gender',
 'Age',
 'Tenure',
 'Balance',
 'NumOfProducts',
 'HasCrCard',
 'IsActiveMember',
 'EstimatedSalary']

    values = [0.1467177043553157,
 0.0378344833562251,
 0.022929773232751312,
 0.23664882948058388,
 0.08139286181730235,
 0.13193117678359773,
 0.13125815681473138,
 0.01984296040112788,
 0.04982255216732852,
 0.14162150159103612]

 
    return render_template('chart.html', values=values, labels=labels, legend=legend, 
    firstChartOne = firstChartOne, firstChartTwo = firstChartTwo)
 
 
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = port)