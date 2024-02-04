import os
import sys
import os
import discord

Intents = discord.Intents.all()
#Intents.members = True
client = discord.Client(intents=Intents)

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
    
    userId = message.author.id
    name = guild.get_member(userId).display_name

    #VCに接続されているかどうか確認
    voicechannels = guild.voice_channels
    isConnectVoiceChannel = False
    for ch in voicechannels:
        memberList = ch.members
        for m in memberList:
            if m.id == userId:
                isConnectVoiceChannel = True
                break;
    
    print(isConnectVoiceChannel)

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
        
        #embed作成
        embed = discord.Embed( # Embedを定義する
                          title=name + "さんパーティーの降下場所こちら！",# タイトル
                          color=0xFF0000, # フレーム色指定(今回は緑)
                          description="location.name", # Embedの説明文 必要に応じて
                          )
        
        # ローカル画像からFileオブジェクトを作成
        embed.set_footer(text="made by ShinoMegu")
        
        #msg = location.name + " x:" + str(location.location.x), " y:" + str(location.location.y) + " z:" + str(location.location.z)
        #await message.channel.send(msg,file=discord.File(fn))

        await message.channel.send(embed=embed)


token = os.getenv('TESTTOKEN')
client.run(token)