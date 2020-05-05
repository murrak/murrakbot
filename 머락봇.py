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
        await message.channel.send("~정보, ~명령어, ~크루")

    if message.content.startswith("~크루"):
        await message.channel.send("현재 머락의 크루 : 쉰김치")


client.run("NzA2MTA2MDc1MzYyODg1Njk0.Xq1bEA.paxJmPpQzYXo9ERJ73Z82VvaIzY")