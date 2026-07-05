import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def crawl_cbuae(max_pages: int = 1):
    results = []
    for page in range(max_pages):
        url = f"https://rulebook.centralbank.ae/en/view-revision-updates?page={page}"
        r = requests.get(url, headers=HEADERS, timeout=15)
        print("Status:", r.status_code, "Length:", len(r.text))
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select("a[href*='/en/rulebook/']"):
            title = a.get_text(strip=True)
            link = a["href"]
            if title and link:
                results.append({"title": title, "url": link, "reg_body": "CBUAE"})
    return results

if __name__ == "__main__":
    items = crawl_cbuae(max_pages=1)
    print(f"Found {len(items)} items")
    for i in items[:5]:
        print(i)