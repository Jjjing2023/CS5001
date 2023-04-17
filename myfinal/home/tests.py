from django.test import TestCase
from django.urls import reverse
from .models import Sign
# Create your tests here.


class HomeViewsTestCase(TestCase):
    def setUp(self):
        self.sign = Sign.objects.create(
            name='Test Sign',
            description='Test description',
            url='http://test.url'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_result_view(self):
        data = {
            'name': 'Test User',
            'birthdate': '1990-01-01',
            'gender': 'M'
        }
        response = self.client.post(reverse('result'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/result.html')
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Test description')
        self.assertContains(response, 'http://test.url')

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=[self.sign.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/detail.html')
        self.assertContains(response, 'Test Sign')
        self.assertContains(response, 'Test description')
        self.assertContains(response, 'http://test.url')


