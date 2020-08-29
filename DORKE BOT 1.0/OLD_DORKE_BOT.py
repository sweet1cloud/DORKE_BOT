#도르크봇 정식 출시!
#참고 자료: https://github.com/Ryzen72700/thecircle_prj/blob/master/tc_github.py
#참고 자료22: https://github.com/Ryzen72700/DISCORDPY_Aria/blob/master/Aria_Public.py
#봇에 다양한 기능을 많이 넣었습니다. 간단한 챗봇의 기능을 무사히 수행할 수 있도록 하겠습니다! (그냥 뻘짓봇이 확실하다)
#봇의 업데이트 내역은 현재 보고 계시는 레포지토리의 "update.md" 문서를 확인하시면 됩니다.
#도움을 주신 분: 기우
#2020-06-21 대규모 업데이트
#2020-06-22 추가 업데이트
#아래 내용부터 봇의 코드입니다.
#2020년 8월 5일부터 기존 도르크봇의 소스를 갈아엎기로 했습니다. 현재 보고 계신 코드들은 이제부터 사용되지 않을 예정입니다.
#----------------------------
import discord, asyncio, random, datetime, time, os, tasks
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

uid = discord_user_id #'discord_user_id' 부분에다가 본인의 디스코드 ID를 입력하세요.
token = "bot_token" #'bot_token' 부분에다가 봇 토큰을 입력하세요.
app = commands.Bot(command_prefix='d#')

@app.event
async def on_ready():
    print("LOADING...")
    print("Fix. 191210 | Last Update 20200829 ver.")
    print("")
    print("■■■■■■■■■■■■■■■[ I  N  F  O ]■■■■■■■■■■■■■■■")
    print("")
    print(">> Sourced By The Circle! ProJect, Aria_Public ProJect")
    print("[INFO] Loading...")
    print("[INFO] Bot Commands Loading Complete!")
    print("")
    print("■■■■■■■■■■■■■■■[ B O T -  b o o t i n g  - C O M P L E T E ! ]■■■■■■■■■■■■■■■")
    print("")
    print("Copyright 도르크봇 (DORKE BOT) All Rights Reserved.")
    print("")
    print("BOT ID :")
    print(app.user.id)
    print("이 메시지가 뜬다면 봇 디버깅에 성공한 것입니다.")
    game = discord.Game("[d#help]도르크봇을 불러보세요!")
    await app.change_presence(status=discord.Status.online, activity=game)
@app.command(pass_context=True)
async def 도움말(ctx):
    embed = discord.Embed(
            title="도움말",
            description="> 도르크봇 1.0 버전을 이용해주셔서 감사합니다!\n> 봇 공식 페이지에서 봇 명령어를 확인하실 수 있습니다!\n ``봇 공식 페이지:`` [도르크봇 깃헙](https://github.com/sweet1cloud/DORKE_BOT)\n ```Bot Running Information \n 현재 돌아가고 있는곳 : 개발자 컴퓨터에서 구동 중입니다!(24시간 X) \n 프로그래밍 언어 : Python 3.7.0 32-bit (With VSC)``` \n```공지 시스템: DPNK\n봇 소스: The Circles! ProJect, Aria_Public ProJect\n(라이센스 위반 없이 사용중.)```\n ```개발자 연락처: 디스코드: Sweet_Cloud#9892, \n이메일: idoyun027@gmail.com```\n```help - DM으로 전송\n도움 - 서버 채팅 채널에 전송```\n``봇 참고 레포지트리:`` [the circle prj](https://github.com/Ryzen72700/thecircle_prj/blob/master/tc_github.py)\n ``봇 참고 레포지트리:`` [Aria prj](https://github.com/Ryzen72700/DISCORDPY_Aria/blob/master/Aria_Public.py)\n``개발자 유튜브``: [youtube](https://www.youtube.com/channel/UC1v2JDiftMw7epyndnVA_Bg)",
            timestamp=datetime.datetime.utcnow(),
            color=0x99EAF5
        )
    await ctx.channel.send(embed=embed)
    
