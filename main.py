import asyncio
import sys
import string
import discord
import DropBoxUploder
import os

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

    f = open(os.path.dirname(os.path.abspath(__file__)) + "/data.bin",
             mode='r', encoding='UTF-8')

    lines = f.readlines()

    for line in lines:
        data = line.split(':')
        if "\n" in data[1]:
            datalist.append(data[1][:-1].replace("!", ""))
        else:
            datalist.append(data[1].replace("!", ""))

    print(datalist)

    f.close()


def main(argv):
    global messageText
    ReadBotData()

    drop = DropBoxUploder.DropBoxManager(
        datalist[2], argv[2], datalist[3] + argv[1])
    drop.UpLoadFile()
    CreateBuildMessage(argv[1], drop.GetFileLink(), argv[3], argv[4])

    client.run(datalist[0])


def CreateBuildMessage(fileName, downloadLink, version, Buildmessage):
    global messageText

    messageText = ''
    messageText += "새로운 파일이 올라갔습니다.\n"
    messageText += "\n"
    messageText += "파일 이름 : " + fileName + "\n"
    messageText += "다운로드 링크 : " + downloadLink + "\n"
    messageText += "버전 : " + version + "\n"
    messageText += "빌드 메시지 : " + Buildmessage + "\n"

# def SaveBinaryToken():
    # f = open("/Users/shj/Desktop/UnityProject/Project_SHJ/PG_Bot/PGBot/data.txt",
    #          mode='wb')

    # tokenlist = ""
    # tokenlist += "disrdCode:"
    # tokenlist += "channelID:6775699159672224\n"
    # tokenlist += "dropBoxCode:\n"
    # tokenlist += "dropboxUplodePath:/JPER/Build/\n"

    # f.write(tokenlist.encode())


if __name__ == "__main__":
    main(sys.argv)
