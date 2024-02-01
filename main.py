import sys
import os
#sys.path.append('/home/cnct/local/python/lib/python3.9/site-packages/discord')
import discord
import random
import getImage
import PIL
import uuid
#from dotenv import load_dotenv

import getLocation

Intents = discord.Intents.all()
#Intents.members = True
client = discord.Client(intents=Intents)
# ランダムで送るメッセージの一覧 ※ここに書き足すことでランダムに選ぶ内容を増やせる
random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    
    name = message.author.name
    # メッセージの本文が 鳴いて だった場合
    if message.content == "d":

        # 送信するメッセージをランダムで決める
        #content = name + random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る

        #マップデータを取得
        mapdata = getLocation.getLocations()
        #ランダムに選択
        NamedLocation = getLocation.FindNamedLocation(mapdata.data)
        location = random.choice(NamedLocation)
        x = location.location.x
        y = location.location.y
        z = location.location.z
        print(location.name,"x:",y,"y:",x)
        # _url = geturl()
        img = getImage.GetImage(mapdata.PoisImage,x,y)
        
        #tmpファイルを保存
        fn = "./tmp" + str(uuid.uuid1()) + ".png"
        img.save(fn,format='png')
        
        msg = location.name + " x:" + str(location.location.x), " y:" + str(location.location.y) + " z:" + str(location.location.z)
        await message.channel.send(msg,file=discord.File(fn))
        
        #tmpファイルを削除
        os.remove(fn)
        

    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")

token = os.getenv('TOKEN')
client.run(token)