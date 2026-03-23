import unittest
from PartA import Artist, Song, Album, Playlist


class TestInstanceOf(unittest.TestCase):

    def test_artist_instance(self):
        artist = Artist("Taylor Swift", "December 13, 1989", "USA")
        self.assertIsInstance(artist, Artist)


    def test_song_instance(self):
        song = Song("Blank Space", "Taylor Swift", 2014)
        self.assertIsInstance(song, Song)

    def test_album_instance(self):
        album = Album("1989", "Taylor Swift", 2014)
        self.assertIsInstance(album, Album)



    def test_playlist_instance(self):
        playlist = Playlist("My Playlist")
        self.assertIsInstance(playlist, Playlist)


class TestNotInstanceOf(unittest.TestCase):

    def test_artist_not_song(self):
        artist = Artist("Taylor Swift", "December 13, 1989", "USA")
        self.assertNotIsInstance(artist, Song)

    def test_song_not_album(self):
        song = Song("Blank Space", "Taylor Swift", 2014)
        self.assertNotIsInstance(song, Album)

    def test_album_not_playlist(self):
        album = Album("1989", "Taylor Swift", 2014)
        self.assertNotIsInstance(album, Playlist)

    def test_playlist_not_artist(self):
        playlist = Playlist("My Playlist")
        self.assertNotIsInstance(playlist, Artist)


class TestIdentical(unittest.TestCase):


    def test_identical_objects(self):
        song = Song("Style", "Taylor Swift", 2014)
        same_song = song  # same object, not a copy
        self.assertIs(song, same_song)

    def test_not_identical_objects(self):
        ##two seperate objects even if they have the same data
        song1 = Song("Style", "Taylor Swift", 2014)
        song2 = Song("Style", "Taylor Swift", 2014)
        self.assertIsNot(song1, song2)


class TestAddMethods(unittest.TestCase):

    def test_album_add_song(self):
        album = Album("1989", "Taylor Swift", 2014)
        album.add_song("Blank Space", 2014)
        self.assertEqual(len(album.songs), 1)
        self.assertEqual(album.songs[0].title, "Blank Space")

    def test_playlist_add_song(self):
        playlist = Playlist("Test Playlist")
        song = Song("Style", "Taylor Swift", 2014)
        playlist.add_song(song)
        self.assertEqual(len(playlist.songs), 1)


    def test_artist_add_song(self):
        artist = Artist("Taylor Swift", "December 13, 1989", "USA")
        song = Song("Shake It Off", "Taylor Swift", 2014)
        artist.add_song(song)
        self.assertEqual(len(artist.songs), 1)

    def test_artist_add_album(self):
        artist = Artist("Taylor Swift", "December 13, 1989", "USA")
        album = Album("1989", "Taylor Swift", 2014)
        artist.add_album(album)
        self.assertEqual(len(artist.albums), 1)


class TestPlaylistSorting(unittest.TestCase):

    def test_sort_ascending(self):
        playlist = Playlist("Test")
        playlist.add_song(Song("Style", "Taylor Swift", 2014))
        playlist.add_song(Song("Blank Space", "Taylor Swift", 2014))
        playlist.add_song(Song("Shake It Off", "Taylor Swift", 2014))
        playlist.sort_playlist('ASC')
        titles = []
        for s in playlist.songs:
            titles.append(s.title)
        self.assertEqual(titles, ["Blank Space", "Shake It Off", "Style"])


    def test_sort_descending(self):
        playlist = Playlist("Test")
        playlist.add_song(Song("Style", "Taylor Swift", 2014))
        playlist.add_song(Song("Blank Space", "Taylor Swift", 2014))
        playlist.add_song(Song("Shake It Off", "Taylor Swift", 2014))
        playlist.sort_playlist('DES')
        titles = []
        for s in playlist.songs:
            titles.append(s.title)
        self.assertEqual(titles, ["Style", "Shake It Off", "Blank Space"])

    # just check all songs still there after shuffle
    def test_shuffle(self):
        playlist = Playlist("Test")
        playlist.add_song(Song("Style", "Taylor Swift", 2014))
        playlist.add_song(Song("Blank Space", "Taylor Swift", 2014))
        playlist.add_song(Song("Shake It Off", "Taylor Swift", 2014))
        original = []
        for s in playlist.songs:
            original.append(s.title)
        playlist.shuffle_playlist()
        shuffled = []
        for s in playlist.songs:
            shuffled.append(s.title)
        self.assertEqual(sorted(original), sorted(shuffled))




if __name__ == '__main__':
    unittest.main()