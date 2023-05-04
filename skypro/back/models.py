from django.db import models
from django.contrib.auth.models import User
from back.constants import FileStatusChoices


class UserFile(models.Model):
    file = models.FileField(upload_to='static/files/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=FileStatusChoices, default=FileStatusChoices.uploaded)

    class Meta:
        verbose_name = 'UserFile'
        verbose_name_plural = 'UserFiles'

    def __str__(self):
        return f'{self.author} {self.status}'


class FileLogs(models.Model):
    file = models.ForeignKey(UserFile, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'FileLog'
        verbose_name_plural = 'FileLogs'

    def __str__(self):
        return self.description

