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
    channel = client.get_channel(663726361738739712)
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
    
    # argv_test = ["","SHJ(200211)_1,0,0,0_2.apk","/Users/shj/Desktop/UnityProject/Project_SHJ/build/SHJ(200211)_1,0,0,0_2.apk","1,0,0,0"]

    drop = DropBoxUploder.DropBoxManager("3O3J4VcCmqAAAAAAAAAAlX6c1yOPi7GjI29eN61gTuVweKtqmyK91QE4P8GngM_H", argv[2],"/PG/Build/" + argv[1])
    drop.UpLoadFile()
    CreateBuildMessage(argv[1],drop.GetFileLink(),argv[3])
    # CreateBuildMessage("test","test","test")
    client.run('NjYzNjgyNTgyNDU3NjE0MzM2.XkKbWQ.dqMkOX3pdL_YC2rlgXp9HEOItAo')


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

