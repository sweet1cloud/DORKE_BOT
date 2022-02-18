#도르크봇 정식 출시!
#참고 자료: https://github.com/Ryzen72700/thecircle_prj/blob/master/tc_github.py
#참고 자료22: https://github.com/Ryzen72700/DISCORDPY_Aria/blob/master/Aria_Public.py
#봇에 다양한 기능을 많이 넣었습니다. 간단한 챗봇의 기능을 무사히 수행할 수 있도록 하겠습니다! (그냥 뻘짓봇이 확실하다)
#봇의 업데이트 내역은 현재 보고 계시는 레포지토리의 "update.md" 문서를 확인하시면 됩니다.
#도움을 주신 분: 기우
#2020-06-21 대규모 업데이트
#2020-06-22 추가 업데이트
#도르크봇 2.0도 추후 개발 예정입니다.
#2021년 8월 28일 discord.py의 개발 및 서비스 종료
#2022-02-17 discord.py → nextcord (https://github.com/nextcord/nextcord)
#아래 내용부터 봇의 코드입니다.
#----------------------------
import discord, asyncio, random, datetime, time
from nextcord.ext import commands

uid = discord_user_id #'discord_user_id' 부분에다가 본인의 디스코드 ID를 입력하세요.
token = "bot_token" #'bot_token' 부분에다가 봇 토큰을 입력하세요.
app = commands.Bot(command_prefix='d#')

@app.event
async def on_ready():
    print("Fix. 191210 | Last 20220217 ver.")
    print("")
    print("■■■■■■■■■■■■■■■[ I  N  F  O ]■■■■■■■■■■■■■■■")
    print("")
    print(">> Sourced By The Circle! ProJect, Aria_Public ProJect")
    print("")
    print("■■■■■■■■■■■■■■■[ B O T -  b o o t i n g  - C O M P L E T E ! ]■■■■■■■■■■■■■■■")
    print("")
    print("Copyright 도르크봇 (DORKE BOT) All Rights Reserved.")
    print("")
    print("BOT ID :")
    print(app.user.id)
    print("이 메시지가 뜬다면 봇 디버깅에 성공한 것입니다.")
    game = discord.Game("[d#도움말]도르크봇을 불러보세요!")
    await app.change_presence(status=discord.Status.online, activity=game)
    channel = app.get_channel(709228507540095028) #도르크 프로젝트 봇-로그 채널 ID
    await channel.send('봇켜짐')

@app.command(pass_context=True)
async def 도움말(ctx):
    embed = discord.Embed(
            title="도움말",
            description="> 도르크봇 1.0 버전을 이용해주셔서 감사합니다!\n> 봇 공식 페이지에서 봇 명령어를 확인하실 수 있습니다!\n ```Bot Running Information \n 현재 돌아가고 있는 곳 : 개발자 컴퓨터에서 구동 중입니다! (24시간 X)\n 프로그래밍 언어 : Python 3.8.8 64-bit (With VSCode, nextcord)```\n```공지 시스템: DPNK\n봇 소스: The Circles! ProJect, Aria_Public ProJect\n(라이선스 위반 없이 사용 중.)```\n```d#도움말 - 현재 명령어\nd#ping - 클라이언트 지연 시간(핑) 확인\nd#invite - 봇 초대코드\nd#랜덤로고 - 랜덤으로 로고를 보여줍니다.\nd#반응 - 여러가지 감정 반응이 있어요!```\n``개발자 디스코드 프로필 보기``:[링크](https://discord.com/users/284143521886109697) \n``봇 공식 페이지``: [도르크봇 깃헙](https://github.com/sweet1cloud/DORKE_BOT) \n``봇 참고 레포지트리``: [The Circles! Project](https://github.com/Ryzen72700/thecircle_prj/blob/master/tc_github.py), [Aria_Public ProJect](https://github.com/Ryzen72700/DISCORDPY_Aria/blob/master/Aria_Public.py)\n``개발자 유튜브``: [YouTube](https://www.youtube.com/channel/UC1v2JDiftMw7epyndnVA_Bg)\n``이메일``: idoyun027@gmail.com",
            timestamp=datetime.datetime.now(),
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
            description="Bot shutdown... Goodbye :wave:",
            color=0xFF0000
        )
        await ctx.send(embed=embed)
        await app.close()
    else:
        embed = discord.Embed(
            title=":warning: 경고",
            description=" 현재 해당 명령어를 사용할 수 있는 권한은 봇 소유자밖에 없습니다.\n개발자에게 문의를 해주세요."
        )
        await ctx.send(embed=embed)

@app.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(
            title=":e_mail: 초대하기!",
            description="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=702477692402008094&permissions=8&scope=bot)\n봇 초대가 안된다면 [여기](https://discord.com/users/284143521886109697)로 디스코드 DM 보내주세요.",
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
    str = ['와','상상도못함','dyd', '놀람', 'hello', '당황', 'thinking', 'why', '바보', '멍청이', 'ㅁㄴㅇㄹ', 'simsimhanga', '심심해']
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
    elif r == '바보':
        await ctx.send("어ㅡ허")
    elif r == '멍청이':
        await ctx.send("어1허")
    elif r == 'ㅁㄴㅇㄹ':
        await ctx.send("ㅁㄴㅇㄹ")
    elif r == 'simsimhada':
        await ctx.send("심심하다 **★**")

@commands.has_permissions(manage_messages=True) #명령어 사용대상이 메시지 관리 역할이 있는가?
@app.command(name="clean", pass_context=True)
async def clean(ctx, ro):
    await ctx.channel.purge(limit=int(ro)) #라인 채팅청소
    await ctx.channel.send("<@" + str(ctx.message.author.id) + "> 님이 채팅을 청소하셨습니다.") #채팅청소 안내

@clean.error
async def clean_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("삭제할 수를 넣으시지 않으셨습니다.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("당신은 메시지 관리 권한이 없어 채팅청소가 불가합니다.")

@app.command(pass_context=True)
async def 도배(ctx):
    embed = discord.Embed(
            title="도배",
            description="도배",
            color=0x99EAF5
        )
    await ctx.send(embed=embed)

#임시 비활성화
#@app.event
#async def on_message(message):
    #if message.content.startswith("d#정보"):
        #date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        #embed = discord.Embed(color=0x00ff00)
        #embed.add_field(name="이름", value=message.author.name, inline=True)
        #embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        #embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        #embed.add_field(name="아이디", value=message.author.id, inline=True)
        #embed.set_thumbnail(url=message.author.avatar_url)
        #await message.channel.send(embed=embed)

app.run(token)
