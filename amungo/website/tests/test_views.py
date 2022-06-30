from django.test import TestCase, Client
from django.urls import reverse


class ViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.home_page_url = reverse('home_page')

    def test_index_page_accessible(self):
        template_name = 'website/index.html'
        response = self.client.get(self.home_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


