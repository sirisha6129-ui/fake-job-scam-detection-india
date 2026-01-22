
from flask import Flask, render_template, request
import sys, os

# PyDroid path fix for utils folder
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "utils"))

from rules import is_scam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        job_text = request.form['job_text']
        if is_scam(job_text):
            result = "⚠️ This text seems like a scam!"
        else:
            result = "✅ This text seems safe."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)