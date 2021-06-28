from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands


url = "https://dev.to/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')



class dev_scraper(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def dev_latest(self,ctx):
        url = "https://dev.to/latest"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        articles = soup.find('div', class_='crayons-layout crayons-layout--3-cols crayons-layout--3-cols--drop-right-left')
        links = articles.find_all('a', class_='crayons-story__hidden-navigation-link')
        for url in links:
            await ctx.send("https://dev.to"+url.get('href'))

    @commands.command()
    async def dev_week(self,ctx):
        url = "https://dev.to/top/week"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        articles = soup.find('div', class_='crayons-layout crayons-layout--3-cols crayons-layout--3-cols--drop-right-left')
        links = articles.find_all('a', class_='crayons-story__hidden-navigation-link')
        for url in links:
            await ctx.send("https://dev.to"+url.get('href'))
    
    @commands.command()
    async def dev_month(self,ctx):
        url = "https://dev.to/top/month"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        articles = soup.find('div', class_='crayons-layout crayons-layout--3-cols crayons-layout--3-cols--drop-right-left')
        links = articles.find_all('a', class_='crayons-story__hidden-navigation-link')
        for url in links:
            await ctx.send("https://dev.to"+url.get('href'))
     
    @commands.command()
    async def dev_year(self,ctx):
        url = "https://dev.to/top/year"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        articles = soup.find('div', class_='crayons-layout crayons-layout--3-cols crayons-layout--3-cols--drop-right-left')
        links = articles.find_all('a', class_='crayons-story__hidden-navigation-link')
        for url in links:
            await ctx.send("https://dev.to"+url.get('href'))
    
    @commands.command()
    async def dev_infinity(self,ctx):
        url = "https://dev.to/top/infinity"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        articles = soup.find('div', class_='crayons-layout crayons-layout--3-cols crayons-layout--3-cols--drop-right-left')
        links = articles.find_all('a', class_='crayons-story__hidden-navigation-link')
        for url in links:
            await ctx.send("https://dev.to"+url.get('href'))





def setup(bot):
    bot.add_cog(dev_scraper(bot))

    
