import threading
import requests
import time

urls = [
           "https://google.com",
           "https://www.python.org",
           "https://www.apple.com",
           "https://www.wikipedia.org",
       ] * 20

def download_url(url):
    response = requests.get(url)
    print(f"{url} yuklandi! Status: {response.status_code}")

start_time = time.time()

threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Barcha saytlardan yuklash vaqti: {time.time() - start_time:.2f} soniya")