import discord
import os
import asyncio
from discord.ext import commands
intents = discord.Intents(messages=True,guilds=True)

client = commands.Bot(command_prefix='>',intents=intents,case_insensitive=True)

@client.event
async def on_ready():
	print("Logged in as {0.user}\n".format(client))

@client.command()
async def hello(ctx):
  m=await ctx.send(f"Heyoo I am working, {ctx.author.mention}",delete_after=60)
  await m.add_reaction("👍")


@client.command()
async def start(ctx):
  def check(m):
    return ctx.author == m.author and ctx.channel==m.channel
  await ctx.send(f"{ctx.author.mention}This game is under testing")
  await asyncio.sleep(1)
  await ctx.send(file=discord.File('logo.jpg'))
  await asyncio.sleep(1)
  await ctx.send("To Jump To Next Dialouge React with Emote To Present Dialouge,The GAME Is a Vitual Novel Game You Have To Choose Between Difftent Options,The Option You Choose Will Decide Your Path,Remeber To React With EMOTE To Next Dialouge")
  await ctx.send(file=discord.File('god.jpg'))
  await ctx.send("”HEY YOU, yes you right there it seems like you have gained a consciousness. Hmmm I am the omnificent being who created you they also call me god.",)
  await ctx.send("Do you want to live? Do you want a life? I shall grant you with the most perfect vessel, do you want it or not?” ")
  try:
    msg= await client.wait_for('message',check=check,timeout=12)
  except asyncio.TimeoutError:
    await ctx.send("You Haven't Responded In Time")
  if msg.content.lower() == 'yes':
    await asyncio.sleep(1)
    await ctx.send("Great lets play")
  else:
    await ctx.send("You gonna Miss great Time")
  
    
client.run('ODYwNjg2NjI1OTU1NjQzNDMy.YN-24g.XAZHasSqkxgHvNyIOZuaBZWE7zA')
