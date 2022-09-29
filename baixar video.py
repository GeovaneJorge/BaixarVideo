import youtube_dl
import sys
import os

link = input('Digite o link do youtube: ')

################ video e audio ##################

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

################## FIM ######################




############## somente audio ###################
'''
ydl = youtube_dl.YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
})
'''
################## FIM ######################




with ydl:
    result = ydl.extract_info(link, download=True) 


if 'entries' in result:
    video = result['entries'][0]
else:
    video = result

#print(video)
video_url = video['url']
#print(video_url)