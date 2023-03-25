def NumeroRegsitros(file):
    with open(r"arquivo.txt", "r") as rfile:
        line = len(rfile.readlines())
        return line


def LerRegistroComRRN(file, meio):


def BuscaBinaria(file, key, record):
    start = 0
    end = NumeroRegistros(file) - 1
    while(start <= end):
        busca = False
        half = (start+end)/2
        record = LerRegistroComRRN(file, meio)
        if(record.key == key):
            busca = True
            return busca
        if(record.key < key):
            end = half + 1
        else:
            start = half + 1
    return busca
