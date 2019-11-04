"""
Some tests of authentication in the polls app,
based on the user stories.
"""
import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question, Choice
from django.contrib.auth.models import User


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (days < 0 for questions published
    in the past, days > 0 for questions published in the future).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    return question


class AuthTest(TestCase):
    """Some tests of authentication using django.contrib.auth."""

    def setUp(self):
        self.q1 = create_question("A First Question", days=-1)
        # question should have some choices, to test voting
        self.c1 = Choice.objects.create(choice_text="First Choice", question=self.q1)
        self.c2 = Choice.objects.create(choice_text="Second Choice", question=self.q1)
        self.c3 = Choice.objects.create(choice_text="Third Choice", question=self.q1)
        # a user who can vote
        self.username = "testuser"
        self.userpass = "123$*HCfjdksla"
        self.user = User.objects.create_user(self.username,password=self.userpass)

    def test_can_view_poll_detail(self):
        """Test that an unauthenticated user can view poll detail"""
        url = reverse('polls:detail', args=[self.q1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/detail.html')

    def test_user_can_login(self):
        """Test that a user can login at the url named 'login'.
           This is the standard name used in django.contrib.auth.urls.
           See: response = self.client.get(reverse('polls:index'))
        """
        login_url = reverse('login')
        response = self.client.post(login_url,
                    {'username':self.user.username, 'password':self.userpass})
        # This is a weak test: if login succeeds he is redirected.
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('polls:index'))
        # Can we use the client session to check valid login?
        # self.client.session

    def test_vote_requires_auth_user(self):
        """Test that user must be authenticated to vote.
           When unauthorized user submits a vote
           he should be redirected to the 'login' url.
           When authorized user submits a vote, he is
           redirected to results page.
        """
        try:
            self.client.logout(self)
        except Exception:
            pass
        vote_url = reverse('polls:vote', args=[self.q1.id])
        choice_id = self.q1.choice_set.first().id
        response = self.client.post( vote_url, {'choice':choice_id})
        self.assertEqual(response.status_code, 302)
        # comparing redirect response to reverse('login') fails
        # because of next=... query param.  Append it.
        expect_url = reverse('login') + '?next=' + vote_url
        self.assertRedirects(response, expect_url)

        # Now check that he can vote after login
        response = self.client.post( reverse('login'),
                    {'username':self.user.username, 'password':self.userpass})
        # submit a vote
        response = self.client.post( vote_url, {'choice':str(choice_id)})
        self.assertEqual(response.status_code, 302)
        # This time the redirect should be to poll results
        expect_url = reverse('polls:results', args=[self.q1.id])
        self.assertRedirects(response, expect_url)
        # retrograde manual confirmation of voting
        print("After vote")
        for choice in self.q1.choice_set.all():
            print(choice, "votes:", choice.votes)
        # vote again
        response = self.client.post( vote_url, {'choice':'2'})
        self.assertEqual(response.status_code, 302)
        print("After second vote")
        for choice in self.q1.choice_set.all():
            print(choice, "votes:", choice.votes)
