import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, long_url):
        code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[code] = long_url
        return f"http://short.ly/{code}"

    def resolve(self, code):
        return self.url_map.get(code, "URL not found, buddy!")

if __name__ == "__main__":
    shortener = URLShortener()
    my_url = "https://github.com/Jernish-FDO/Python"
    
    print(f"🔗 Original: {my_url}")
    short_link = shortener.shorten(my_url)
    print(f"✨ Shortened: {short_link}")
    
    code = short_link.split("/")[-1]
    print(f"🏠 Resolves to: {shortener.resolve(code)}")
