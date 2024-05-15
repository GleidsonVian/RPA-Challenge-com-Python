# Automação de Preenchimento de Formulário Web com Python e Selenium

Este é um projeto de automação desenvolvido em Python utilizando a biblioteca Selenium para preencher um formulário web com dados de um arquivo Excel. O código foi criado para automatizar a inserção de informações em um formulário da web hospedado em [RPA Challenge](https://www.rpachallenge.com/), um site projetado para testar habilidades de automação.

## Pré-requisitos

- Python 3.x instalado no seu sistema.
- Bibliotecas Python necessárias, listadas no arquivo `requirements.txt`.
- Um navegador web instalado, como Google Chrome ou Mozilla Firefox.
- WebDriver correspondente ao seu navegador instalado e configurado. No caso deste projeto, foi utilizado o ChromeDriver.

## Instalação

1. Clone este repositório para o seu sistema local:

    ```
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```
    cd nome-do-diretorio
    ```

3. Instale as dependências Python necessárias usando o pip:

    ```
    pip install -r requirements.txt
    ```

## Como Usar

1. Execute o script Python `automacao_formulario.py`.
2. O script abrirá uma janela do navegador e acessará o site RPA Challenge.
3. Ele preencherá automaticamente o formulário com os dados do arquivo Excel localizado em `C:\pasta4\Python\rpa challenge\challenge.xlsx`.(mudar de acordo com seu computador)
4. Após preencher o formulário, o script tirará uma captura de tela da tela atual e a salvará como `foto.png` no diretório `C:\pasta4\Python\rpa challenge\`.

## Contribuindo

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para enviar pull requests ou abrir issues para discutir novos recursos, problemas ou melhorias.

