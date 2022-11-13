from discord.ext import commands
import discord
import random
import time
import os
import math
import bloxflippredictor
from bloxflippredictor import *

# Bot Prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

# Ids (not exactly api)
ids = []

def checkid(roundid):
  if roundid in ids:
    return False
  ids.append(roundid) 



bombs=1 # Maths for Mines 1

#  Mines predictor
@bot.command(name="mines")
async def reg(ctx, e):
    a = len(e)
    if a == 36: # Checks if Round ID is 36 letters long
      await ctx.send(f'Getting Round ID {e}')
      if checkid(e) == False:
        return
      await mines(ctx, e)
    else:
      time.sleep(2)
      await ctx.send('Invalid Round ID')

# Mines predictor code
async def mines(ctx, e):
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
    tiles = list(range(1,26))
    time.sleep(2)
    await ctx.send(f'{ctx.author.mention} How many tiles do you want open? *(Average: 3-2)* ')
    msg = await bot.wait_for("message", check=check)
    msgo = int(msg.content)
    totalsquaresleft = 25
    formel = ((totalsquaresleft - bombs) / (totalsquaresleft))
    totalsquareslefts = 24
    formel2 = ((totalsquareslefts - bombs) / (totalsquareslefts))
    output = minespredictor(msgo, bombs)
    end = formel2 * 100
    multiplier = calculate_multiplier(msgo, bombs)
    embed=discord.Embed(title="Mines Prediction", description=f" Predicting: {e}")
    embed.add_field(name="mines", value=output, inline=False)
    embed.add_field(name="chances", value=f"Your win chance is {int(end)}%", inline=False)
    embed.add_field(name="winnings", value="Multiplier: {0:.2f}".format(multiplier), inline=False)
    pfp = 'https://cdn.discordapp.com/attachments/976337461254959144/1016437269948801024/standard.gif'
    em = discord.Embed(color=0x11F1D3)
    em.set_thumbnail(url=pfp)
    em.set_footer(text="Vex Services | discord.gg/9G3m78jZSY") # Footer / very bottom description
    await ctx.send(ctx.author.mention, embed=embed)


#  Maths for Mines 2
def nCr(n,r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)

def calculate_multiplier(bombs, msgo):
  house_edge = 0.01
  return (0.96 - house_edge) * nCr(25, msgo) / nCr(25 - bombs, msgo)




# Crash Calculator Command
@bot.command()
async def crash(ctx, multiplier: float):
    embed=discord.Embed(color=0x11F1D3)
    embed.add_field(name="Crash Calculator", value=f"*There's a* {(1 - (1/33 + (32/33)*(.01 + .99*(1 - 1/multiplier))))*100}*% chance of it crashing at or above {multiplier}x*")
    pfp = 'https://cdn.discordapp.com/attachments/976337461254959144/1016437269948801024/standard.gif'
    embed.set_thumbnail(url=pfp)
    embed.set_footer(text="Vex Services | discord.gg/9G3m78jZSY")
    await ctx.reply(embed=embed)


# Value Command
@bot.command()
async def value(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.reply('Please Enter multiplier amount:')
    multiplier = await bot.wait_for('message', check=check)
    multiplier = int(multiplier.content)

    await ctx.reply('Please Enter bet amount:')
    bet_amount= await bot.wait_for('message', check=check)
    bet_amount= int(bet_amount.content)

    await ctx.reply('Please Enter tax percent: (Enter 0 if theirs none)')
    tax_percent= await bot.wait_for('message', check=check)
    tax_percent= int(tax_percent.content)

    await ctx.reply('Please Enter game count:(games your going to play/going for)')
    game_count= await bot.wait_for('message', check=check)
    game_count= int(game_count.content)
    if not tax_percent:
        chance = (1/33 + (32/33)*(.01 + .99*(1 - 1/multiplier)))
    else:
        chance = 1/multiplier
    
    e = ((( (multiplier-1) * bet_amount* 1-tax_percent) * (1 - chance)) + (-bet_amount* chance)) * game_count
    embed=discord.Embed(color=0x11F1D3)
    embed.add_field(name=f'*In* {game_count} *game/s expect to lose R$* {round(e, 2)*-1}', value='*If it says youll lose negative robux that means youll make profit!*' )
    await ctx.reply(embed=embed)


# Towers Command
@bot.command(name="tr")
async def rege(ctx, e):
    a = len(e)
    if a == 36:
      await ctx.send(f'Getting Round ID: {e}')
      if checkid(e) == False:
        return 
      await anu(ctx, e)
    else:
      time.sleep(2)
      await ctx.send('Invalid round ID')
async def anu(ctx, e):
  o = bloxflippredictor.towers
  an = o.towerspredictor()
  embed=discord.Embed(title="Towers Prediction", description=f"Predicting:: {e}")
  embed.add_field(name="towers", value=an, inline=False)
  pfp = 'https://cdn.discordapp.com/attachments/976337461254959144/1016437269948801024/standard.gif'
  embed.set_thumbnail(url=pfp)
  embed.set_footer(text="Vex Services | discord.gg/9G3m78jZSY  (Please Do Not Repeat Round ID!)")
  await ctx.send(ctx.author.mention, embed=embed)


# Roulette predictor
@bot.command(name="re")
async def roulette(ctx):
  output = roulettepredictor()
  embed=discord.Embed(title="Reoulette Prediction", description=f" Predicting: Roulette")
  embed.add_field(name="Roulette", value=output, inline=False)
  pfp = 'https://cdn.discordapp.com/attachments/976337461254959144/1016437269948801024/standard.gif'
  embed.set_thumbnail(url=pfp)
  embed.set_footer(text="Vex Services | discord.gg/9G3m78jZSY  (Please Do Not Repeat Round ID!)")
  await ctx.reply(embed=embed)


bot.run("BOT TOKEN HERE")
