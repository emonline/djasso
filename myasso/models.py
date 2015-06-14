from django.db import models
from django.utils.translation import ugettext_lazy as _

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
                            default='',
                            verbose_name=_('role'))
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=11, verbose_name=_('phone'))
    address = models.CharField(max_length=100, verbose_name=_('address'))
    zipcode = models.IntegerField(verbose_name=_('zipcode'))
    city = models.CharField(max_length=50, verbose_name=_('city'))
    accessiondate = models.DateField(verbose_name=_('accesiondate'))
    association = models.ForeignKey(Association)

    def __str__(self):
        return u'%s %s' % (self.last_name,self.first_name)


