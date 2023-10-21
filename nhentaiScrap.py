import cloudscraper
import random
class HentaiScrap():
    scraper = cloudscraper.create_scraper()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}
    # Define the cookie string
    cookie_string = "csrftoken=9wvmUvUMiaZ2C63KLpDqNMuKYcVmWzhRxroecUKqw7KGLOv8J2VoU3BQZrVlejXd; cf_clearance=JBMcUgzvwtafK10jxcPSvDcUnxpf4BW7ZBv5cJrxaU8-1697856110-0-1-6aa2f90e.82630f08.3da3a6ee-160.0.0"

    # Convert the cookie string to a dictionary
    cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_string.split('; ')}
    # Step 1: Make an HTTP request to the URL
    def hentai_scrap(self):
        rand_number = random.randint(1,117533)
        url = 'https://nhentai.net/api/gallery/{}'.format(rand_number)
        response = self.scraper.get(url, headers=self.headers, cookies=self.cookies)

        # Check if the request was successful
        if response.status_code == 200:
            # Step 2: Parse the HTML content using BeautifulSoup
            page_content = response.json()
            titl = page_content['title']['english']
            img = 'https://i7.nhentai.net/galleries/{}/1.jpg'.format(page_content['media_id'])
            url = 'https://nhentai.net/g/{}'.format(page_content['id'])
            return titl, img, url
        

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    def hentai_tag(self, query):
        url = 'https://nhentai.net/api/galleries/search?query={}'.format(query)
        response = self.scraper.get(url, headers=self.headers, cookies=self.cookies)        

        # Check if the request was successful
        if response.status_code == 200:

            # Step 2: Parse the HTML content using BeautifulSoup
            query = response.json()
            rand_number = random.randint(0,(len(query["result"])-1))
            page_content =  query["result"][rand_number]
            titl = page_content['title']['english']
            img = 'https://i7.nhentai.net/galleries/{}/1.jpg'.format(page_content['media_id'])
            url = 'https://nhentai.net/g/{}'.format(page_content['id'])
            return titl, img, url
        

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")