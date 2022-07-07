from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'artist'
        verbose_name_plural = 'artists'
