import os
import os.path
import requests


def download(url):
    req = requests.get(url)
    if req.status_code == 404:
        print('No file found at %s' % url)
        return
    filename = url.split('/')[-1]
    with open(filename, 'wb') as fobj:
        fobj.write(req.content)
    print("Download complete!")


if __name__ == '__main__':
    url = input('Please enter a URL: ')
    download(url)
