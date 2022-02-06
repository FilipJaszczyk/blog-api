from datetime import datetime
from email.policy import default
from attr import field
from django.db import models
from accounts.models import Account
from enum import Enum
from django_fsm import FSMIntegerField, transition


class BlogEntryStates(Enum):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2
    


class BlogEntry(models.Model):
    title = models.CharField(max_length=512, blank=False)
    content = models.TextField(blank=False)
    state = FSMIntegerField(default=BlogEntryStates.DRAFT.value)
    created_by = models.ForeignKey(to=Account, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)
    archived_at = models.DateTimeField(null=True)

    @transition(field=state, 
    source=BlogEntryStates.DRAFT.value, target=BlogEntryStates.PUBLISHED.value)
    def publish(self):
        self.published_at = datetime.now()

    @transition(field=state, 
    source=BlogEntryStates.DRAFT.value, target=BlogEntryStates.PUBLISHED.value)
    def archive(self):
        self.archived_at = datetime.now()

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
        ]
