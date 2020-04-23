from django.db import models

# Create your models here.

class Artist(models.Model):
    
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='media/artist/images/')

	
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    

def song_directory_path(instance, filename):
    
    return f"music/songs/{instance.id}_{instance.name}_{filename}"


class Song(models.Model):

    name = models.CharField(max_length=200)
    song_file = models.FileField(null=True, upload_to='media/songs/')
    artists = models.ManyToManyField(Artist, related_name="songs")

    def __str__(self):
        artists_str = ""
        artists = list(self.artists.all())
        if len(artists) == 0:
            return f"{self.name}"
        artists_str = f"{artists[0].name}"
        for artist in artists[1:]:
            artists_str += f", {artist.name}"
        return f"{self.name} by {artists_str}"

    def __repr__(self):
        return self.__str__() 
