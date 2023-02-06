import discord
from discord.ext import commands
import requests, aiohttp, io, json

with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get("https://meme-api.herokuapp.com/gimme")
      res = r.json()
      em = discord.Embed(title="Meme",color=embed_color)
      em.set_image(url=res['url'])
      await ctx.send(embed=em)
    
    @commands.command()
    async def dog(self, ctx): # b'\xfc'
      await ctx.message.delete()
      r = requests.get("https://dog.ceo/api/breeds/image/random").json()
      em = discord.Embed(title="Dog Photo",colour=embed_color)
      em.set_image(url=str(r['message']))
      try:
          await ctx.send(embed=em)
      except:
          await ctx.send(str(r['message']))

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
      await ctx.message.delete()
      r = requests.get("https://nekos.life/api/v2/img/hug")
      res = r.json()
      try:
          async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
          with io.BytesIO(image) as file:
            await ctx.send(user.mention)
      except:
          embed = discord.Embed(title=f"{ctx.message.author.name} Hugged {user.name}")
          embed.set_image(url=res['url'])
          embed.set_footer(text=embed_footer)
          await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(res['url']) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(user.mention)
        except:
            embed = discord.Embed(title=f"{ctx.message.author.name} Kissed {user.name}")
            embed.set_image(url=res['url'])
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed)

    @commands.command()
    async def clyde(self, ctx, text: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(colour=embed_color)
                embed.set_image(url=res["message"])
                await ctx.send(res["message"])

    @commands.command()
    async def tweet(self, ctx, username: str, *, message: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                res = await r.json()
                embed = discord.Embed(colour=embed_color)
                embed.set_image(url=res["message"])
                await ctx.send(res["message"])
  

def setup(client):
    client.add_cog(image(client))