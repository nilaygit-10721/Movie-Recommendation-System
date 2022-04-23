from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    vote_count= models.IntegerField()
    vote_avg = models.FloatField()
    genre = models.CharField(max_length=255)
    movie_img_url = models.URLField()
    release_date = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return self.title




