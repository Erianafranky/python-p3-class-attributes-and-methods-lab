class Song:
    #class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    #instantiates with a name, artist, and genre
    def __init__ (self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        #Song.count += 1

    #counts the total number of Song objects
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    #keeps track of all Song genres
    @classmethod
    def add_to_genres(cls, genre):
        Song.genres.append(genre)
    
    #keeps track of all Song artists
    @classmethod
    def add_to_artists(cls, artist):
        Song.artists.append(artist)
    
    #keeps count of Songs for each genre.
    def add_to_genre_count(self, genre):
        if Song.genre_count.get(genre):
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
    
    #keeps count of Songs for each artist
    def add_to_artist_count(self, artist):
        if Song.artist_count.get(artist):
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
