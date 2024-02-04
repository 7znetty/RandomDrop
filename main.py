import sys
import os
import discord
import random
import getImage
import PIL
import uuid
import RandomColor
import getLocation
import datetime

#本番環境設定
#↓さくらサーバー用
#sys.path.append('/home/cnct/local/python/lib/python3.9/site-packages/discord')
from dotenv import load_dotenv
#ここまで

Intents = discord.Intents.all()
#Intents.members = True
client = discord.Client(intents=Intents)

#本番環境設定
load_dotenv()
#ここまで

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    
    #鯖ID取得
    guild = client.get_guild(message.guild.id) 
    memberList = ""
    userId = message.author.id

    #VCに接続されているかどうか確認
    voicechannels = guild.voice_channels
    isConnectVoiceChannel = False
    for ch in voicechannels:
        memberList = ch.members
        for m in memberList:
            if m.id == userId:
                isConnectVoiceChannel = True
                break;
    #VC接続されてない場合は弾く
    if not isConnectVoiceChannel:
        return
    
    name = guild.get_member(userId).display_name
    print(datetime.datetime.now() ,name)

    isRecieveCommand = False
    isAllLocation = False
    # メッセージの本文が d だった場合
    if message.content == "d" or message.content == "!drop" or message.content == "/drop":
        isRecieveCommand = True

        
    elif message.content == "da" or message.content == "!drop_all" or message.content == "/drop_all":
        isRecieveCommand = True
        isAllLocation = True

    #コマンドが送信されている場合は処理開始
    if isRecieveCommand:
        #マップデータを取得
        mapdata = getLocation.getLocations()
        #ランダムに選択
        NamedLocation = getLocation.FindNamedLocation(mapdata.data,isAllLocation)
        location = random.choice(NamedLocation)
        x = location.location.x
        y = location.location.y
        z = location.location.z
        #print(location.name,"x:",y,"y:",x)
        # _url = geturl()
        img = getImage.GetImage(mapdata.PoisImage,x,y)
        
        #tmpファイルを保存
        fileName = str(uuid.uuid1()) + ".png"
        fn = "tmp/" + fileName
        img.save(fn,format='png')

        color = RandomColor.getColor()
        #embed作成
        embed = discord.Embed( # Embedを定義する
                          title=name + "さんパーティーの降下場所こちら！",# タイトル
                          color=color, # フレーム色指定(今回は緑)
                          description=location.name, # Embedの説明文 必要に応じて
                          )
        
        # ローカル画像からFileオブジェクトを作成
        file = discord.File(fp=fn,filename=fileName,spoiler=False)
        embed.set_image(url=f"attachment://{fileName}")
        embed.set_footer(text="made by ShinoMegu")
        
        #msg = location.name + " x:" + str(location.location.x), " y:" + str(location.location.y) + " z:" + str(location.location.z)
        #await message.channel.send(msg,file=discord.File(fn))

        await message.channel.send(embed=embed,file=file)

        #tmpファイルを削除
        os.remove(fn)

token = os.getenv('TESTTOKEN')
client.run(token)