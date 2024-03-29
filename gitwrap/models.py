from django.db import models

# Create your models here.
class dataSet(models.Model):
    """docstring fordataSet."""
    title   =   models.CharField(max_length=200)
    body    =   models.TextField()
    created_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return self.title
        return '%s %s' % (self.title, self.body)
