from threading import Thread
import requests
import json


class Download(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('./test' + filename, 'wb') as f:
            f.write(resp.content)

    pass


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=ca8465005a2a3587b4ec598151a9ef1f&num=10'
    )

    data = resp.json()

    print(data)
    for mm in data['newslist']:
        url = mm['picUrl']
        Download(url).start()
    pass


if __name__ == "__main__":
    main()
    pass