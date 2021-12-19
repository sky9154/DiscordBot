#-----------------------DiscordBot--------------------------
import discord
from discord import embeds
from discord.ext import commands,tasks
#-----------------------Main--------------------------------
import os
import json
#-----------------------Subroutine--------------------------
import random               # 隨機數
import Package.QRcode       # QRcode產生器
import Package.Manga        # 漫畫搜尋器
import Package.Video        # 影片搜尋器
import Package.Top          # 熱門話題
import Package.Notation     # 中序轉前後序
import Package.Labatt       # 拉霸機
import Package.Coupons      # 加碼卷查詢
#-----------------------Initialization----------------------
def claer():    # 清除垃圾訊息   
    if os.system("clear") is 1:
        os.system("cls")

kirito = commands.Bot(command_prefix="kirito ")       # 指令前綴
kirito.remove_command("help")                         # 刪除help

claer()
#-----------------------command-----------------------------
@kirito.command()    # 停止機器人
async def stop(ctx):
    await ctx.send("> 機器人停止中......")
    exit()

file = r"./asset/json/helpObject.json"    # help embed 物件
with open(file, encoding = "UTF-8") as f:
    embedObject = json.load(f)

@kirito.command()    # help 指令
async def help(ctx):
    embed = discord.Embed(title = "目前可用指令",color = discord.Color.blue())
    for i in range(len(embedObject)):
        embed.add_field(
            name = embedObject[i]["name"], 
            value = embedObject[i]["value"], 
            inline = embedObject[i]["inline"]
        )
    await ctx.send(embed = embed)


@kirito.command()    # 重複對話
async def 說(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@kirito.command()    # 刪除聊天紀錄
async def delete(ctx, num: int):
    await ctx.channel.purge(limit = num + 1)


@kirito.command()    # 升天電梯及電鰻
async def goplay(ctx):
    num = random.randint(1, 2)
    if(num %2 == 0):
        await ctx.send("升天電梯")
    else:
        await ctx.send("電鰻")

@kirito.command()    # QRcode 產生器
async def QRcode(ctx, *, msg):
    await ctx.message.delete()
    alist = msg.split()
    img = alist[0]
    url = alist[1]
    fileType = alist[2]
    Package.QRcode.build(img, url, fileType)
    name = "QRcode.gif" if fileType == "GIF" or fileType == "gif" else "QRcode.png"
    pic = discord.File(name, filename = name)
    embed=discord.Embed(
        title = "**網址**: "+ url,
        url = img,
        color = discord.Color.blue()
    )
    embed.set_author(name="QRcode產生器", icon_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdkaq1MYb6Bsr4zO2s4xTw77sdhCrAL8UsRA&usqp=CAU")
    embed.set_image(url = "attachment://" + name)
    await ctx.send(embed = embed, file = pic)
    os.remove(name)
    claer()
    print(">>Bot is online<<")


@kirito.command()    # 漫畫搜尋器
async def 漫畫(ctx, msg):
    img, name, title = Package.Manga.num(msg)
    claer()
    embed=discord.Embed(
        title = title,
        url = "https://nhentai.net/g/"+name+"/1/",
        color = discord.Color.blue(),
        description = "**編號:** " + name)
    embed.set_author(
        name = "漫畫搜尋器",
        url = "https://nhentai.net",
        icon_url = "https://i.imgur.com/IaqcZtR.png"
    )
    embed.set_image(url = img)
    await ctx.send(embed = embed)
    print('>>Bot is online<<')

@kirito.command()    # 中序轉前後序
async def notation(ctx, msg):
    notation = "```\n中序：" + msg + "\n" + Package.Notation.notation(msg) + "\n```"
    await ctx.send(notation)

@kirito.command()    # 影片搜尋器
async def 影片(ctx, *, msg):
    str=msg
    alist = str.split()
    a = alist[0]
    b = int(alist[1])
    for i in range(1, b+1):
        title,url,image = Package.Video.v(a, i)
        embed = discord.Embed(
            title = title,
            url = url,
            color = discord.Color.blue()
            )
        embed.set_author(
            name = "影片搜尋器", 
            url = "https://avgle.com/videos",
            icon_url = "https://i.imgur.com/OqtDVJ9.png"
        )
        embed.set_image(url = image)
        await ctx.send(embed = embed)
    

@kirito.command()    # 熱門話題
async def fire(ctx, msg):
    while True:
        try:
            msg = int(msg)
            if msg > 10:
                await ctx.send("> 請輸入 10 以下的整數")
                break
            else:
                await ctx.send(Package.Top.Top(msg))
                break
        except:
            await ctx.send("> 請輸入整數")
            break

@kirito.command()    # 隨機百鬼圖片
async def Ayame(ctx, msg):
    try:
        msg = int(msg)
        if msg > 10:
            await ctx.send("> 上限為 10 張圖片，將目前張數限制為 10 張，百鬼看太多會變低能，懂嗎！！！")
            msg = 10
        await ctx.message.delete()
        i = 0
        while i < msg:
            await ctx.send("https://ayame-images.herokuapp.com/" + str(random.randrange(8763)) + ".png")
            i += 1
    except:
        await ctx.send("> 請輸入整數")
    

@kirito.command()    # 拉霸機
async def 拉(ctx):
    labatt = "```\n" + Package.Labatt.start() + "\n```"
    await ctx.send(labatt)

@kirito.command()    # BadApple
async def BadApple(ctx):
    print(1)
    f = open("./asset/txt/1.txt", "r", encoding = "UTF-8")
    a = "```" + f.read() + "```"
    message = await ctx.send(a)
    for i in range(2, 655):
        print(i)
        f = open("./asset/txt/%s.txt"%(i), "r", encoding = "UTF-8")
        b = "```"+ f.read() + "```"
        await message.edit(content = b)
    claer()
    print('>>Bot is online<<')

@kirito.command()    # 加碼卷查詢
async def coupons(ctx, msg):
    await ctx.send(Package.Coupons.check(msg))

#-----------------------TOKEN-------------------------------
# f = open("./TOKEN/token.json") 
# data = json.load(f) 
# token = ""
# for i in data["TOKEN"]: 
#     token += i
#-----------------------Run---------------------------------
if __name__ == "__main__":
    @kirito.event
    async def on_ready():
        await kirito.change_presence(activity=discord.Game("Sword Art Online"))
        print(">>Bot is online<<")
    kirito.run(DISCODE_TOKEN)
#------------------------------------------------------------