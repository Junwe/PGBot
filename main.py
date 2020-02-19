import asyncio
import sys
import string
import discord
import DropBoxUploder

client = discord.Client()
messageText = 'none message'
datalist = []


@client.event
async def on_ready():
    global messageText

    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel(int(datalist[1]))
    await channel.send(embed=discord.Embed(description=messageText))
    await client.logout()
    print('----------------')


def ReadBotData():
    global datalist
    f = open("/Users/shj/Desktop/UnityProject/Project_JPER/JPER_Bot/PGBot/data.bin",
             mode='r', encoding='UTF-8')

    lines = f.readlines()

    for line in lines:
        data = line.split(':')
        if "\n" in data[1]:
            datalist.append(data[1][:-1])
        else:
            datalist.append(data[1])

    print(datalist)

    f.close()


def main(argv):
    global messageText
    ReadBotData()

    drop = DropBoxUploder.DropBoxManager(
        datalist[2], argv[2], datalist[3] + argv[1])
    drop.UpLoadFile()
    CreateBuildMessage(argv[1], drop.GetFileLink(), argv[3])

    client.run(datalist[0])


def CreateBuildMessage(fileName, downloadLink, version):
    global messageText

    messageText = ''
    messageText += "새로운 파일이 올라갔습니다.\n"
    messageText += "\n"
    messageText += "파일 이름 : " + fileName + "\n"
    messageText += "다운로드 링크 : " + downloadLink + "\n"
    messageText += "버전 : " + version + "\n"


def EncryptionToken(code):
    for s in code:
        code


def SaveBinaryToken():

    f = open("/Users/shj/Desktop/UnityProject/Project_JPER/JPER_Bot/PGBot/data.bin",
             mode='wb')

    tokenlist = ""
    tokenlist += "discordCode:Njc3NTcwMTU5NTIyODczMzc0.Xky7SQ.mFJ-y04Sb1GLdYBOUF8gygmNH4k\n"
    tokenlist += "channelID:677569915963572224\n"
    tokenlist += "dropBoxCode:3O3J4VcCmqAAAAAAAAAAqteidViPilrvA7dc826_k9Ym1lWmdtWvQI9ES22QWJvU\n"
    tokenlist += "dropboxUplodePath:/JPER/Build/\n"

    f.write(tokenlist.encode())

if __name__ == "__main__":
    main(sys.argv)
