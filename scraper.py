from requests_html import HTMLSession

class Scraper():
    def scrapedata(self, tag):
        url = f"https://quotes.toscrape.com/tag/{tag}"
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        my_list = []

        quotes = r.html.find("div.quote")
        for q in quotes:
            item = {
                'text': q.find("span.text", first=True).text.strip(),
                'Author': q.find("small.author", first=True).text.strip()
            }
            #print(item)
            my_list.append(item)
        return my_list



quotes = Scraper()

quotes.scrapedata("life")
