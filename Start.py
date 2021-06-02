#-----------------------Discord Bot--------------------------
import discord
from discord.ext import commands
#-----------------------Main---------------------------------
import os
os.system('cls')
shion = commands.Bot(command_prefix='shion ')       #指令前綴
os.chdir(r'D:/雜物/程式設計/Python/discord bot')     #固定檔案位置 
#-----------------------Subroutine---------------------------
import random   #Goplay 隨機數
import Package.Build    #QRcode產生器
import Package.Manga    #漫畫下載器
import Package.md   #日期查詢
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


@shion.command()    #QRcode產生器
async def QRcode(ctx, *, msg):
    str=msg
    alist = str.split()
    a=alist[0]
    b=alist[1]
    Package.Build.QRcode(a,b)
    await ctx.message.delete()
    pic = discord.File('./demo/QRcode.png')
    await ctx.send("```\nQRcode的網址為:"+b+"\n```")
    await ctx.send(file=pic)


@shion.command()    #漫畫下載器
async def 號碼(ctx,msg):
    Package.Manga.num(msg)
    os.system("cls")
    pic = discord.File('./demo/MangaIMG.jpg')
    await ctx.message.delete()
    await ctx.send("```\n目前是"+msg+"的封面\n```")
    await ctx.send(file=pic)
    print('>>Bot is online<<')

@shion.command()    #查詢日期
async def week(ctx, *, msg):
    int=msg
    alist = int.split()
    a=alist[0]
    b=alist[1]
    f=Package.md.week(a,b)
    await ctx.send(f)


#-----------------------Run----------------------------------
@shion.event
async def on_ready():
    await shion.change_presence(activity=discord.Game('Sword Art Online'))
    print(">>Bot is online<<")
shion.run("Nzg3MzQ1NDk0NDA1NTQ2MDE0.X9Tmog.fT2AHGbMqXgnZMoblJWM3-mOChQ")
#------------------------------------------------------------