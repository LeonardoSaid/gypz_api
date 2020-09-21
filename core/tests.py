from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            cpf='073.472.723-27',
            first_name='Emilly',
            last_name='Silvana Sales',
            email='emillysilvanasales__emillysilvanasales@hlt.arq.br',
            salary=1,
            birth_date='2012-03-09 00:00',
            password='foo'
        )
        self.assertEqual(user.cpf, '073.472.723-27')
        self.assertEqual(user.first_name, 'Emilly')
        self.assertEqual(user.last_name, 'Silvana Sales')
        self.assertEqual(user.email, 'emillysilvanasales__emillysilvanasales@hlt.arq.br')
        self.assertEqual(user.salary, 1)
        self.assertEqual(user.birth_date, '2012-03-09 00:00')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(cpf='')
        with self.assertRaises(ValueError):
            User.objects.create_user(cpf='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            cpf='073.472.723-27',
            first_name='Emilly',
            last_name='Silvana Sales',
            email='emillysilvanasales__emillysilvanasales@hlt.arq.br',
            salary=1,
            birth_date='2012-03-09 00:00',
            password='foo'
        )
        self.assertEqual(admin_user.cpf, '073.472.723-27')
        self.assertEqual(admin_user.first_name, 'Emilly')
        self.assertEqual(admin_user.last_name, 'Silvana Sales')
        self.assertEqual(admin_user.email, 'emillysilvanasales__emillysilvanasales@hlt.arq.br')
        self.assertEqual(admin_user.salary, 1)
        self.assertEqual(admin_user.birth_date, '2012-03-09 00:00')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
            cpf='073.472.723-27',
            first_name='Emilly',
            last_name='Silvana Sales',
            email='emillysilvanasales__emillysilvanasales@hlt.arq.br',
            salary=1,
            birth_date='2012-03-09 00:00',
            password='foo',
            is_superuser=False
        )
