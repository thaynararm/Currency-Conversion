# Currency Conversion API

A Currency Conversion API é uma ferramenta poderosa em Python, construída com Django e Django Rest Framework, que simplifica a conversão monetária entre mais de 150 moedas diferentes.



## Requisitos

Certifique-se de que o seu sistema atenda aos seguintes requisitos antes de tentar configurar e executar a Currency Conversion API:

**Docker e Docker Compose:**
- Verifique se você possui o Docker instalado em sua máquina. Consulte a [documentação oficial do Docker](https://docs.docker.com/) para obter instruções de instalação.
- Se estiver utilizando Docker Compose, certifique-se de ter a versão mais recente do Docker Compose instalada. [Você pode encontrá-la aqui.](https://docs.docker.com/compose/)



## Instalação
#### Siga os passos abaixo para configurar o ambiente:

**1.** Clone o repositório do GitHub para utiliza-lo:

``` 
git clone https://github.com/thaynararm/Currency-Conversion.git
```
**2.** Navegue até o diretório clonado:
```
cd Currency-Conversion/currency_conversion
```
**3.** Utilize o Docker para construir a imagem:
```
docker build -t conversion .
```
**4.** Execute o contêiner Docker e exponha a porta 8000:**
```
docker run -p 8000:8000 conversion
```

Caso possua Docker Compose instalado, uma alternativa para configurar o ambiente é utilizar o seguinte comando:
```
docker-compose up
```  


## Execução de Testes

Para garantir o correto funcionamento da Currency Conversion API, é recomendado executar os testes automatizados após a construção da imagem Docker. Utilize um dos seguintes comandos, dependendo do seu ambiente:

- **Usando apenas Docker:**
  ```
  docker run -it --rm conversion python manage.py test
  ```
 
- **Usando Docker Compose:**
  ```
  docker-compose run web python manage.py test
  ```



## Uso básico

A API suporta requisições GET e POST para facilitar a integração nos seus projetos. 
 
### Exemplo GET

**Parâmetros**
> **from:** Código ISO 4217 da moeda de origem.
>
> **to:** Código ISO 4217 da moeda de destino.
>
> **amount:** Valor a ser convertido.

```
curl "http://localhost:8000/?&from=USD&to=EUR&amount=100"
```

### Exemplo POST
**Parâmetros**
> **from_currency:** Código ISO 4217 da moeda de origem.
>
> **to_currency:** Código ISO 4217 da moeda de destino.
>
> **amount:** Valor a ser convertido.
```
curl -X POST -H "Content-Type: application/json" -d '{"from_currency": "USD", "to_currency": "EUR", "amount": 100}' http://localhost:8000
```

### Resposta
**Parâmetros**
> **From Currency:** Código ISO 4217 da moeda de origem.
>
> **To Currency:** Código ISO 4217 da moeda de destino.
>
> **Amount:** Valor a ser convertida.
>
> **Converted Amount:** Valor convertido

~~~python
Exemplo de resposta:

{
"From Currency":"USD",
"To Currency":"EUR",
"Amount":100.0,
"Converted amount":92.138,
}
~~~


## Recursos Principais
- Conversão entre mais de 150 moedas. 
- Suporte a requisições GET e POST.
- Construído com Django e Django Rest Framework para desempenho e facilidade de uso.

> - Confira no site as moedas aceitas: https://moeda.info/pages/currency-list
