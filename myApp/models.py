from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=50)

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	group = models.ForeignKey(Group)

	def group_letter(self):
		return self.group.name[0].upper()

	def full_name(self):
		return '%s %s '%(self.first_name, self.last_name)


