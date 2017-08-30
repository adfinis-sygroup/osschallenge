import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=50)
    required_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Groups(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.group


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, default=1)
    points = models.IntegerField(default=0)
    links = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    key = models.CharField(max_length=10, unique=True)
    picture = ThumbnailerImageField(upload_to='profile-pictures', null=True)

    def get_rank(self):
        matches = Rank.objects.filter(required_points__lte=self.points).order_by('-required_points')
        return matches[0]

    def fileurl(self):
        return settings.MEDIA_URL + os.path.basename(self.picture['avatar'].name)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'),)
    lead_text = models.CharField(max_length=300, verbose_name=_('Lead text'),)
    description = models.CharField(max_length=5000,
                                   verbose_name=_('Description'),)
    licence = models.CharField(max_length=50, verbose_name=_('Licence'),)
    website = models.CharField(max_length=50, verbose_name=_('Website'),)
    github = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name="project_owner",
                              verbose_name=_('Owner'),)
    mentors = models.ManyToManyField(User, related_name="project_mentors",
                                     verbose_name=_('Mentors'),)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'),)
    lead_text = models.CharField(max_length=300, verbose_name=_('Lead text'),)
    description = models.CharField(max_length=5000,
                                   verbose_name=_('Description'),)
    mentors = models.ManyToManyField(User, related_name="task_mentors",
                                    verbose_name=_('Mentors'),)
    project = models.ForeignKey(Project, related_name="tasks")
    assignee = models.ForeignKey(User, null=True,
                                 related_name="assignee_tasks",
                                 verbose_name=_('Assignee'),)
    task_done = models.BooleanField(null=False, default=False)
    task_checked = models.BooleanField(null=False, default=False)
    picture = ThumbnailerImageField(upload_to='', null=True)

    def fileurl(self):
        return settings.MEDIA_URL + os.path.basename(self.picture['avatar'].name)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task)
    comment = models.TextField(max_length=150)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
