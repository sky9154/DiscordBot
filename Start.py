#-----------------------DiscordBot--------------------------
import discord
from discord.ext import commands,tasks
#-----------------------Main-------------------------------
import os
os.system('cls')
kirito = commands.Bot(command_prefix='kirito ')       #指令前綴
os.chdir(r'D:/雜物/程式設計/Python/discord bot')     #固定檔案位置 
#-----------------------Subroutine--------------------------
import random   #Goplay 隨機數
import Package.Build    #QRcode產生器
import Package.Manga    #漫畫搜尋器
import Package.md   #日期查詢
import Package.Top  #熱門關鍵字
#-----------------------command----------------------------
@kirito.command()    #停止機器人
async def stop(ctx):
    exit()


@kirito.command()    #重複對話
async def 說(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@kirito.command()    #刪除訊息
async def delete(ctx, num: int):
    await ctx.channel.purge(limit=num+1)


@kirito.command()    #升天電梯及電鰻
async def goplay(ctx):
    num=random.randint(1,2)
    if(num%2==0):
        await ctx.send("升天電梯")
    else:
        await ctx.send("電鰻")


@kirito.command()    #QRcode產生器
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


@kirito.command()    #漫畫搜尋器
async def 漫畫(ctx,msg):
    img,name=Package.Manga.num(msg)
    os.system("cls")
    await ctx.message.delete()
    embed=discord.Embed(
        title="目前為"+name+"的封面",
        url="https://nhentai.net/g/"+name+"/1/",
        color=discord.Color.blue())
    embed.set_author(name="漫畫搜尋器", url="https://nhentai.net", icon_url="https://i.imgur.com/IaqcZtR.png")
    embed.set_image(url=img)
    await ctx.send(embed=embed)
    print('>>Bot is online<<')


@kirito.command()    #查詢日期
async def week(ctx, *, msg):
    int=msg
    alist = int.split()
    a=alist[0]
    b=alist[1]
    f=Package.md.week(a,b)
    await ctx.send(f)

@kirito.command()    #熱門話題
async def fire(ctx,num: int):
    top=Package.Top.Top(num)
    await ctx.send(top)


#-----------------------Run---------------------------------
@kirito.event
async def on_ready():
    await kirito.change_presence(activity=discord.Game('Sword Art Online'))
    print(">>Bot is online<<")
kirito.run("")
#------------------------------------------------------------