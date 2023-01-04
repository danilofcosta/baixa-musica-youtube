from pytube import YouTube, Playlist
import moviepy.editor as mp
import re, os ,time
from tqdm import tqdm as q

def baixarmusic(path,link):   
    print('INICIANDO ')
    if 'playlist' in link:
        print('INICIANDO Download DA Playlist')
        yt=Playlist(link)
        for music in q(yt):
            k = YouTube(music)
            ys = k.streams.filter(only_audio=True).first().download(path)
    else:
        yt = YouTube(link)
        print(f'INICIANDO Download DA MUSICA {yt.title}')
        for i in q(range(100)):
            ys = yt.streams.filter(only_audio=True).first().download(path)


    print('INICIANDO conversão da musica =>',yt.title)
    for file in os.listdir(path):                 
        if re.search('mp4', file):                                    
            mp4_path = os.path.join(path , file)  
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') 
            new_file = mp.AudioFileClip(mp4_path) 
            new_file.write_audiofile(mp3_path)    
            os.remove(mp4_path)                 
    print("Download Completo")


def pasta_out():
    arquivo = '.\\music\\'
    if os.path.exists(arquivo):
        print('O caminho {} existe'.format(arquivo))
    else:
        os.mkdir('music')

pasta_out()
path='.\\music\\'


while True:
    f=str(input('Link da musica : '))
    if f == '999':
        print('saindo.........')
        break
    else:
        baixarmusic(path,f)
    os.system('msg * "MUSICAS BAIXADAS"')
    time.sleep(5)
    os.system('cls')
