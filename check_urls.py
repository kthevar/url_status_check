import requests
import datetime

urls = ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com']

with open('results.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>URL Response Time</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<h1>URL Response Time</h1>\n')
    f.write('<table>\n')
    f.write('<tr><th>Time</th><th>URL</th><th>Response Code</th><th>Response Time</th><th>Requester IP</th></tr>\n')

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            response_time = response.elapsed.total_seconds()
            requester_ip = response.raw._original_response.peer
        except:
            status_code = 'Error'
            response_time = 'N/A'
            requester_ip = 'N/A'

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f'<tr><td>{now}</td><td>{url}</td><td>{status_code}</td><td>{response_time:.2f} seconds</td><td>{requester_ip}</td></tr>\n')

    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>\n')
