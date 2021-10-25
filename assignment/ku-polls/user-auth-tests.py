"""Tests of authentication."""
import django.test
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTest(django.test.TestCase):

    def setUp(self):
        # superclass setUp creates a Client object and initializes database
        super().setUp()
        self.username = "testuser"
        self.password = "FatChance!"
        self.user1 = User.objects.create_user(
                         username=self.username,
                         password=self.password,
                         email="testuser@nowhere.com")
        self.user1.first_name = "Tester"
        self.user1.save()
        # need a poll question to test voting
        q = Question.create("First Poll Question")
        q.save()
        # a few choices
        for n in range(1,4):
            choice = Choice(choice_test=f"Choice {n}", question=q)
            choice.save()
        self.question = q


    def test_login_view(self):
        """Test that a user can login via the login view."""
        login_url = reverse("login")
        # Can get the login page
        response = self.client.get(login_url)
        self.assertEqual(200, response.status_code)
        # Can login using POST
        # usage: client.post(url, {'key1":"value", "key2":"value"})
        form_data = {"username": "testuser", 
                     "password": "FatChance!"
                    }
        response = self.client.post(login_url, form_data)
        self.assertEqual(302, response.status_code)
        # should redirect us to the polls index page ("polls:index")
        self.assertRedirects(response, reverse("polls:index"))

    def test_auth_required_to_vote(self):
        """Test that authentication is required to submit a vote.

        As an unauthenticated user,
        When I submit a vote for a question,
        Then I am redirected to the login page
          Or I receive a 403 response (FORBIDDEN)
        """
        vote_url = reverse('polls:vote', args=[self.question.id])

        # what choice to vote for?
        choice = self.question.choice_set().first()
        # the polls detail page has a form, each choice is identified by its id
        form_data = {"choice": f"{choice.id}"}
        response = self.client.post(vote_url, form_data)
        # should be redirected to the login page
        self.assertEqual(response.status_code, 302)  # could be 303
        self.assertRedirects(response, reverse('login') )

