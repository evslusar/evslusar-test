from django.db import models


class Person(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    biography = models.TextField()

    def __unicode__(self):
        return '%s %s' % (self.firstname, self.lastname,)
