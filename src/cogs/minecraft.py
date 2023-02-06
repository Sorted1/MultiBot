import discord
from discord.ext import commands
import aiohttp, json, os

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
    async def bedwars(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
          async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
              res = await r.json()
              bedwins = res['stats']["BedWars"]["wins"]
              bedloss = res['stats']["BedWars"]["losses"]
              bedfk = res['stats']["BedWars"]["final_kills"]
              bedfd = res['stats']["BedWars"]["final_deaths"]
              uuid = res["uuid"]

              embed = discord.Embed(colour=embed_color, title=res["username"])
              embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
              embed.add_field(name="BedWars Wins", value=f"```{bedwins}```", inline=True)
              embed.add_field(name="BedWars Losses", value=f"```{bedloss}```", inline=True)
              embed.add_field(name="Final Kills", value=f"```{bedfk}```", inline=True)
              embed.add_field(name="Final Deaths", value=f"```{bedfd}```", inline=True)
              await ctx.send(embed=embed)

    @commands.command()
    async def classicduels(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                cdwins = res["stats"]["Duels"]["gamemodes"]["classic_duel"]["wins"]
                cdloss = res["stats"]["Duels"]["gamemodes"]["classic_duel"]["losses"]
                cdk = res["stats"]["Duels"]["gamemodes"]["classic_duel"]["kills"]
                cdd = res["stats"]["Duels"]["gamemodes"]["classic_duel"]["deaths"]
                uuid = res["uuid"]

                embed = discord.Embed(colour=embed_color, title=res["username"])
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                embed.add_field(name="Clasic Duel Wins", value=f"```{cdwins}```", inline=True)
                embed.add_field(name="Clasic Duel Losses", value=f"```{cdloss}```", inline=True)
                embed.add_field(name="Classic Duel Kills", value=f"```{cdk}```", inline=True)
                embed.add_field(name="Classic Duel Deaths", value=f"```{cdd}```", inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    async def sumo(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                cdwins = res["stats"]["Duels"]["gamemodes"]["sumo"]["wins"]
                cdloss = res["stats"]["Duels"]["gamemodes"]["sumo"]["losses"]
                cdk = res["stats"]["Duels"]["gamemodes"]["sumo"]["kills"]
                cdd = res["stats"]["Duels"]["gamemodes"]["sumo"]["deaths"]
                uuid = res["uuid"]

                embed = discord.Embed(colour=embed_color, title=res["username"])
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                embed.add_field(name="Sumo Wins", value=f"```{cdwins}```", inline=True)
                embed.add_field(name="Sumo Losses", value=f"```{cdloss}```", inline=True)
                embed.add_field(name="Sumo Kills", value=f"```{cdk}```", inline=True)
                embed.add_field(name="Sumo Deaths", value=f"```{cdd}```", inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    async def skywars(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                skwins = res["stats"]["SkyWars"]["wins"]
                skloss = res["stats"]["SkyWars"]["losses"]
                skk = res["stats"]["SkyWars"]["kills"]
                skd = res["stats"]["SkyWars"]["deaths"]
                skdr = res["stats"]["SkyWars"]["kill_death_ratio"]
                uuid = res["uuid"]

                embed = discord.Embed(colour=embed_color, title=res["username"] + " SkyWars Stats")
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                embed.add_field(name="SkyWars Wins", value=f"```{skwins}```", inline=True)
                embed.add_field(name="SkyWars Losses", value=f"```{skloss}```", inline=True)
                embed.add_field(name="SkyWars Kills", value=f"```{skk}```", inline=True)
                embed.add_field(name="SkyWars Deaths", value=f"```{skd}```", inline=True)
                embed.add_field(name="SkyWars KD", value=f"```{skdr}```", inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    async def uhc(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                uhwins = res["stats"]["UHC"]["wins"]
                uhloss = res["stats"]["UHC"]["win_loss"]
                uhk = res["stats"]["UHC"]["kills"]
                uhd = res["stats"]["UHC"]["deaths"]
                uhl = res["stats"]["UHC"]["level"]
                uuid = res["uuid"]

                embed = discord.Embed(colour=embed_color, title=res["username"] + " SkyWars Stats")
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                embed.add_field(name="UHC Wins", value=f"```{uhwins}```", inline=True)
                embed.add_field(name="UHC Losses", value=f"```{uhloss}```", inline=True)
                embed.add_field(name="UHC Kills", value=f"```{uhk}```", inline=True)
                embed.add_field(name="UHC Deaths", value=f"```{uhd}```", inline=True)
                embed.add_field(name="UHC Level", value=f"```{uhl}```", inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    async def mc(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                uuid = res["uuid"]
                skin = f"https://crafatar.com/renders/body/{uuid}?size=4&default=MHF_Steve&overlay"

                embed = discord.Embed(colour=embed_color, title="About " + res["username"])
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                embed.add_field(name="UUID", value=f"```{uuid}```", inline=False)
                embed.add_field(name="Skin", value=f"[Click Here](https://crafatar.com/skins/{uuid})", inline=False)
                embed.add_field(name="NameMC", value=f"[Click Here](https://namemc.com/profile/{username})", inline=False)
                embed.set_image(url=skin)
                await ctx.send(embed=embed)

    @commands.command()
    async def level(self, ctx, username: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.slothpixel.me/api/players/{username}") as r:
                res = await r.json()
                uuid = res["uuid"]
                level = res["level"]

                embed = discord.Embed(colour=embed_color, title=f"About {username}", description=f"{username} is level {level}!")
                embed.set_thumbnail(url=f"https://visage.surgeplay.com/bust/{uuid}")
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(image(client))