import time
import instaloader
import os
import shutil
from datetime import datetime
import requests

# Define o diretório de trabalho como o local onde o script está sendo executado
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cores para mensagens no terminal
RED = "\033[31m"  # Cor vermelha para erros
RESET = "\033[0m"  # Resetando a cor do terminal

# Inicializa uma instância da classe Instaloader. Este objeto será utilizado para baixar o conteúdo do Instagram, de um post específico fornecido pelo usuário.
L = instaloader.Instaloader()

# Solicita ao usuário que insira a URL de um post do Instagram para realizar o download do conteúdo.
post_url = input("Digite o link do post do Instagram: ")

# Verifica se a URL fornecida já contém o prefixo 'https://'. Caso contrário, o prefixo é adicionado.
if not post_url.startswith("https://"):
    post_url = "https://" + post_url

# O shortcode é a parte única do link do post que permite identificar o conteúdo na plataforma Instagram.
# Aqui, extraímos essa parte da URL para utilizá-la posteriormente ao buscar o post.
shortcode = post_url.split("/")[-2]

# Cria um diretório de download baseado na data e hora atual. Isso ajuda a organizar os downloads
# e evita a sobreposição de pastas com o mesmo nome.
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Obtém a data e hora atual
download_folder = os.path.join(os.getcwd(), current_time)  # Define o caminho da pasta de download

# Verifica se a pasta já existe. Se não existir, ela será criada para armazenar os arquivos baixados.
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Introduz uma pausa de 2 segundos entre as requisições para evitar bloqueios por parte do Instagram, devido ao envio excessivo de solicitações em um curto período de tempo.
time.sleep(2)

try:
    # Obtém o objeto do post utilizando o shortcode extraído da URL. Esse objeto contém as informações
    # sobre o post, como se ele é um vídeo, uma imagem única ou um carrossel (várias imagens).
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # Verifica se o post é um carrossel (contém múltiplas imagens). O 'typename' do post será 'GraphSidecar'
    # se for um carrossel.
    if post.typename == 'GraphSidecar':  # Verifica se o post é um carrossel com múltiplas imagens
        # Itera sobre todas as imagens do carrossel, realizando o download de cada uma delas
        for idx, sidecar_node in enumerate(post.get_sidecar_nodes()):
            # Para cada imagem do carrossel, cria-se um nome único para o arquivo.
            filename = os.path.join(download_folder, f"{shortcode}_image_{idx + 1}.jpg")
            with open(filename, 'wb') as f:
                # Realiza o download da imagem e a salva no arquivo correspondente
                f.write(requests.get(sidecar_node.display_url).content)
            print(f"Imagem {idx + 1} do carrossel baixada com sucesso!")
    else:
        # Caso o post não seja um carrossel, verifica se é um vídeo ou uma imagem única.
        if post.is_video:  # Se o post for um vídeo
            # Cria o nome do arquivo de vídeo com base no shortcode
            filename = os.path.join(download_folder, f"{shortcode}.mp4")
            with open(filename, 'wb') as f:
                # Realiza o download do vídeo e o salva no arquivo correspondente
                f.write(requests.get(post.video_url).content)
            print(f"Vídeo baixado com sucesso!")
        else:  # Se o post for uma imagem
            # Cria o nome do arquivo de imagem com base no shortcode
            filename = os.path.join(download_folder, f"{shortcode}.jpg")
            with open(filename, 'wb') as f:
                # Realiza o download da imagem e a salva no arquivo correspondente
                f.write(requests.get(post.url).content)
            print("Imagem baixada com sucesso!")

    # Após o download, exibe uma mensagem indicando que o processo foi concluído com sucesso.
    print("Download concluído com sucesso!")
    # Exibe o local onde o conteúdo foi salvo para o usuário.
    print(f"O conteúdo foi salvo em: {download_folder}")

# Caso ocorra um erro relacionado ao Instaloader (exemplo: post não encontrado, erro na requisição)
except instaloader.exceptions.InstaloaderException as e:
    # Exibe uma mensagem de erro em vermelho
    print(f"{RED}Erro no Instaloader: {e}{RESET}")
    # Caso ocorra erro, a pasta criada durante o processo de download é removida
    if os.path.exists(download_folder):
        shutil.rmtree(download_folder)

# Caso ocorra qualquer outro tipo de erro durante o processo de download (exemplo: erro de rede)
except Exception as e:
    # Exibe uma mensagem genérica de erro em vermelho
    print(f"{RED}Erro geral ao tentar baixar o post: {e}{RESET}")
    # Caso ocorra erro, a pasta criada durante o processo de download é removida
    if os.path.exists(download_folder):
        shutil.rmtree(download_folder)
