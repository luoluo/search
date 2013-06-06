from django.db import models
class Cars(models.Model):
	Name = models.CharField(max_length = 30)
	Price = models.IntegerField()


	def __unicode__(self):
		return "%s %d" % (self.Name, self.Price)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


#	**def __unicode__(self):**
#        **return self.name**
