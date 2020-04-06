from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Design Scorecard')


    def test_services_page_works(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'services.html')
        self.assertContains(response, 'Design Scorecard')

    def test_contact_page_works(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'Contact Us')

    def test_design_challenge_page_works(self):
        response = self.client.get(reverse("design_challenge"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'design_challenge.html')
        self.assertContains(response, 'Design Scorecard')
