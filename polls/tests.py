import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Create your tests here.

class QuestionModelTests(TestCase):

    def test_is_published_recently_with_future_question(self):
        """
        is_published_recently() returns False for questions with pub_date in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.is_published_recently())

    def test_is_published_recently_with_old_question(self):
        """
        is_published_recently() returns False for questions with pub_date older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.is_published_recently())

    def test_is_published_recently_with_recent_question(self):
        """
        is_published_recently() returns True for questions with pub_date within last day
        """
        time = timezone.now() - datetime.timedelta(seconds=10)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.is_published_recently())


def create_question(question_text, days):
    """
    Create a Question with the given text and published given number of days offset to now
    (negative amount means date published in the past, positive means will be published in the future/not yet published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        No questions => message displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question('A question?', -30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A question?')
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        """
        Questions with a pub_date in the future are not displayed on the
        index page.
        """
        create_question('A question?', 1)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        Future question should not be retrievable => 404
        """
        future_question = create_question('A question?', 30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Past question should be retried => 200 & displays the question's text.
        """
        past_question = create_question('A question?', -1)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
