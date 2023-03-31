from flask import Flask, render_template
import requests
import socket

app = Flask(__name__)

@app.route('/')
def index():
    with open('urls.txt') as f:
        urls = [line.strip() for line in f]

    results = []
    for url in urls:
        response = requests.get(url)
        results.append({
            'url': url,
            'http_response': response.content,
            'http_status_code': response.status_code,
            'requester_ip': requests.get('https://api.ipify.org').text,
            'resolved_dns_target': socket.gethostbyname(url.split('//')[1])
        })

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
