from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, unique=True, null=False)
    last_name = models.CharField(max_length=50, unique=True, null=False)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return f'{self.tag}'


class Quote(models.Model):
    text = models.TextField(max_length=500, unique=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.text} - {self.author}'


class ScrapData(models.Model):
    choice = models.CharField(max_length=10)
    dictionary = models.JSONField()

    def __str__(self):
        return f'{self.dictionary}'





