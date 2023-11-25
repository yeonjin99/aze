from django.db import models

# Create your models here.


class Board(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=2000)
    write_date = models.DateTimeField()

    def __str__(self):
        return str({"writer": self.writer,
                    "title":self.title,
                    "content":self.content,
                    "write_date":self.write_date})