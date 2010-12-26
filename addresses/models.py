from django.db import models


class Address(models.Model):
    address_1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address Line 1')
    address_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('UsState', blank=True, null=True)
    province = models.ForeignKey('CanadianProvince', blank=True, null=True)
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    country = models.ForeignKey('Country', blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def state_or_province(self):
        return self.state or self.province


from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
        iso = models.CharField(_('ISO alpha-2'), max_length=2, primary_key=True)
        name = models.CharField(_('Official name (CAPS)'), max_length=128)
        printable_name = models.CharField(_('Country name'), max_length=128)
        iso3 = models.CharField(_('ISO alpha-3'), max_length=3, null=True)
        numcode = models.PositiveSmallIntegerField(_('ISO numeric'), null=True)
        
        class Meta:
                verbose_name = _('Country')
                verbose_name_plural = _('Countries')
                ordering = ('name',)
		
        class Admin:
                list_display = ('printable_name', 'iso',)

        @classmethod
        def the_usa(cls):
                try:
                        return Country.__the_usa
                except:
                        Country.__the_usa = Country.objects.get(pk="US")
                        return Country.__the_usa

        def __unicode__(self):
                return self.printable_name


class UsState(models.Model):
        name = models.CharField(_('State name'), max_length=50, null=False)
        id = models.AutoField(primary_key=True)
        abbrev = models.CharField(_('Abbreviation'), max_length=2, null=False)

        class Meta:
                verbose_name = _('US State')
		verbose_name_plural = _('US States')
		ordering = ('name',)

        class Admin:
                list_display = ('name', 'abbrev',)

        def __unicode__(self):
                return self.name


class CanadianProvince(models.Model):
        name = models.CharField(_('Province name'), max_length=50, null=False)
        id = models.AutoField(primary_key=True)
        abbrev = models.CharField(_('Abbreviation'), max_length=2, null=False)

        class Meta:
                verbose_name = _('Canadian Province')
		verbose_name_plural = _('Canadian Provinces')
		ordering = ('name',)

        class Admin:
                list_display = ('name', 'abbrev',)

        def __unicode__(self):
                return self.name

