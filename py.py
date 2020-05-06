import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("~정보")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith("~정보"):
        await message.channel.send("머락이 개발한 아주 간단한 머락봇입니다 ~명령어를 사용하세요")

    if message.content.startswith("~명령어"):
        await message.channel.send("~정보, ~명령어, ~크루, ~머락유튜브, ~머락트위치")

    if message.content.startswith("~크루"):
        await message.channel.send("현재 머락의 크루 : 쉰김치")

    if message.content.startswith("~머락유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UC7DkGh8P4jJ9RqxS4O3I-Iw")

    if message.content.startswith("~머락트위치"):
       await message.channel.send("https://www.twitch.tv/murrak")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
