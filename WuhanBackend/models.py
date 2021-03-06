# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Newsinfo(models.Model):
    newsid = models.CharField(primary_key=True, max_length=64)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    content = models.TextField()
    url = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    theme_label = models.CharField(max_length=255)
    content_label = models.CharField(max_length=255)
    country_label = models.CharField(max_length=255)
    positive = models.FloatField()
    negative = models.FloatField()
    influence = models.FloatField()
    reliability = models.FloatField()
    crisis = models.FloatField()
    persons = models.TextField()
    orgs = models.TextField()
    wjwords = models.TextField()
    nextevent = models.TextField()

    class Meta:
        # managed = False
        db_table = 'newsinfo'


class Othernewsinfo(models.Model):
    newsid = models.CharField(primary_key=True, max_length=64)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    content = models.TextField()
    url = models.CharField(max_length=255)
    imgurl = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    theme_label = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    reliability = models.FloatField()
    crisis = models.FloatField()
    title_zh = models.CharField(max_length=255)
    content_zh = models.TextField()
    persons = models.TextField()
    orgs = models.TextField()

    class Meta:
        # managed = False
        db_table = 'othernewsinfo'


class Viewsinfo(models.Model):
    viewid = models.CharField(primary_key=True, max_length=64)
    personname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    orgname = models.CharField(max_length=255)
    pos = models.CharField(max_length=255)
    verb = models.CharField(max_length=255)
    viewpoint = models.TextField()
    newsid = models.ForeignKey(Newsinfo, models.DO_NOTHING)
    sentiment = models.FloatField()
    time = models.DateTimeField()
    original_text = models.TextField()

    class Meta:
        # managed = False
        db_table = 'viewsinfo'
