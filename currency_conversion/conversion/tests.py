from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class GetTestCase(APITestCase):

    def setUp(self):
        self.fixtures = [
        {
            "from_currency": "BRL",
            "to_currency": "EUR",
            "amount": 100
        },
    ]


    def test_get_correct(self):
        '''Teste para verificar se a página inicial dá o erro 404 quando nenhum dado é passado na URL'''

        self.url_index = reverse('convert_currency')
        response = self.client.get(self.url_index)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_correct(self):
        '''Teste para verificar se o get está aceitando dados corretos na URL '''

        from_currency = self.fixtures[0]['from_currency']
        to_currency = self.fixtures[0]['to_currency']
        amount = self.fixtures[0]['amount']

        url_index = reverse('convert_currency')
        
        url_with_params = f"{url_index}?from={from_currency}&to={to_currency}&amount={amount}"

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
