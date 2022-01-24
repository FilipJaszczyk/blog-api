from django.db import models
from accounts.models import Account


class BlogEntry(models.Model):
    title = models.CharField(max_length=512, blank=False)
    content = models.TextField(blank=False)
    created_by = models.ForeignKey(to=Account, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
        ]
