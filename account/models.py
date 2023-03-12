from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='account_book')
    price = models.BigIntegerField(default=100)
    published_date = models.DateField()
    copy_sold = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return f"{self.book_title} By {self.author.first_name} {self.author.last_name}"
