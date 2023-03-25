import sys
import os

class Musica:
    #criando objeto musica
    def __init__(self):
        self.ano = []
        self.duracao = []
        self.titulo = []
        self.artista = []
        self.genero = []
        self.idioma = []
        self.Quantidade = 0
    #definindo parametros musica
    def setMusica(self, ano, duracao, titulo, artista, genero, idioma):
        self.ano.append(ano)
        self.duracao.append(duracao)
        self.titulo.append(titulo)
        self.artista.append(artista)
        self.genero.append(genero)
        self.idioma.append(idioma)
        self.Quantidade += 1

    def getMusica(self, Quantidade):
        return (self.ano[Quantidade] + '|' + self.duracao[Quantidade] + '|' + self.titulo[Quantidade] + '|'
                + self.artista[Quantidade] + '|' + self.genero[Quantidade] + '|' + self.idioma[Quantidade])

#abrindo arquivo de leitura dos dados
Playlist = open(sys.argv[0], 'r+')
    #iniciando no comeco dos registros
Playlist.seek(0, 0)
    #separando cada registro do arquivo
MusicaPlaylist = (Playlist.readline()).strip()
#verificando se arquivo esta vazio
if (os.stat(sys.argv[0]).st_size == None):
    print('O arquivo esta Vazio!')
    exit(1)
#abrindo arquivo de filtro a pesquisar
Filtro = open(sys.argv[1], 'r+')
    #iniciando no comeco do arquivo
Filtro.seek(0, 0)
#separando os elementos de filtro
ElementoFiltro = (Filtro.readline()).strip()
#verificando se o arquivo esta vazio
if (os.stat(sys.argv[1]).st_size == None):
    print('O arquivo esta vazio!')
    exit(1)
    #define o elemento para pesquisa
Categoria = ElementoFiltro
#separa cada registro de pesquisa do arquivo entrada
ElementoFiltro = (Filtro.readline()).strip()
#verifica se tem valores a serem utilizados
if (ElementoFiltro == None):
    print('ERRO: Falta de parametros no arquivo!')
    exit(1)
#cria o index de pesquisa
Elemento = ElementoFiltro.upper()

#define o cabecalho a ser lido
Cabecalho = MusicaPlaylist.split()
#vetor auxiliar para tratamento do cabecalho
VetorizaCabecalho = []
#lendo cada item do cabecalho
for ItemCabecalho in Cabecalho:
    #separa o valor dos itens do cabecalho
    Item = ItemCabecalho.split('=')
    #coloca o valor separado no vetor
    VetorizaCabecalho.append(Item[1])

#salvando os registros
Registro = Musica()

for RegistroMusica in range(int(VetorizaCabecalho[2])):
    #separa os registros de cada linha do carquivo
    MusicaPlaylist = (Playlist.readline()).strip()
    #verifica se o arquivo esta vazio
    if (MusicaPlaylist == None):
        print('O arquivo nao tem registros')
        exit(1)
    #separa o registro pelos pipes
    MusicaPlaylist = MusicaPlaylist.split('|')
    #define objeto musica em registro
    Registro.setMusica(ano=MusicaPlaylist[0], duracao=MusicaPlaylist[1],
                       titulo=MusicaPlaylist[2], artista=MusicaPlaylist[3],
                       genero=MusicaPlaylist[4], idioma=MusicaPlaylist[5])
#abrindo arquivo de saida
with open(sys.argv[2], 'w+') as Resultado:
    #forca inicio do arquivo de saida
    Resultado.seek(0, 0)
    #criando string auxiliar
    RegistroEncontrado = ''
    #contador de registros encontrados setado em 0
    NumeroRegistros = 0
    #se o filtro selecionado for igual a ano
    if (Categoria.upper() == 'ANO'):
        #para cada registro com ano igual insere, na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            if Registro.ano[posicao] == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro selecionado for igual a duracao
    elif (Categoria.upper() == 'DURACAO'):
        #para cada registro com duracao igual insere, na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            if Registro.duracao[posicao] == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro selecionado for igual ao titulo
    elif (Categoria.upper() == 'TITULO'):
        #para cada registro com titulo igual, insere na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            RegistroEncontrado = Registro.titulo[posicao]
            if RegistroEncontrado.upper() == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro selecionado for igual a artista
    elif (Categoria.upper() == 'ARTISTA'):
        #para cada registro com artista igual, insere na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            RegistroEncontrado = Registro.artista[posicao]
            if RegistroEncontrado.upper() == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro for igual ao genero
    elif (Categoria.upper() == 'GENERO'):
        #para cada registro com genero igual, insere na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            RegistroEncontrado = Registro.genero[posicao]
            if RegistroEncontrado.upper() == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro for igual ao idioma
    elif (Categoria.upper() == 'IDIOMA'):
        #para cada registro com idioma igual,  insere na string auxiliar
        for posicao in range(int(VetorizaCabecalho[2])):
            RegistroEncontrado = Registro.idioma[posicao]
            if RegistroEncontrado.upper() == Elemento:
                RegistroBusca = Registro.getMusica(posicao)
                Resultado.write(RegistroBusca+'\n')
                NumeroRegistros += 1
    #se o filtro informado estiver fora das opcoes informadas
    else:
        print("Opcao inexistente!")
    #se o contador de registro for igual a zero, nao ha nada no arquivo que foi filtrado
    if (NumeroRegistros == 0):
        Resultado.write("Nao ha registro com esse filtro")
#fechando os arquivos abertos
Playlist.close()
Filtro.close()
Resultado.close()
