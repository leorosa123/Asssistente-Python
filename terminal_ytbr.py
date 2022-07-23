from time import sleep
import sys
from pathlib import Path
from yt_sel import python_video_search


####
class inputs_youtube_on:
    def __init__(self, on_of=True):
        if on_of:
            self.user_on = python_video_search(on_of)
        else:
            print("Ocorreu algum erro de conexão")

    def input_(self):
        while True:
            print()
            command_user = str(input("------------Youtube_on: ")).strip()
            sleep(3)
            if command_user == 'exit':
                print()
                print("Fechando a sessão...")
                self.user_on.quit_py_musc()
                sleep(5)
                print("=-" * 80)
                print("Muito obrigada!! por usar nossos serviços, Clary guardou vc no coração robôtico :}")
                print("=-" * 80)
                break

            if command_user == 'opt':
                document_ytbr_and_options()
                sleep(4)

            if command_user == 'by_link':
                print()
                print("Clary aqui!!Pesquise seus vídeos de um modo diferente e prático utilizando seus links :]")
                print("Dica: Escreva apenas seu link e evite adicionais além da URL")
                sleep(4)
                link = input(str("-> Link vídeo: ")).strip()
                print("Estou colocando seu vídeo..."), sleep(2)
                self.user_on.search_video_by_link(link)

            if command_user == "uk_yt":
                search_yt = input(str("-> Vídeo a ser pesquisado: ")).strip().capitalize()
                sleep(2)
                print("Vou aproveitar para adicionar essa faixa no meu banco de dados [.__.]")
                sleep(2)
                self.user_on.search_video(search_yt)

            if command_user == 'play_yt':
                print("Estou colocando seu vídeo <;-;>...")
                sleep(2)
                self.user_on.play_video()

            if command_user == 'list_yt':
                print("-=" * 50)
                print("*CENTRAL DE VÁRIOS VÍDEOS*")
                print("Clary passando para te dar uma dica!! :]")
                print("Dica: Adicione suas faixas e quando terminar envie um [.]")
                print("-=" * 50)
                sleep(4)
                print()
                faixas = []
                while True:
                    musics = str(input("Adicone seu vídeo para espera: ")).strip().capitalize()
                    sleep(1.5)
                    if musics == '.':
                        break
                    faixas.append(musics)
                    print(f"-{musics}- Adicionado com sucesso!!")
                    print()
                self.user_on.colocar_video_list(faixas)
                print()
                sleep(2)
                print("Consegui adicionar suas faixas, estão preparadas para tocar em qualquer momento :}")

            if command_user == "list_play":
                print()
                print("-" * 100)
                print("OhOuuuu, Clary na área denovo para te dar um aviso!!")
                sleep(2)
                print("Receba essa outra dica para melhor expêriencia!;}"), sleep(1.5)
                print(
                    "DICA: Em reproduções seguidas de outras faixas é importante que defina um tempo de execução de cada uma, nosso padrão é 4 minutos por vídeo"), sleep(
                    2)
                print("-" * 100)
                time_video = int(input("Informe um tempo médio de cada faixa, você controla sua expêriencia!![min]: "))
                sleep(2)
                print("Preparando seus vídeos...:}"), sleep(5)
                print("Agora vou reproduzir suas faixas :]")
                self.user_on.reproduzir_lista(time_video)
                sleep(1)
                print("Terminei de reproduzir suas faixas!!Espero que eu tenha acertado nelas [~_::_~]")

            if command_user == "delete_list":
                print()
                print("-" * 100)
                print(
                    "Clary na área!!, tudo em ordem aqui?Lembre-se caso queira apagar um vídeo informe a faixa adicionada anteriormente")
                print("Cuidado: Ao apagar uma faixa não é possível restaurá-la ")
                print("-" * 100), sleep(4)
                vd = str(input("Faixa a ser deletada: ")).strip().capitalize()
                self.user_on.delete_video_list(vd)

            if command_user == "fx_yt":
                self.user_on.tocadas_visu()
            if command_user == "lx_yt":
                self.user_on.lixeira_historico()


# caso não saiba o caminho para executar pelo CMD use essa função
def qual_caminho_execute_cmd():
    """
    lembre-se: 'cd /dict' para navegar e 'cd..' para voltar um dict

    Revela o caminho completo a ser passado para o cmd
    para executar o programa escreva : python 'name_arquivo.py'
    :return -> retorna o caminho completo do arquivo
    """
    caminho_execute = Path(__file__).parent

    return caminho_execute


