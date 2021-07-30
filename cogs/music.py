import discord
from discord import colour
from discord.embeds import Embed
from discord.ext.commands.core import command
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

from requests.api import get

load_dotenv()


def lastfm_get(payload):
    headers = {'user-agent': os.getenv("USER_AGENT")}
    url = " http://ws.audioscrobbler.com/2.0/"
    payload['api_key']  = os.getenv("LASTFM_API_KEY")
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)

    return response




def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text[1:-1])



class lastfm_scraper(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def get_album(self, ctx, artist: str, album: str):
        r = lastfm_get({'method': 'album.getinfo', 'artist': f'{artist.replace("_", " ")}', 'album': f'{album.replace("_", " ")}' })
        data = r.json()
        await ctx.send(data["album"]["url"])

    @commands.command()
    async def get_song(self, ctx, artist: str, song: str):
        r = lastfm_get({'method': 'track.getinfo', 'artist': f'{artist.replace("_", " ")}', 'track': f'{song.replace("_", " ")}'})
        data = r.json()
        await ctx.send(data["track"]["url"])

    



def setup(bot):
    bot.add_cog(lastfm_scraper(bot))

