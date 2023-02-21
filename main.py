from pytube import YouTube, Playlist
import os,telebot
from moviepy.editor import *


TOKEN = "tokem" 
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()

def sending(file,chatid):
        bot.send_audio(chatid,audio = open(f"{file[:-4]+'.mp3'}", 'rb'),caption=':)',disable_notification=True)


def baixayt(link,id):
    #verifica se o link e de playlist or lista de reprodução
    try:
        p=[Playlist(link)]
        listLink=p[0]
        if len(listLink)==0:
            listLink.append(link)      
    except:
        listLink=[]
        listLink.append(link) 

    #verifica se a pasta em que  download caso n existir a cria
    #if os.path.isfile(os.path.join(os.getcwd(),'music')):#msm tendo pasta e retornado false revisar //////////////////////////
    ff=False
    for f in os.listdir(os.getcwd()): 
        if f=='music':
            ff=True
    if ff:
        pass
    else:
        os.mkdir('music')
    outdir=os.path.join(os.getcwd(),'music')

    #pesquisa e baixa a musica e tbm a converte para mp3 e remove mp4
    for i in listLink:
        yt=YouTube(i)
        hd=yt.streams.filter(only_audio=True,abr='128kbps',).first().download(outdir)
        fileyt =AudioFileClip(hd).write_audiofile(hd[:-4]+'.mp3',verbose=False,progress_bar=False)
        fileyt =AudioFileClip(hd).close()
        os.remove(hd)
        sending(hd,id)



@bot.message_handler(func=lambda messagem:True)
def allmsg(m): 
    link=m.text
    if 'https:/' in link and 'yo' in link:
        baixayt(link,int(m.chat.id))
        try:
            os.system('rm -r music/')#caso tiver usando link
        except:
            os.remove(os.path.join(os.getcwd(),'music'))

print(f'rodandando no bot {user.first_name} .............')
bot.polling()