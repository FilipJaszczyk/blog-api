from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from faker import Faker
from accounts.models.account import Account
from django.test import tag

ENDPOINT = "account-create"

@tag(ENDPOINT)
class CreateAccountSuite(APITestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        password = self.faker.password(length=10)
        self.valid_content = {
            "email": self.faker.email(),
            "given_name": self.faker.first_name(),
            "family_name": self.faker.last_name(),
            "password": password,
            "repeated_password": password,
        }

    def test_success(self):
        res = self.client.post(reverse(ENDPOINT), self.valid_content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        account_query = Account.objects.filter(email=self.valid_content["email"])
        self.assertEqual(account_query.count(), 1)

    def test_passwords_dont_match(self):
        self.valid_content["password"] += "".join(self.faker.random_letters(length=2))
        res = self.client.post(reverse(ENDPOINT), self.valid_content)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
