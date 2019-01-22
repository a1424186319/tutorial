import urllib.request

def get():
    resp = urllib.request.urlopen('http://192.168.221.221:5010/get/')
    p = resp.read().decode()
    return p