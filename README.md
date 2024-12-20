# Instagram Post Downloader

Este projeto permite que você baixe conteúdo de posts do Instagram, incluindo imagens, vídeos e carrosséis (posts com múltiplas imagens). O script utiliza a biblioteca `Instaloader` para realizar o download e organiza os arquivos em uma pasta baseada na data e hora do download.

## Funcionalidade

- Baixa imagens, vídeos ou carrosséis de posts do Instagram.
- Cria um diretório único para cada download, baseado na data e hora atual, para evitar sobreposição de arquivos.
- Verifica automaticamente se o link fornecido é válido e adiciona o prefixo `https://` se necessário.
- Em caso de erro, remove a pasta criada durante o processo de download.

## Requisitos

Este projeto requer as seguintes dependências para funcionar corretamente:

-  `instaloader`: Para baixar o conteúdo do Instagram.
-  `requests`: Para realizar as requisições HTTP para download de imagens e vídeos.
- Você pode instalar todas as dependências utilizando o arquivo `requirements.txt`.

## Como Usar

1. Clone ou baixe o repositório para o seu computador.
2. Abra o terminal no diretório onde o projeto foi salvo.
3. Instale as dependências utilizando o arquivo `requirements.txt`.

````
pip install -r requirements.txt
````

4. Execute o script e forneça o link do post do Instagram para realizar o download.

## Possíveis Erros

- Se o post não for encontrado ou ocorrer algum erro na requisição, o script exibirá uma mensagem de erro e removerá a pasta criada durante o processo.

- Certifique-se de que o link fornecido seja válido e esteja acessível.

## Tecnologias Utilizadas

### 1. **Python**

Descrição: Linguagem de programação de alto nível, amplamente utilizada para scripts e automação, bem como para desenvolvimento de aplicações web e análise de dados.

### 2. **Instaloader**

Descrição: Biblioteca Python que permite baixar imagens, vídeos e outros conteúdos de posts, perfis, hashtags e histórias do Instagram. No seu projeto, ela é usada para baixar posts específicos do Instagram a partir da URL fornecida pelo usuário.

Link: [Instaloader no GitHub](https://github.com/instaloader/instaloader)

### 3. **Requests**

Descrição: Biblioteca Python para fazer requisições HTTP de maneira simples e elegante. É usada para baixar o conteúdo (imagens ou vídeos) do Instagram a partir das URLs dos posts.

Link: [Requests no GitHub](https://github.com/psf/requests)

### 4. **os**

Descrição: Módulo integrado do Python que fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios.

Link: [os no Python Docs](https://docs.python.org/3/library/os.html)

### 5. **shutil**

Descrição: Módulo integrado do Python que fornece funções para manipulação de arquivos e operações de cópia, movimentação e remoção de arquivos.

Link: [shutil no Python Docs](https://docs.python.org/3/library/shutil.html)

### 6. **datetime**

Descrição: Módulo integrado do Python que oferece classes para manipulação de datas e horas.

Link: [datetime no Python Docs](https://docs.python.org/3/library/datetime.html)
