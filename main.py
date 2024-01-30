import sys
sys.path.append('/home/cnct/local/python/lib/python3.9/site-packages/discord')
import discord
import random

Intents = discord.Intents.default()
Intents.members = True
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
    print(name)
    # メッセージの本文が 鳴いて だった場合
    if message.content == "!":
        # 送信するメッセージをランダムで決める
        content = name + random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")


client.run("MTIwMTU2NTc0NjE4MzAyODc3Ng.GfyGDT.Wx8QXHUqIyKtL0RnkxQgAshTSYVOgAUM-rnraU")