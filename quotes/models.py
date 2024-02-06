from django.db import models


class Author(models.Model):
    objects = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Quote(models.Model):
    objects = None
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField()

    def __str__(self):
        return f'{self.text} - {self.author}'





