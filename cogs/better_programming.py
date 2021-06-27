import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


url = "https://betterprogramming.pub/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
    

class better_programming_scraper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def better_programming(self,ctx):
        articles = soup.find('div', class_='u-marginBottom40 js-collectionStream')
        for article in articles:
            latest_articles = article.find('section', class_='u-marginTop30 u-xs-margin0 u-marginBottom15 u-maxWidth1032 u-sm-paddingLeft20 u-sm-paddingRight20 u-borderBox u-marginAuto')
            latest_articles_url = latest_articles.findAll('a', class_="")
            for article in latest_articles_url:
                await ctx.send(article.get('href'))
             

         





def setup(bot):
    bot.add_cog(better_programming_scraper(bot))