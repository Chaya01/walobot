import requests

class Fetchbooru:
    def __init__(self,query_words):
        self.query_words = query_words
        self.link = None

    def link(self):
        return self.link
    
    async def find_rand_img(self,ctx):
    # Combine the query words with underscores to form the query
        #query = "_".join(self.query_words)
        if self.query_words == 'fate_(series)':
            query = self.query_words
        else:
            query = "_".join(self.query_words)

        # Danbooru API URL to fetch a random image with the specified query
        danbooru_api_url = f"https://danbooru.donmai.us/posts/random.json?tags={query}"

        try:
            # Make a request to the Danbooru API
            response = requests.get(danbooru_api_url)

            if response.status_code == 200:
                danbooru_data = response.json()

                if not danbooru_data:
                    return(f"Tag '{query}' not found.")
                else:
                    image_url = danbooru_data["file_url"]
                    return image_url
            else:
                await ctx.send("Unable to find an image for the specified query.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")




""""
    def FindTagBooru(self):
        # Combine the query words with underscores to form the query
        query = "_".join(self.searchTag)

        # Danbooru API URL to fetch a random image with the specified query
        danbooru_api_matches = f"https://danbooru.donmai.us/tags.json?search[name_matches]={query}*"

        try:
            response = requests.get(danbooru_api_matches)

            if response.status_code == 200:
                danbooru_data = response.json()

                if not danbooru_data:
                    return f"tag '{self.searchTag}' not found."
                else:
                    bestTag = danbooru_data[0]["name"]
                    self.bestTag = bestTag
                    return self.bestTag
        except Exception as e:
            print(e)
            return "Error1"
                
    def GetImgBooru(self):
        try:
            if self.bestTag is not None:
                # Make a request to the Danbooru API using the best tag
                danbooru_api_url = f"https://danbooru.donmai.us/posts/random.json?tags=id:{self.bestTag}"
                response = requests.get(danbooru_api_url)

                if response.status_code == 200:
                    danbooru_data = response.json()

                    if not danbooru_data:
                        return f"tag '{self.bestTag}' not found."
                    else:
                        image_url = danbooru_data["file_url"]
                        return image_url
                else:
                    return "Unable to find an image for the specified query."
        except Exception as e:
            print(e)
            return "ERROR"
"""