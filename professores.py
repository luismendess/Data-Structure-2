class Professor:

    def __init__(self, ID=3, nome=30, sexo=1, idade=2, especialidade=30, telefone=14):
        self.ID = ID
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.especialidade = especialidade
        self.telefone = telefone

    def setID(self, ID):
        self.ID = ID

    def setNome(self, nome):
        self.nome = nome

    def setSexo(self, sexo):
        self.sexo = sexo

    def setIdade(self, idade):
        self.idade = idade

    def setEspecialidade(self, especialidade):
        self.especialidade = especialidade

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getID(self):
        return (self.ID)

    def getNome(self):
        return (self.nome)

    def getSexo(self):
        return (self.sexo)

    def getIdade(self):
        return (self.idade)

    def getEspecialidade(self):
        return (self.especialidade)

    def getTelefone(self):
        return (self.telefone)
