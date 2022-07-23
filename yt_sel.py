from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pathlib import Path

# Path -> é um gerenciador de arquivos para conseguimos pegar os diretorios usados

root_folder = Path(__file__).parent

# root_foler -> retorna o caminho desde nossa raiz até o arquivo atual

path_CHROME = f"{root_folder}/chromedriver.exe"


# path_CHROME -> é o caminho até o nosso driver baixado (chromedriver.exe) : precisamos dele para o python acessar a
# navegação


def conectar_google(*options: str) -> webdriver:
    options_chrome = webdriver.ChromeOptions()

    # options_chrome -> contem as configurações do Chrome

    if options is not None:
        for option in options:
            options_chrome.add_argument(option)
        # faz a iteração das opções passadas na função

    service_chrome = Service(executable_path=path_CHROME)

    # service_chrome -> criamos um serviço google e passamos o  caminho necessário para criar a conexão

    browser = webdriver.Chrome(service=service_chrome, options=options_chrome)

    return browser

    # browser -> Aqui realmente tentamos realizar a conexão passando o serviço e as opções declaradas


# -----------------------------------------------


class python_video_search:
    def __init__(self, on_ytBr=False):
        """
        Inicia o objeto python vídeo

        :param on_ytBr -> Recebe uma Boolean para iniciar o browser ou Youtube
        :type on_ytBr -> Boolean

        :param self -> sujeito do inicializador
        """
        self.list_music_after = []
        self.musc_tocadas = []
        self.lixeira = []
        self.musc_play = ""

        if on_ytBr:
            self.youtube = conectar_google()
            self.youtube.get("https://www.youtube.com/")

            sleep(6)
        else:
            print("Inicie uma conexão  com o Youtube Br :]")

    def colocar_video_list(self, *musics):
        """
        colocar_video_list: Função que recebe *args de uma fila de reprodução e os repassa para uma lista de espera

        -> prepara os vídeos

        :param musics -> são os argumentos 'vídeo' para listar a reprodução
        :type musics -> String
        :return -> Adiciona os argumentos em uma fila de reprodução
        """

        sleep(1.5)
        for music in musics:
            for value_musc in music:
                if not value_musc:
                    continue
                self.list_music_after.append(value_musc)

    def reproduzir_lista(self, define_time=4):
        """
        reproduzir_lista -> Faz a reprodução da fila de espera, quando não encontrado a reprodução termina
        :param define_time -> é o tempo de definição que tal vídeo vai durar por média
        :type -> INT
        :return -> Reproduz a fila de espera de acordo com o argumento recebido e tempo definido
        """
        define_time = define_time * 60 + 25
        if not self.list_music_after:
            print("Nenhuma música a ser reproduzida!!")
        else:

            for index, musica in enumerate(self.list_music_after):
                self.youtube.find_element(By.NAME, "search_query").send_keys(musica)
                sleep(2)
                self.youtube.find_element(By.NAME, "search_query").send_keys(Keys.ENTER)
                sleep(2)
                self.youtube.find_element(By.XPATH,
                                          '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
                sleep(define_time)
                self.musc_tocadas.append(musica)
                for char in range(140):
                    self.youtube.find_element(By.NAME, "search_query").send_keys(Keys.LEFT + Keys.DELETE)
                sleep(1.5)
        self.youtube.get("https://www.youtube.com/")
        self.list_music_after.clear()
        sleep(2)

    def delete_video_list(self, video):
        """
        delete_video_list -> Excluir um argumento na fila de reprodução definida, caso não encontre avise-me
        :param video -> Argumento necessário para exclusão do vídeo em espera
        :type -> Str
        :return -> exclusão do argumento na lista de reprodução
        """
        if not self.list_music_after:
            print('Não é possível deletar o vídeo pois não foi inserido!!')
        else:
            if video in self.list_music_after:
                self.lixeira.append(video)
                self.list_music_after.remove(video)
                print(f"vídeo -{video}- apagado!!")
            else:
                print("vídeo não encontrado!!")

    def search_video(self, music):
        """
        serach_video -> prepara o vídeo a ser reproduzido
        :param music -> pesquisa na query do youtube o argumento passado
        :return -> pesquisa inserida e colocada em preparo de reprodução
        """

        self.youtube.find_element(By.NAME, "search_query").send_keys(music)
        sleep(1.8)
        self.musc_play = music
        self.youtube.find_element(By.NAME, "search_query").send_keys(Keys.ENTER)
        sleep(1.8)

    def play_video(self):
        """
        play_video -> Inicializa o vídeo
        :type -> INT
        :return -> Clique da reprodução de acordo com o param time
        """
        for char in range(140):
            self.youtube.find_element(By.NAME, "search_query").send_keys(Keys.LEFT + Keys.DELETE)
        self.youtube.find_element(By.XPATH,
                                  '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
        self.musc_tocadas.append(self.musc_play)

    def search_video_by_link(self, link_music):
        """

        :param link_music -> argumento de pesquisa em formato link
        :type -> Str(links)
        :return -> reprodução direta
        """
        self.youtube.get(link_music)

    def quit_py_musc(self):
        """

        :return -> fecha o navegador ou youtube
        """
        sleep(2)
        self.youtube.quit()

    def tocadas_visu(self):
        with open("file_write_faixas", "a+") as faixa:
            for item in self.musc_tocadas:
                faixa.write(f"  faixa: -[ {item} ]- Data: {datetime.today().strftime('%d/%m/%Y %H:%M')}\n")
        self.musc_tocadas.clear()

        print("=-"*80)
        with open("file_write_faixas", "r+") as ler:
            for line in ler.readlines():
                print(line)
        print("=-"*80)

    def lixeira_historico(self):
        print("=-"*80)
        print(" ALERTA: Após fechar uma sessão o historico é limpado!!")
        if not self.lixeira:
            print(" Clary não encontrou faixas apagadas!!")
        else:
            for id, item in enumerate(self.lixeira):
                print(f"    item {id} faixa: [{item}]")
        print("=-"*80)
