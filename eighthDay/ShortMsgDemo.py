import urllib.parse
import http.client
import json


def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    params = urllib.parse.urlencode({
        'account': '18227631762',
        'password': 'asd19937',
        'content': '您的验证码是：147258。请不要把验证码泄露给其他人。',
        'mobile': '18227631762',
        'format': 'json'
    })
    print(params)
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    resp = conn.getresponse()
    resp_str = resp.read()
    js_str = resp_str.decode('utf-8')
    print(json.loads(js_str))
    conn.close()
    pass


if __name__ == '__main__':
    main()