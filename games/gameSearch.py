# criando uma classe (GAMES), seus objetos são com base no arquivo games.txt
class Games:
    def _init_(self, titulo=None, produtora=None, genero=None, plataforma=None, ano=None, classificacao=None, preco=None, 
               midia=None, tamanho=None):
        self.titulo = titulo
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        
    # metodo set - serve para atrubir um novo valor ao atributo (games."compos")
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_produtora(self, produtora):
        self.produtora = produtora

    def set_genero(self, genero):
        self.genero = genero

    def set_plataforma(self, plataforma):
        self.plataforma = plataforma

    def set_ano(self, ano):
        self.ano = ano

    def set_classificacao(self, classificacao):
        self.classificacao = classificacao

    def set_preco(self, preco):
        self.preco = preco

    def set_midia(self, midia):
        self.midia = midia

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    # metodo get - serve para retonar o valor do atributo (gemes."compos")
    def get_titulo(self):
        return self.titulo

    def get_produtora(self):
        return self.produtora

    def get_genero(self):
        return self.genero

    def get_plataforma(self):
        return self.plataforma

    def get_ano(self):
        return self.ano

    def get_classificacao(self):
        return self.classificacao

    def get_preco(self):
        return self.preco

    def get_midia(self):
        return self.midia

    def get_tamanho(self):
        return self.tamanho

# Metodo 1: tamanho fixo
def metodo1():
    print()
    
# Metodo 2: Indicador de tamanho
def metodo2():
    print()

# Metodo 3: Delimitadores
def metodo3(line):
    line = line.split('|')
    with open('metodo3.txt', 'w') as saida1:
        saida1.write(line[0] + '*')
        saida1.write(line[1] + '*')
        saida1.write(line[2] + '*')
        saida1.write(line[3] + '*')
        saida1.write(line[4] + '*')
        saida1.write(line[5] + '*')
        saida1.write(line[6] + '*')
        saida1.write(line[7] + '*')
        saida1.write(line[8] + '*')

# Metodo 4: Expressao chave-valor
def metodo4(line):
    with open('metodo4.txt', 'w') as saida1:
        games = Games(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        saida1.write('title = ' + games.titulo + '|')
        saida1.write('producer = ' + games.produtora + '|')
        saida1.write('genre = ' + games.genero + '|')
        saida1.write('platform = ' + games.plataforma + '|')
        saida1.write('year = ' + games.ano + '|')
        saida1.write('classification = ' + games.classificacao + '|')
        saida1.write('price = ' + games.preco + '|')
        saida1.write('media = ' + games.midia + '|')
        saida1.write('size = ' + games.tamanho + '|')


with open('games.txt', 'r') as file:
    for line in file:
        line = line.split('|')
        print(line.strip())
    