from django.db import models

# Create your models here.
class BooksLocations(models.Model):
    id=models.IntegerField(primary_key=True)
    from_rack_number=models.IntegerField()
    to_rack_number=models.IntegerField()
    location=models.CharField(max_length=100)


class BooksDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    availability_status=models.BooleanField(default=True)
    no_of_issue_copies=models.IntegerField()
    rack_number=models.IntegerField()
    location_id=models.ForeignKey(BooksLocations,on_delete=models.CASCADE,related_name="books")
    popularity_rating=models.IntegerField()