"""
urllib提供了一系列操作url的功能
"""
import json
from html.parser import HTMLParser
from urllib import request

def print_response(url):
    with request.urlopen(url) as response:
        data = response.read()
        print('status:', response.status, response.reason)
        print('******')
        for head_name, head_value in response.getheaders():
            print('%s: %s' % (head_name, head_value))
        print('******')
        print('data:', data.decode('utf-8'))

def mock_request(url, *headers):
    assert url is not None and len(url.strip()) != 0, 'url不得为空'
    req = request.Request(url)
    if headers is not None and len(headers) != 0:
        req.add_header(headers[0][0], headers[0][1])
    with request.urlopen(req) as response:
        for head_name, head_value in response.getheaders():
            print('%s: %s' % (head_name, head_value))
        print('******')
        print('data:', response.read().decode('utf-8'))

def get_response_json(url):
    with request.urlopen(url) as response:
        return json.loads(response.read().decode('utf8'))
# print_response('https://liaoxuefeng.com/books/python/built-in-modules/urllib/index.html')
# mock_request('https://www.doubao.com/chat/', ('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'))
print_response('https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no')

data = get_response_json('https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no')
print(json.dumps(data, indent = 4))
assert data['location']['name'] == 'Beijing'

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
