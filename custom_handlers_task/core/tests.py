from django.test import TestCase


class ViewTestClass(TestCase):
    def test_error_page(self):
        response = self.client.get('/nonexist-page/')
        # Проверьте, что статус ответа сервера - 404
        # Проверьте, что используется шаблон core/404.html
