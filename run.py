import os
from bs4 import BeautifulSoup
import applemusic_xml_parser as axp
import spotify_accessor as sa

cwd = os.getcwd()
list_dir = os.listdir(cwd)
filtered_list = [element for element in list_dir if element.endswith(".html")]
# print(filtered_list)

for file_name in filtered_list:
    playlist_name = file_name.split(' - Playlist')[0]
    playlist_name = playlist_name[1:]
    print(playlist_name)
    song_list = []
    artist_list = []
    album_list = []
    # print(file_name)
    with open(file_name, mode='r' , encoding='utf-8') as file:
        html_content = file.read()
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements with the specified data-testid attribute
        # REPLACE "attrs" value for each element in case of error #########################################
        song_elements = soup.find_all(attrs={"data-testid": "track-title"})
        artist_elements = soup.find_all(attrs={"songs-list__col songs-list__col--secondary svelte-4lh1r1"})
        album_elements = soup.find_all(attrs={"songs-list__col songs-list__col--tertiary svelte-4lh1r1"})

        # Extract and print the content of each element
        for element in song_elements:
            song_name = element.text.strip().replace("\n", " ")
            song_list.append(song_name)
        # Extract and print the content of each element
            
        for element in artist_elements:
            artist_name = element.text.strip().replace("\n", " ")
            artist_list.append(artist_name)

        for element in album_elements:
            album_name = element.text.strip().replace("\n", " ")
            album_list.append(album_name)
        
        # print(song_list)
        # print("####")
        # print(artist_list)
        # print("####")
        # print(album_list)


    if not (len(song_list) == len(artist_list) and len(artist_list) == len(album_list)):
        print("length mismatch")
    else:
        print("All lengths match")


    song_name = song_list
    final_song_name = axp.remove_feat_from_song(song_name)
    # final_song_name = song_name
    artist_name = artist_list
    album_name = album_list
    final_album_name = album_name
    # final_album_name = axp.remove_feat_from_album(album_name)
    my_playlist_id = sa.create_playlist(playlist_name)
    multiple_tracks, missing_albums, missing_tracks = sa.get_track_id(final_song_name, artist_name, final_album_name)
    more_tracks = sa.get_missing_track_id(missing_albums, missing_tracks)
    all_songs = sa.add_song_ids(multiple_tracks, more_tracks)
    sa.add_songs_playlist(all_songs, my_playlist_id)
    break