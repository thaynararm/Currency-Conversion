from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class GetTestCase(APITestCase):
    '''Testes para testar a requisição GET'''

    def setUp(self):
        '''Configuração Inicial para o ambiente de testes.'''
        
        with open('conversion/fictitious_conversions.json') as file:
            self.fixtures = json.load(file)
        self.base_url = reverse('convert_currency')
        

    def _build_url(self, from_currency, to_currency, amount):
        '''Constrói a URL com os parâmetros fornecidos'''
        url_with_params = f"{self.base_url}?from={from_currency}&to={to_currency}&amount={amount}"
        return url_with_params
        

    def test_get_correct_url(self):
        '''Verifica se a requisição GET aceita dados corretos na URL.'''

        from_currency = self.fixtures[0]['from_currency']
        to_currency = self.fixtures[0]['to_currency']
        amount = self.fixtures[0]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_incorrect_from_currency(self):
        '''Verifica se a requisição GET rejeita dados incorretos no parâmetro 'from_currency'.'''

        from_currency = self.fixtures[1]['from_currency']
        to_currency = self.fixtures[1]['to_currency']
        amount = self.fixtures[1]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem e final devem ser válidas.', response.data)


    def test_get_incorrect_to_currency(self):
        '''Verifica se a requisição GET rejeita dados incorretos no parâmetro 'to_currency'.'''

        from_currency = self.fixtures[2]['from_currency']
        to_currency = self.fixtures[2]['to_currency']
        amount = self.fixtures[2]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem e final devem ser válidas.', response.data)

    
    def test_get_incorrect_amount(self):
        '''Verifica se a requisição GET rejeita dados incorretos no parâmetro 'amount'.'''

        from_currency = self.fixtures[3]['from_currency']
        to_currency = self.fixtures[3]['to_currency']
        amount = self.fixtures[3]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('O valor a ser convertido deve ser um número válido.', response.data)

    
    def test_get_equal_currency(self):
        '''Verifica se a requisição GET rejeita valores iguais nos parâmetros 'from_currency' e 'to_currency'.'''

        from_currency = self.fixtures[4]['from_currency']
        to_currency = self.fixtures[4]['to_currency']
        amount = self.fixtures[4]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem deve ser diferente da moeda final.', response.data)


    def test_get_comma_in_amount(self):
        '''Verifica se a requisição GET aceita valores com vírgula como separador decimal no 'amount'.'''

        from_currency = self.fixtures[5]['from_currency']
        to_currency = self.fixtures[5]['to_currency']
        amount = self.fixtures[5]['amount']
        
        url_with_params = self._build_url(from_currency, to_currency, amount)

        response = self.client.get(url_with_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class PostTestCase(APITestCase):
    '''Testes para a requisição POST na API de conversão de moeda.'''

    def setUp(self):
        '''Configuração Inicial para o ambiente de testes.'''
        
        with open('conversion/fictitious_conversions.json') as file:
            self.fixtures = json.load(file)
        self.base_url = reverse('convert_currency')


    def test_post_correct_url(self):
        '''Verifica se a requisição POST aceita dados corretos.'''

        data = {
            'from_currency': self.fixtures[0]['from_currency'],
            'to_currency': self.fixtures[0]['to_currency'],
            'amount': self.fixtures[0]['amount']
            }

        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_incorrect_from_currency(self):
        '''Verifica se a requisição POST rejeita dados incorretos no parâmetro 'from_currency'.'''

        data = {
            'from_currency': self.fixtures[1]['from_currency'],
            'to_currency': self.fixtures[1]['to_currency'],
            'amount': self.fixtures[1]['amount']
            }

        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem e final devem ser válidas.', response.data)


    def test_post_incorrect_to_currency(self):
        '''TVerifica se a requisição POST rejeita dados incorretos no parâmetro 'to_currency'.'''

        data = {
            'from_currency': self.fixtures[2]['from_currency'],
            'to_currency': self.fixtures[2]['to_currency'],
            'amount': self.fixtures[2]['amount']
            }

        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem e final devem ser válidas.', response.data)

    
    def test_post_incorrect_amount(self):
        '''Verifica se a requisição POST rejeita dados incorretos no parâmetro 'amount'.'''

        data = {
            'from_currency': self.fixtures[3]['from_currency'],
            'to_currency': self.fixtures[3]['to_currency'],
            'amount': self.fixtures[3]['amount']
            }

        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A requisição deve receber moeda de origem, moeda final e valor a ser convertido válidos.', response.data)

    
    def test_post_equal_currency(self):
        '''Verifica se a requisição POST rejeita valores iguais nos parâmetros 'from_currency' e 'to_currency'.'''

        data = {
            'from_currency': self.fixtures[4]['from_currency'],
            'to_currency': self.fixtures[4]['to_currency'],
            'amount': self.fixtures[4]['amount']
            }

        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('A moeda de origem deve ser diferente da moeda final.', response.data)

