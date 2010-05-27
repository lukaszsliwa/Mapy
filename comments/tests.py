# encoding: utf-8
from django.test import TestCase
from forms import CommentForm

class CommentsTest(TestCase):
    def test_empty_comment(self):
        """
        Próba zapisania pustego formularza
        """
        comment = CommentForm()
        self.assertFalse(comment.is_valid())

    def test_valid_comment(self):
        """
        Powinien zapisać poprawnie komentarz
        """
        comment = CommentForm({ 'content': 'Test'})
        self.assertTrue(comment.is_valid())
        

