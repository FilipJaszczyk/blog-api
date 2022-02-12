import faker
from blog.models import BlogEntry, BlogEntryStates
from accounts.models import Account
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
from rest_framework.reverse import reverse


class BlogEntryTransitionsViewsSuite(APITestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.author = Account.objects.create(email=self.faker.email())
        self.valid_content = {
            "title" : self.faker.sentence(),
            "content" : self.faker.sentence(),
        }

    def test_create_blog_entry(self):
        self.client.force_authenticate(self.author)
        res = self.client.post(reverse("blog-entry-create"), self.valid_content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_publish_blog_entry_by_author(self):
        self.client.force_authenticate(self.author)
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        res = self.client.post(reverse("blog-entry-publish", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_publish_blog_entry_transition_not_allowed(self):
        self.client.force_authenticate(self.author)
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        obj.publish()
        obj.save()
        res = self.client.post(reverse("blog-entry-publish", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_412_PRECONDITION_FAILED)

    def test_publish_blog_entry_by_another_user(self):
        user = Account.objects.create(email=self.faker.email())
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        self.client.force_authenticate(user)
        res = self.client.post(reverse("blog-entry-publish", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_archive_blog_entry_by_author(self):
        self.client.force_authenticate(self.author)
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        res = self.client.post(reverse("blog-entry-archive", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_archive_blog_entry_transition_not_allowed(self):
        self.client.force_authenticate(self.author)
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        obj.archive()
        obj.save()
        res = self.client.post(reverse("blog-entry-archive", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_412_PRECONDITION_FAILED)

    def test_archive_blog_entry_by_another_user(self):
        user = Account.objects.create(email=self.faker.email())
        obj = BlogEntry.objects.create(title=self.faker.sentence(), created_by=self.author)
        self.client.force_authenticate(user)
        res = self.client.post(reverse("blog-entry-archive", kwargs={"pk":obj.pk}))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
