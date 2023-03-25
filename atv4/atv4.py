import sys

class IdxPrimario:

    # Tabelas de Indices
    TabelaIdxPrimario = list()
    TabelaIdxSecundario = list()

    def __init__(self, ArquivoEntrada=None, ArquivoIdx=None, ArquivoSaida=None):
        # Leitura do arquivo principal
        try:
            self.ArquivoEntrada = open(sys.argv[0], 'r+')

        # verificacao se ha o arquivo informado
        except FileNotFoundError:
            print('O arquivo de dados nao foi encontrado')
            print('Por favor informe novamente')
            exit(1)

        # Abertura do arquivo de Indices
        try:
            self.ArquivoIdx = open(sys.argv[1], 'r+')

        # verificacao se ha o arquivo informado
        except FileNotFoundError:
            print('Arquivo de indices nao foi encontrado')
            print("Por favor, informe novamente!")
            exit(1)

        # Imprime a lista de Indices
        self.ArquivoSaida = open(sys.argv[2], 'w+')

        # criando tabela de indices
        lines = self.ArquivoEntrada.readlines()

        # referencia a cada componente do header
        size = self.Cabecalho(lines[0])
        top = self.Cabecalho(lines[0])
        qtd = self.Cabecalho(lines[0])
        status = self.Cabecalho(lines[0])

        # separa os filtros do arquivo
        Filtro = self.ArquivoIdx.readLines()
        Filtro1 = Filtro[0]
        Filtro1 = Filtro1.strip()
        Filtro2 = Filtro[1]
        Filtro2 = Filtro2.strip()

        def Cabecalho(self, cabecalho):
            # Separa SIZE para leitura
            SplitaTamanho = cabecalho.split(" ")
            size = SplitaTamanho[0].split("SIZE = ")
            # Separa TOP para leitura
            SplitaTop = cabecalho.split(" ")
            top = SplitaTop[1].split("TOP = ")
            # Separa QTDE para leitura
            SplitaQuantidadeRegistros = cabecalho.split(" ")
            qtd = SplitaQuantidadeRegistros[2].split("QTDE = ")
            # Separa Status para leitura
            SplitaStatus = cabecalho.split(" ")
            status = SplitaStatus[3].split("STATUS = ")
            # retorna os valores do header
            return (size[1], top[1], qtd[1], status[1])

        # gera as tuplas para cada registro
        for Indice in range(1, len(lines)):
            ChavePrimaria = self.GeraChaveCanonica(Registro=lines[Indice])
            ChaveSecundaria = self.GeraChaveSecundaria(
                Registro=lines[Indice], Filtro1=Filtro2)

            # definindo RRN
            RRN = Indice - 1

            # criando tuplas: primaria e secundaria
            TuplaPrimaria = (RRN, ChavePrimaria)
            TuplaSecundaria = (ChaveSecundaria, ChavePrimaria)

            # inserindo tuplas na tabela de indices
            self.TabelaIdxPrimario.append(TuplaPrimaria)
            self.TabelaIdxSecundario.append(TuplaSecundaria)

        # ordenando tabelas
        self.TabelaIdxPrimario.sort(key=lambda TuplaPrimaria: TuplaPrimaria[1])
        self.TabelaIdxSecundario.sort(key=lambda TuplaSecundaria: TuplaSecundaria[0])

        def PesquisaIdxSecundario(self, Filtro1, aux):
            if(Filtro1.upper() in aux[0]):
                return aux[1]
            return (-1)

        def PesquisaIdxPrimario(self, ChaveCanonica, lines):
            # compara com os valores de indice primario para verificar se h? o registro no arquivo
            for elemento in self.getIdxPrimario():
                if (elemento[1] == ChaveCanonica):
                    return lines[int(elemento[0] + 1)]

        # variavel auxiliar para buscar um valor dentro do arquivo e realizar os testes
        ValorEncontrado = False
        for elemento in self.TabelaIdxSecundario:
            ChaveCanonica = self.PesquisaIdxSecundario(Filtro1=Filtro1, aux=elemento)
            # adiciona ao arquivo de sa?da se algum valor for encontrado
            if(ChaveCanonica != -1):
                ValorEncontrado = True
                Registro = self.PesquisaIdxPrimario(
                    ChaveCanonica=ChaveCanonica, lines=lines)
                self.ArquivoSaida.write(Registro)
            # se nao for encontrado valor, informa no arquivo e encerra
            if(ValorEncontrado != True):
                self.ArquivoSaida.write( 'Nao ha registros com a opcao desejada')
            self.__del__()

        def getIdxPrimario(self):
            return self.TabelaIdxPrimario

        def getIdxSecundario(self):
            return self.TabelaIdxSecundario

        def GeraChaveCanonica(self, Registro):
            auxiliar = Registro.strip()
            tokens = auxiliar.split('|')
            
            # Gerando Chave Canonica com Ano e Titulo
            key = tokens[4] + tokens[2]
            key = key.upper()
            key = key.replace(' ', '')
            return (key)

        def GeraChaveSecundaria(self, registro, opcao):
            auxiliar = registro.strip()
            tokens = auxiliar.split('|')
            
            # faz a verificacao dos valores lidos no arquivo
            if(opcao == 'ano'):
                keySecundaria = tokens[0]
            elif(opcao == 'duracao'):
                keySecundaria = tokens[1]
            elif(opcao == 'titulo'):
                keySecundaria = tokens[2]
            elif(opcao == 'artista'):
                keySecundaria = tokens[3]
            elif(opcao == 'genero'):
                keySecundaria = tokens[4]
            elif(opcao == 'idioma'):
                keySecundaria = tokens[5]
            else:
                self.ArquivoSaida.write('opcao invalida')
                exit(1)
                
            # seta a opcao lida em uppercase para us?-la como chave secundaria
            keySecundaria = keySecundaria.upper()
            return (keySecundaria)

        # fechando os arquivos
        def __del__(self):
            self.ArquivoEntrada.close()
            self.ArquivoIdx.close()
            self.ArquivoSaida.close()


def main():
    if(len(sys.argv) != 4):
        print('numero incorreto de parametros')
        exit(1)
    IdxPrimario(ArquivoEntrada=sys.argv[0], ArquivoIdx=sys.argv[1], ArquivoSaida=sys.argv[2])
    
main()