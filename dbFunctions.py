import json

# Making a function to add a new song to the JSON data
def add_song(json_data, song_name, artist, album, duration, wpm, spanish_lyrics, english_lyrics):
    new_song = {
        "songName": song_name,
        "artist": artist,
        "album": album,
        "duration": duration,
        "wpm": wpm,
        "spanishLyrics": spanish_lyrics,
        "englishLyrics": english_lyrics
    }
	# Here we are appending the new song object to the existing array
    json_data["songs"].append(new_song)

# Loading existing JSON data from the file, checking it it exists, if it doesn't we create a new structure
try:
    with open("songs.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {
        "songs": []
    }

# Save the updated JSON data to the file
with open("write.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
