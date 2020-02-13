import asyncio
import sys
import string
import discord
import DropBoxUploder

client = discord.Client()
messageText = 'none message'
@client.event
async def on_ready():
    global messageText

    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel(677569915963572224)
    await channel.send(embed=discord.Embed(description = messageText))
    await client.logout()
    print('----------------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await  message.channel.send('test!!!!')
 
    elif message.content.startswith('!say'):
        await  message.channel.send('leave message')
        msg = await client.wait_for_message(timeout=15.0, author=message.author)
 
        if msg is None:
            await  message.channel.send('15초내로 입력해주세요. 다시시도: !say')
            return
        else:
            await  message.channel.send(msg.content)
 
def main(argv):
    global messageText

    drop = DropBoxUploder.DropBoxManager("3O3J4VcCmqAAAAAAAAAAfiA8-aVNhApM-SiG_3MIT952sJYOJCznK_gHexTMtB3m", argv[2],"/JPER/Build/" + argv[1])
    drop.UpLoadFile()
    CreateBuildMessage(argv[1],drop.GetFileLink(),argv[3])

    client.run('Njc3NTcwMTU5NTIyODczMzc0.XkWKzg.dPOoJsFOQOQYG9dGhb5jAdXBTGg')


def CreateBuildMessage(fileName,downloadLink,version):
    global messageText

    messageText = ''
    messageText += "새로운 파일이 올라갔습니다.\n"
    messageText += "\n"
    messageText += "파일 이름 : " + fileName + "\n" 
    messageText += "다운로드 링크 : " + downloadLink + "\n"
    messageText += "버전 : " + version + "\n"

if __name__ == "__main__":
    main(sys.argv)

