import discord
from discord.ext import commands
import requests, aiohttp, io, json, urllib, random
import string

with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = black

class tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ascii(self, ctx, *, text):
        await ctx.message.delete()
        r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
        if len('```'+r+'```') > 2000:
            return
        await ctx.send(f"```{r}```")

    @commands.command()
    async def nitro(self, ctx):
        await ctx.message.delete()
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')

    @commands.command(pass_context=True)
    async def invite(self, ctx):
      link = await ctx.channel.create_invite(xkcd=True, max_age = 0, max_uses = 0)
      em = discord.Embed(title=f"Join The {ctx.guild.name} Discord Server Now!", url=link, description=f"**{ctx.guild.member_count} Members** [**JOIN**]({link})\n\n**Invite link for {ctx.channel.mention} is created.**\nNumber of uses: **Infinite**\nLink Expiry Time: **Never**", color=0x303037)
      em.set_thumbnail(url=ctx.guild.icon_url)
      em.set_author(name="INSTANT SERVER INVITE")
      await ctx.send(f"> {link}", embed=em)

    @commands.command()
    async def ranum(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1")
        res = r.json()
        em = discord.Embed(title="Random Number Generator",colour=embed_color, description=f'```{res}```')
        await ctx.send(embed=em)

  

def setup(client):
    client.add_cog(tools(client))