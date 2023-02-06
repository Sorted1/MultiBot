import discord
from discord.ext import commands
import requests, aiohttp, io, json, os

with open('./customize.json') as f:
    customization = json.load(f)

embed_color = customization.get('embed_color')
embed_thumbnail = customization.get('embed_thumbnail')
embed_footer = customization.get('embed_footer')

try:
        embed_color = int(embed_color.replace('#', '0x'), 0)
except:
        embed_color = white

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
      await ctx.message.delete()
      await member.kick(reason=reason)
      em = discord.Embed(title=f"Kicked {member.name}!")
      em.set_image(url=f"{member.avatar_url}")
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, channel: discord.TextChannel, *, message,):
      embed = discord.Embed (title="📢 Announcement!", description=message)
      embed.set_footer(text=embed_footer)
      await channel.send("||@everyone||", embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
      await ctx.message.delete()
      await member.ban(reason=reason)
      em = discord.Embed(title=f"Banned {member.name}!")
      em.set_image(url=f"{member.avatar_url}")
      em.set_footer(text=embed_footer)
      await ctx.send(embed=em)

    @commands.command(name='setwelcome')
    async def setwelcome(self, ctx, channel: discord.TextChannel):
        with open('guilds.json', 'r', encoding='utf-8') as f:
            guilds_dict = json.load(f)

        guilds_dict[str(ctx.guild.id)] = str(channel.id)


        with open('guilds.json', 'w', encoding='utf-8') as f:
            json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
        
        await ctx.send(f'Set welcome channel for {ctx.message.guild.name} to {channel.name}')

    @commands.command(aliases= ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount :int = -1):
      if amount == -1:
        await ctx.message.delete()
        await ctx.send("Please Choose An Amount of Messages You Want To Delete!")
      else:
          await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(admin(client))