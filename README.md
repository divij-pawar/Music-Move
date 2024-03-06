# Apple Music to Spotify <br>
 Some simple python 3 scripts to help import your Apple Music playlists into Spotify playlists. <br >
 
## Usage
### 1. Export Apple Music playlists to HTML File <br >
The first step is to select the playlist you want to import over and download webpage as a html file to the same folder as run.py.<br>

### 2. Install dependencies <br >
Install dependencies using pip
```bash
$ pip install -r requirements.txt
```

### 3. Configure Spotify developer application and variables
1. Go to https://developer.spotify.com/dashboard/applications.
2. Create an app with any name.
3. Select the app.
4. Select **EDIT SETTINGS**.
5. Under **Redirect URIs**, enter `http://localhost:8888/callback` and select **Add**. Select **SAVE**.
6. Find **Client ID** and copy the value to the `client_id` variable in [spotify_accessor.py](./spotify_accessor.py).
7. Select **SHOW CLIENT SECRET**. Copy the value to the `client_secret` variable in [spotify_accessor.py](./spotify_accessor.py).
8. Go to https://spotify.com > **Profile** > **Account**.
9. Copy the value of **Username** to the `username` variable in [spotify_accessor.py](./spotify_accessor.py).
10. Save the edited file.


### 4. Run the program <br >
Run the program by using the terminal and navigating to the directory you cloned this repo into. Type in
```bash
$ python run.py
 ```
 to start the program. Follow the intended dirctions and BAM! Your Apple Music playlists are now Spotify playlists! <br >

### 5. Troubleshooting / Problems / TODO
Incase the song-name/artist/album-name is not getting scraped, modify the attr value to the tag associated with the corresponding value(song-name/artist/album-name) in the html file. This may have happened due to Apple music updating their website.