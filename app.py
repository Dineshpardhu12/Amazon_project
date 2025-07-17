from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger', methods=['POST'])
def trigger():
    # Trigger Jenkins pipeline
    jenkins_url = "http://<jenkins_host>:8080/job/my-job/build"
    response = requests.post(jenkins_url, auth=("admin", "your_api_token"))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
