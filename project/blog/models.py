from django.db import models

class Blog(models.Model):
    writer = models.CharField(default = "yjyang", max_length = 10)
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=10, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s  |   %s' % (self.title, self.created_at)
