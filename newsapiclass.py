import discord
from newsapi import NewsApiClient
from datetime import date, timedelta
import os
from dotenv import load_dotenv

class News:
    def __init__(self):
        self.notice = None

    def select_formula_one_news_title_list():
        newsapi = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

        all_articles = newsapi.get_everything(q='formula1',
                                            from_param=str(date.today()-timedelta(days=2)),
                                            to=str(date.today()),
                                            language='en',
                                            sort_by='publishedAt')
        
        discord_options = []
        count = 0
        
        for article in all_articles["articles"]:
            option = discord.SelectOption(label=article["title"], value=count)
            discord_options.append(option)
            count = count + 1

        return discord_options, all_articles["articles"]

    def select_formula_one_news_from_option(articles, option): 
        return articles[option]["url"]