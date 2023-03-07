from pytube import YouTube, Playlist
import os
from moviepy.editor import *


def baixayt(link):
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
        print(0)
        fileyt =AudioFileClip(hd).write_audiofile(hd[:-4]+'.mp3',verbose=False,progress_bar=False)
        fileyt =AudioFileClip(hd).close()
        os.remove(hd)





def allmsg(m): 
    link=m
    if 'https:/' in link and 'yo' in link:
        baixayt(link)
while True:
    g=allmsg(input('link'))
    if g =='000':
        break
