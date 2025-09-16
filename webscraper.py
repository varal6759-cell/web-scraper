import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india"
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve page")
    exit()
soup = BeautifulSoup(response.content, 'html.parser')
headlines = soup.find_all(['h2', 'span'], class_=['title', 'w_tle'])
if not headlines:
    headlines = soup.select('div.news-card a')
top_headlines = []
for headline in headlines:
    text = headline.get_text(strip=True)
    if text and text not in top_headlines:
        top_headlines.append(text)
    if len(top_headlines) == 5:
        break
print("Top 5 TIMES OF INDIA News Headlines:")
for i, headline in enumerate(top_headlines, 1):
    print(f"{i}. {headline}")
with open("timesofindia_top_headlines.txt", "w", encoding='utf-8') as f:
    f.write("Top 5 TIMES OF INDIA News Headlines:\n")
    for i, headline in enumerate(top_headlines, 1):
        f.write(f"{i}. {headline}\n")
print("Headlines saved to 'timesofindia_top_headlines.txt'")
