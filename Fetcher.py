import requests


class FetchImages:
    def __init__(self, searchTag):
        self.searchTag = searchTag
        self.link = None

    def link(self):
        return self.link
    
    def find_random_image_tenor(self):
        try:
            url_tenor_random = 'https://g.tenor.com/v1/random?q={}&key=LIVDSRZULELA&limit=1'.format(self.searchTag)
            # Make a request to the Tenor API
            response = requests.get(url_tenor_random)

            if response.status_code == 200:
                tenor_data = response.json()

                if not tenor_data:
                    return f"Tag '{self.searchTag}' not found."
                else:
                    image_url = tenor_data["results"][0]["media"][0]["gif"]["url"]
                    return image_url
            else:
                return "Unable to find an image for the specified query."
        except Exception as e:
            print(e)
            return "ERROR"
