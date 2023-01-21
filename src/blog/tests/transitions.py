import faker
from blog.models import BlogEntry, BlogEntryStates
from accounts.models import Account
from django.test import TestCase
from faker import Faker


class BlogEntryTransitionsSuite(TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.user = Account.objects.create(email=self.faker.email())

    def test_default_state(self):
        blog_entry = BlogEntry.objects.create(
            title=self.faker.sentence(), created_by=self.user
        )
        self.assertEqual(BlogEntryStates(blog_entry.state), BlogEntryStates.DRAFT)

    def test_publish(self):
        blog_entry = BlogEntry.objects.create(
            title=self.faker.sentence(), created_by=self.user
        )
        blog_entry.publish()
        self.assertIsNotNone(blog_entry.published_at)

    def test_archive_published_blog_entry(self):
        blog_entry = BlogEntry.objects.create(
            title=self.faker.sentence(), created_by=self.user
        )
        blog_entry.publish()
        blog_entry.archive()
        self.assertIsNotNone(blog_entry.archived_at)

    def test_archive_draft_blog_entry(self):
        blog_entry = BlogEntry.objects.create(
            title=self.faker.sentence(), created_by=self.user
        )
        blog_entry.archive()
        self.assertIsNotNone(blog_entry.archived_at)
