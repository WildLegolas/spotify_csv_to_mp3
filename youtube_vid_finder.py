# coding=utf8
from youtubesearchpython import Search
import pandas as pd
import numpy as np

search_query_test = 'Кончится Лето Kino'

def find_first_vid(search_query):

    allSearch = Search(search_query, limit = 1)

    result_dict = allSearch.result()
    result_dict2 = list(result_dict.values())[-1]
    result_dict3 = result_dict2[-1]
    result_dict4 = list(result_dict3.values())[-2]

    return result_dict4




df_songs = pd.read_csv('song_links_results.csv', encoding='utf8')
df_list_songs = df_songs.values.tolist()
song_list = []

for i in df_list_songs:
    song_list.append(i[1])

from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url,outdir):
    # url input from user
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')





'''
for song in song_list[1619:]:
    print(song_list.index(song))
    try:
        youtube2mp3(song,'dirpath')
    except FileExistsError:
        continue
    except AttributeError:
        continue
    except KeyError:
        continue








df_convert = pd.read_csv('converted_spotify_music_list.csv', encoding='utf8')
#df.apply(lambda x: pd.lib.infer_dtype(x.values))

df_titles_artists = df_convert[['Track Name','Artist Name(s)']]
df_titles_artists.astype(str)
df_titles_artists["separator"] = '-'


df_titles_artists["combined_col"] = df_titles_artists["Track Name"] + df_titles_artists["separator"] + df_titles_artists["Artist Name(s)"]

df_combined = df_titles_artists["combined_col"]

print(df_combined)
df_combined = df_combined.dropna(axis=0)
titles_artists_list = df_combined.values.tolist()

#print(titles_artists_list)

song_link_list = []
#titles_artists_list_subset = titles_artists_list[0:50]
titles_artists_list_subset = titles_artists_list
for song in titles_artists_list_subset:
    print('trying:',song)
    result_link = find_first_vid(song)
    song_link_list.append(result_link)


df_song_links = pd.DataFrame(song_link_list)

df_song_links.to_csv('song_links_results.csv', encoding='utf-8')

'''