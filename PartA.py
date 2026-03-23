import random

# Song class
class Song:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year


    def display_info(self):
        print(f"Song: {self.title}, Artist: {self.artist_name}, Year: {self.year}")


class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    # adds a song to the album

    def add_song(self, title, year):
        new_song = Song(title, self.artist_name, year)  # year taken from album
        self.songs.append(new_song)


    def display_info(self):
        print(f"Album: {self.title}, Artist: {self.artist_name}, Year: {self.year}")
        print('Songs:')
        for song in self.songs:
            print(f"  - {song.title}")

# Artist class
class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []
        self.songs = []



    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


    def display_info(self):
        # prints all artist info
        print(f"Artist: {self.name}, DoB: {self.dob}, Country: {self.country}")

        print('Albums:')
        for album in self.albums:
            print(f"  - {album.title}")
        print('Songs:')
        for song in self.songs:
            # print("debug:", song.title)
            print(f"  - {song.title}")


class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print("Playlist: " + self.title)
        for song in self.songs:
            print(f"  - {song.title}")

    # order can be ASC or DES
    def sort_playlist(self, order='ASC'):
        def get_title(s):
            return s.title

        if order == 'ASC':
            self.songs.sort(key=get_title)

        elif order == 'DES':
            self.songs.sort(key=get_title, reverse=True)

    def shuffle_playlist(self):
        random.shuffle(self.songs)  # not sure if this needs a seed or something


if __name__ == "__main__":

    # creat artist
    taylor = Artist("Taylor Swift", "December 13, 1989", "USA")

    # create an album
    album1989 = Album("1989", "Taylor Swift", 2014)


    # create a few songs for the artist
    s1 = Song("Love Story", "Taylor Swift", 2008)
    s2 = Song("You Belong With Me", "Taylor Swift", 2008)
    s3 = Song("Shake It Off", "Taylor Swift", 2014)

    # use add_song from Album to add two songs
    album1989.add_song("Blank Space", 2014)
    album1989.add_song("Style", 2014)

    # use add_album and add_song to update artist info
    taylor.add_album(album1989)
    taylor.add_song(s1)
    taylor.add_song(s2)
    taylor.add_song(s3)

    taylor.display_info()
    print()
    album1989.display_info()
    print()
    s1.display_info()
    print()

    # make a playlist
    playlist = Playlist("My Taylor Playlist")
    for song in album1989.songs:
        playlist.add_song(song)
    # add a couple extra
    playlist.add_song(s1)
    playlist.add_song(s2)
    #playlist.add_song(s3)

    print("Playlist before sorting:")
    playlist.print_all_song()
    print()


    playlist.sort_playlist('ASC')
    print("Sorted ASC:")
    playlist.print_all_song()
    print()

    playlist.sort_playlist('DES')
    print("Sorted DES:")
    playlist.print_all_song()
    print()


    # shuffle the playlist
    playlist.shuffle_playlist()
    print("After shuffle:")
    playlist.print_all_song()