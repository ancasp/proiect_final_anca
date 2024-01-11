import asyncio
import requests
from bs4 import BeautifulSoup as bs

url = ['https://www.zf.ro/']

async def zf_titluri(url):
    raspuns = requests.get(url)
    text_html = raspuns.text
    soup = bs(text_html, "html.parser")
    titlu = soup.find(id = "firstHeading")

    return titlu.text
async def main():
    titluri = []
    for url in url:
        titlu = await zf_titluri(url)
        await asyncio.sleep(2)
        titluri.append(titlu)

    for title in titluri:
        print(title)

if __name__ == "__main__":
    asyncio.run(main())

