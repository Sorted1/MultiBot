import discord
from discord.ext import commands
import requests, json, random


with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class nsfw(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.errors.NSFWChannelRequired):
        msg = discord.Embed()
        msg.title = "NSFW Command"
        msg.description = error.args[0]
        return await ctx.send(embed=msg)

    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=hentai")
        res = r.json()
        em = discord.Embed(title="Hentai", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

    @commands.command()
    @commands.is_nsfw()
    async def feet(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=feet")
        res = r.json()
        em = discord.Embed(title="Feet", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

    @commands.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=boobs")
        res = r.json()
        em = discord.Embed(title="Boobs", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

    @commands.command()
    @commands.is_nsfw()
    async def anal(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=anal")
        res = r.json()
        em = discord.Embed(title="Anal", colour=embed_color)   
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)   

    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=blowjob")
        res = r.json()
        em = discord.Embed(title="BlowJob", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

    @commands.command()
    @commands.is_nsfw()
    async def gonewild(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=gonewild")
        res = r.json()
        em = discord.Embed(title="Gone Wild", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

    @commands.command()
    @commands.is_nsfw()
    async def pussy(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=pussy")
        res = r.json()
        em = discord.Embed(title="Gone Wild", colour=embed_color)
        em.set_image(url=res['message'])
        await ctx.send(embed=em, delete_after=60)

def setup(client):
    client.add_cog(nsfw(client))