from django.test import TestCase
from forms import ProfileForm, LoginForm, EditProfileForm

class ProfileTest(TestCase):
    def test_create_profile(self):
        form = ProfileForm({
            'username': 'test',
            'password': 'test',
            'email': 'test@test.pl' })
        self.assertTrue(form.is_valid(), 'Formularz jest niepoprawny.')

        form = ProfileForm()
        self.assertFalse(form.is_valid(), 'Formularz nie jest niepoprawny.')

    def test_login_form(self):
        form = LoginForm({ 'username': 'test', 'password': 'pass' })
        self.assertTrue(form.is_valid(), 'Niepoprawny formularz.')
        self.assertFalse(LoginForm().is_valid(), 'Niepoprawny formularz.')

    def test_edit_profile_form(self):
        epf = EditProfileForm({
            'first_name': 'Jan',
            'last_name': 'Kowalski',
            'email': 'jan@kowalski.pl',
            })
        self.assertTrue(epf.is_valid(), 'Niepoprawny formularz.')
        self.assertFalse(EditProfileForm().is_valid(), 'Niepoprawny formularz.')



