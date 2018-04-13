from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

class DegreeCourse(models.Model):
    name = models.CharField(max_length=32)
    policy_list = GenericRelation("PricePolicy")

class Course(models.Model):
    name = models.CharField(max_length=32)
    policy_list = GenericRelation("PricePolicy")

class PricePolicy(models.Model):
    period = models.CharField(max_length=32)
    price = models.FloatField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')