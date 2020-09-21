from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Card

class CardTest(TestCase):

    def test_create_card(self):
        User = get_user_model()
        user = User.objects.create_user(
            cpf='811.180.736-81',
            first_name='Lucas',
            last_name='André Ribeiro',
            email='llucasandreribeiro@etirama.com.br',
            salary=1.5,
            birth_date='1970-07-09 00:00',
            password='lucaribeiro123'
        )
        card = Card.objects.create(
            status=True,
            score=500,
            limit=1000,
            user=user
        )
        self.assertTrue(card.status)
        self.assertEqual(card.score, 500)
        self.assertEqual(card.limit, 1000)
        self.assertEqual(card.user, user)