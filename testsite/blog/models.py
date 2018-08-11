from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    uid = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.uid = hashlib.md5((self.username + self.email).encode()).hexdigest()
        super(User, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now=True)  # for "last-modified" timestamps!
    gid = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_assign', args=(self.slug, ))


class Report(models.Model):
    title = models.CharField(max_length=100, blank=False, help_text="Report Title")
    contents = models.TextField(blank=False, help_text="Fill out the report.")
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now=True)  # for "last-modified" timestamps!
    uid = models.CharField(max_length=32)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Report, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('report_edit', args=(self.slug, ))

