class Game:

    # construtor do objeto Game
    def __init__(self, cod=None, nome=None, genero=None, plataforma=None, ano=None, classificacao=None, preco=None, midia=None, tamanho=None, produtora=None):
        self.cod = cod
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora

    def setCod(self, cod):
        self.cod = cod

    def getCod(self):
        return (self.cod)
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return (self.nome)

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return (self.genero)

    def setPlataforma(self, plataforma):
        self.plataforma = plataforma

    def getPlataforma(self):
        return (self.plataforma)

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return (self.ano)

    def setClassificacao(self, classificacao):
        self.classificacao = classificacao

    def getClassificacao(self):
        return (self.classificacao)

    def setPreco(self, preco):
        self.preco = preco

    def getPreto(self):
        return (self.preco)

    def setMidia(self, midia):
        self.midia = midia

    def getMidia(self):
        return (self.midia)

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def getTamanho(self):
        return (self.tamanho)

    def setProdutora(self, produtora):
        self.produtora = produtora

    def getProdutora(self):
        return (self.produtora)
