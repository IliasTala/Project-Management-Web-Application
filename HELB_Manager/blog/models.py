from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    collaborator = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.TextField()
    assign_task_to = models.TextField()
    status1 = models.CharField(max_length=100)
    status2 = models.CharField(max_length=100)
    status3 = models.CharField(max_length=100)
    status4 = models.CharField(max_length=100)

    def list_assignations(self):
        return self.assign_task_to.split('/')

    def list_collaborator(self):
        return self.collaborator.split('/')

    def list_tasks(self):
        return self.tasks.split('/')

    def list_assigned_tasks(self):
        task_contrib_pairs = []
        tasks = self.tasks.split('/')
        collaborator = self.list_assignations()

        for i in range(len(tasks)):
            task_contrib_pairs.append((tasks[i], collaborator[i]))

        return task_contrib_pairs

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})