@app.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(
            title=":ping_pong: 클라이언트 지연 시간 (단위 : ms)",
            description="현재 당신의 핑은 **" + str(int(app.latency * 1000)) + "ms** 예요.",
            timestamp=datetime.datetime.utcnow(),
            color=0xAAF599
        )
    await ctx.send(embed=embed)

@app.command(pass_context=True)
async def shutdown(ctx):
    if str(ctx.message.author.id) == "284143521886109697":
        embed = discord.Embed(
            title="Shutdown!",
            description="Bot shutdown... bye bye :wave:",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        await app.close()
    else:
        embed = discord.Embed(
            title=":warning: 경 고",
            description="  현재 해당 명령어를 사용할 수 있는 권한은 봇 소유자밖에 없습니다.\n개발자에게 문의를 해주세요."
        )
        await ctx.send(embed=embed)

@app.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(
            title=":e_mail: 초대하기!",
            description="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=702477692402008094&permissions=8&scope=bot)\n```봇 초대가 안된다면 DORKE_Σ#9892로 디스코드 DM 보내주세요.```",
            color=0x99EAF5
        )
    await ctx.send(embed=embed)

@app.command(pass_context=True)
async def 랜덤로고(ctx):
    str = ['YOUTUBE 로고', 'DISCORD 로고', 'TWITCH 로고', 'NAVER 로고', 'CHROME']
    r = random.choice(str)
    if r == 'YOUTUBE 로고':
        await ctx.send("https://cdn.discordapp.com/attachments/694152174409613333/698068155037122640/youtube.png")
    elif r == 'DISCORD 로고':
        await ctx.send("https://cdn.discordapp.com/attachments/694152174409613333/701757309403136010/discord.png")
    elif r == 'TWITCH 로고':
        await ctx.send("https://cdn.discordapp.com/attachments/694152174409613333/709948886457909318/twitch.png")
    elif r == 'NAVER 로고':
         await ctx.send("https://cdn.discordapp.com/attachments/694152174409613333/695922600089485312/NAVER.png")
    elif r == 'CHROME':
         await ctx.send("https://cdn.discordapp.com/attachments/693721629808787477/694079206472024065/god_chrome.png")

@app.command(pass_context=True)
async def 반응(ctx):    
    str = ['와','상상도못함','dyd', '놀람', 'hello', '당황', 'thinking', 'why', 'dqd', '바보', '멍청이', 'ㅁㄴㅇㄹ', 'simsimhada', 'simsimhanga', '심심해', '도르크']
    r = random.choice(str)
    if r == '와':
        await ctx.send("샌즈")
    elif r == '상상도못함':
        await ctx.send("ㄴㅇㄱ")
    elif r == 'dtd':
        await ctx.send("ㅇㅅㅇ")
    elif r == '놀람':
         await ctx.send("ㄷㄷ")
    elif r == 'hello':
         await ctx.send("반가워요! :wave:")
    elif r == '당황':
        await ctx.send(";;")
    elif r == 'thinking':
        await ctx.send(":thinking:")
    elif r == 'why':
        await ctx.send("외않됀데?")
    elif r == 'dqd':
        await ctx.send("ㅇㅂㅇ")
    elif r == '바보':
        await ctx.send("어ㅡ허")
    elif r == '멍청이':
        await ctx.send("어1허")
    elif r == 'ㅁㄴㅇㄹ':
        await ctx.send("ㅁㄴㅇㄹ")
    elif r == 'simsimhada':
        await ctx.send("SIMSIMHADA **★**")
    elif r == 'simsimhanga':
        await ctx.send("https://discord.gg/wkPDgyg")
    elif r == '심심해':
        await ctx.send("```저랑 가위바위보 게임 하실래요?```\n```d#가위바위보 명령어로 가위바위보 게임이 가능합니다!```")
    elif r == '도르크':
        await ctx.send("https://discord.gg/9Q6Z9p2")

app.run(token)
