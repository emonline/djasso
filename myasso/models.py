from django.db import models

class Association(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    logo = models.URLField()
    website = models.URLField()
    serialnumber = models.IntegerField(default=0)
    creationdate = models.DateField()

    def __str__(self):
        return self.name


class Adherent(models.Model):
    ROLE_CHOICES = (
        ('President', 'President'),
        ('Secretaire', 'Secretaire'),
        ('Tresorier', 'Tresorier'),
        ('', ''),
    )
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES,
                            default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)
    accessiondate = models.DateField()
    association = models.ForeignKey(Association)

    def __str__(self):
        return u'%s %s' % (self.last_name,self.first_name)


