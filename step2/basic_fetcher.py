import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    with requests.Session() as session:
        urls = ['https://naver.com',
                'https://google.com', 'https://instagram.com'] * 10
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
