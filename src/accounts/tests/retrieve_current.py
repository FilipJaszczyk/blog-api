from rest_framework.test import APITestCase
from rest_framework import status
from django.test import tag
from rest_framework.reverse import reverse
from accounts.models.account import Account
from faker import Faker


ENDPOINT = "current-account-details"



@tag(ENDPOINT)
class RetrieveCurrentAccountSuite(APITestCase):
    def test_unauthenticated(self):
        res = self.client.get(reverse(ENDPOINT))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated(self):
        faker = Faker()
        data = {
            "email": faker.email(),
            "given_name": faker.first_name(),
            "family_name": faker.last_name(),
            "password": faker.password,
        }
        account = Account.objects.create(**data)
        self.client.force_authenticate(account)
        res = self.client.get(reverse(ENDPOINT))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
