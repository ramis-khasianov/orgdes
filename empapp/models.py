from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    manager = models.ForeignKey('self', related_name='subordinates', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