def document_ytbr_and_options():
    print()
    print("-=" * 80)
    print("""
    *Opções comando*[opt]
    Agora vou te mostrar os comandos disponivéis durante a navegação (youtube-on)!
    
    DICA: defina o tempo de seus vídeos para antingir maior precisão de reprodução
    
    cuidado: Esses comandos só estão disponivéis quando iniciada um sessão [youtube-on] atráves do comando 'start'
    
    Opções de navegação:
            [A] - Pesquisar vídeo por link: comando - [by_link]
            [B] - Pesquisar vídeo único pela query do Youtube: comando - [uk_yt]
            [C] -  Tocar reprodução de pesquisa única: comando - [uk_play]
            [D] - Colocar vídeo em lista de espera: comando - [list_yt]
            [E] - Tocar faixas em espera: comando - [list_play]
            [F] - Excluir faixa na lista de reprodução: comando - [delete_list]
            
    Opções de Análise de dados:
            [1] - Verificar todas as faixas tocadas: comando - [fx_yt]
            [2] - Visualizar historico de faixas apagadas: comando - [lx_yt]
           
            
    """)
    print("-=" * 80)


def doc_dev():
    from random import choice
    user_real = "clary_dev_program_33-22"
    passwords_real = ["bot-22-23", "bot-33-66", "bot-20-10", "bot-55-66"]
    passwords_real = choice(passwords_real)
    tentativas = 3
    while True:
        print("-=" * 80)
        if tentativas == 0:
            print("Você não tem acesso para a área Devs!!")
            break
        user = str(input("User_dev: ")).strip()
        passworrds = str(input("password_dev:")).strip()
        print()
        print("Analisando..."), sleep(3)

        if user == user_real and passworrds == passwords_real:
            print()
            print()
            print("=" * 160)
            print(f"{'Central DEVs':^150}")
            print()
            print(" Olha quem chegou aqui!!Meu querido Dev!Seja bem vindo(a) a central Dev da clarinha")
            print(" É um prazer ter você aqui para mostrar o quão nossa comunidade é forte e curiosa :]")
            print()
            print(" *Documentação*")
            print("     Arquivos python:")
            print(
                "         yt_sel.py -Arquivo 1-: Esse arquivo foi utilizado para construir as propriedades e funções que controlam a plataforma do Youtube.")
            print(
                "         terminal_ytbr.py -Arquivo 2-: Esse aquivo foi utilizado para criar a conexão entre os comandos do CMD e python.")
            print()
            print("     Classes dentro dos Arquivos:")
            print(
                "          python_video_search[Arquivo:yt_sel.py]: Essa classe comporta as funções que controlam o Youtube e faz a conexão entre programa e plataforma.")
            print(
                "          inputs_youtube_on[Arquivo:terminal_ytbr.py]: Essa classe comporta as funções que desenvolvem um segundo prompt de comando,\n também realiza a comunicação de cliente e programa")
            print()
            print("     Arquivos Adicionais e extensões:")
            print("           [chromedriver.exe] - Arquivo capaz de conectar o programa com o google")
            print(
                "           [file_write_faixas.txt]- Arquivo capaz de Analisar dados do cliente e retornar a faixa e data de reprodução")
            print()
            print("     Funções do programa:")
            print()
            print(
                "Funções de iniciar conexão e encerrar conexão com o chrome:\n conectar_google()[file:yt_sel.py] \n quit_py_music()[fie:yt_sel.py]")
            print()
            print("Funções de pesquisa única: \n search_video()[file:yt_sel.py] \n play_video[file:yt_sel.py]")
            print()
            print(
                "Funções que controlam lista de faixas de reprodução[file: yt_sel.py]:\n colocar_video_list() \n reproduzir_lista() \n delete_video_list() ")
            print()
            print("Funções para analise de dados do user[file:yt_sel.py]:\n tocadas_visu() \n lixeira_historico()")
            print("=" * 160)
            break
        else:
            print("Acesso negado!!")
            tentativas -= 1


comandos = sys.argv
actions = len(comandos)

if __name__ == "__main__":

    if 'terminal_ytbr.py' in comandos and len(comandos) == 1:
        print("=-" * 80)
        print("""
        Bem vindo(a)!! a central de comando Youtube automizada, ficamos muito contente com sua escolha a nossos serviços \n
        Meu nome é Clary!!Prazer querido usuario!! serei sua assistente nessa jornada automatica :] \n
        Vamos para os comandos!! \n 
        
        Dica básica: toda vez que quiser executar um comando escreva 'python 'name_file'.py [comando_cmd]'
        """)

        print(f"""
            Comando promt: \n
            {'1 - [opt]: Traz todos os comandos do programa ao ser iniciado':<50}  \n
            {'2 - [doc]: Traz toda a documentação com as funções de cada opção para Devs':<50} \n
            {'3 - [start] Inicia o programa toda vez que chamado':<50} \n
            {'4 - [exit] Para fechar programas e ações'}
        """)

        print("=-" * 80)
        print()

    if actions > 2:
        print("Desculpe mas não é possível realizar duas ações")
    else:
        if 'start' in comandos:
            try:
                yt_on = inputs_youtube_on(True)
                yt_on.input_()
            except Exception as e:
                print("Ocorreu algum erro!!", e)
        if 'opt' in comandos:
            document_ytbr_and_options()

        if 'doc' in comandos:
            doc_dev()
        if 'exit' in comandos:
            exit()
