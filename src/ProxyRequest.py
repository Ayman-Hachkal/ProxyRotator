import httpx 
import threading

class ProxyRequest:
    proxyurl = "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/https/data.txt"
    list_of_proxies = []
    def __init__(self):
        self.requestProxies()

    def get_proxy(self):
        return self.list_of_proxies

    def requestProxies(self):
        try: 
            r = httpx.get(self.proxyurl)
            proxies = r.text
            for line in proxies.splitlines():
                self.list_of_proxies.append(line)
        except:
            print("Errror requesting proxies")
        threading.Timer(300, self.requestProxies)


