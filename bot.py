#-----------------------Discord Bot--------------------------
import discord
from discord.ext import commands
#-----------------------Main---------------------------------
import os
os.system('cls')
shion = commands.Bot(command_prefix='shion ')  # 前綴
#-----------------------Subroutine---------------------------
import random   #Goplay 隨機數

#-----------------------command------------------------------
@shion.command()    #停止機器人
async def stop(ctx):
    exit()


@shion.command()    #重複對話
async def 說(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@shion.command()    #刪除訊息
async def delete(ctx, num: int):
    await ctx.channel.purge(limit=num+1)


@shion.command()    #升天電梯及電鰻
async def goplay(ctx):
    num=random.randint(1,2)
    if(num%2==0):
        await ctx.send("升天電梯")
    else:
        await ctx.send("電鰻")

    

#-----------------------Run----------------------------------
@shion.event
async def on_ready():
    await shion.change_presence(activity=discord.Game('Sword Art Online'))
    print(">>Bot is online<<")
shion.run(TOKEN)
#------------------------------------------------------------