class lutador:
    def __init__ (self,cod,nome,sexo,idade,peso,PO, CP):
        self.cod = cod
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
        self.pais_Origem = PO
        self.categoria_Peso =CP

class main:
    def __init__ (self):
        self.listaL = []
        self.CES()


    def CES(self):
        print('------Sistema UFC 1.3------')
        cf = 1
        while(cf):
            print('1-visualizar lista dos Lutadores cadastrados')
            print('2-adicionar Lutador')
            print('3-excluir Lutador')
            print('4-visualizar lista por categoria de peso')
            print('5-funçao proxima categoria')
            print('6-visualizar historia do UFC')
            print('7-sair')
            option=self.OP()
            if (option == 1):
                self.visualizar()
            elif (option == 2):
                self.addLut()
            elif (option == 3):
                self.remove()
            elif (option == 4):
                self.VisCate()
            elif (option == 5):
                self.proxCat()
            elif (option == 6):
                self.visualizarHis()
            elif (option == 7):
                cf = 0


    def OP(self):
        return int(input('escolha uma opçao: '))

    def visualizar(self):
        print('\n----visualizando----')
        for i in range(0,len(self.listaL)):
            print('cod: {}| nome: {}| peso: {} quilos| categoria de peso: {}| sexo: {}| idade: {}| pais de origem: {}'
                  .format(self.listaL[i].cod, self.listaL[i].nome, self.listaL[i].peso,self.listaL[i].categoria_Peso,self.listaL[i].sexo,self.listaL[i].idade,
                          self.listaL[i].pais_Origem))
        #self.VICL()
        print('\n')


    def addLut(self):
        print('\n--adicionando Lutador--')
        cod = int(input('digite o codigo: '))
        nome=input('digite o nome: ')
        sx = ''
        while (True):
            if sx == 'F' or sx == 'M':
                break
            if sx == 'f':
                sx = 'F'
                break
            if sx == 'm':
                sx = 'M'
                break
            sx = input('digite o sexo(F/M): ')
        idade = int(input('digite a idade: '))
        peso = float(input('digite o peso: '))
        pais_O = input('digite o pais de origem: ')
        categoriaP = self.defeniCategoria(peso,sx)
        lut = lutador(cod,nome,sx,idade,peso,pais_O,categoriaP)
        self.listaL.append(lut)
        print('\n')

    def remove(self):
        cr = int(input('digite o codigo do Lutador a ser removido: '))
        for i in range(0,len(self.listaL)):
            if (self.listaL[i].cod == cr):
                self.listaL.remove(self.listaL[i])
                break
        print('\n')

    def VisCate(self):
        print('---visualizando por categoria de peso---')
        catP = self.choiceOpC()
        for i in range(0,len(self.listaL)):
            if (self.listaL[i].categoria_Peso == catP):
                print('cod: {}| nome: {}| peso: {} quilos| categoria de peso: {}| sexo: {}| idade: {}| pais de origem: {}'
                  .format(self.listaL[i].cod, self.listaL[i].nome, self.listaL[i].peso,self.listaL[i].categoria_Peso,self.listaL[i].sexo,self.listaL[i].idade,
                          self.listaL[i].pais_Origem))
        print('\n')

    def VICL(self):
        print('\ndeseja escolhe um lutador para visualizar as informaçoes completa dele')
        print('ou continuar !')
        print('1-visualizar infor completa de Lutador')
        print('2-continuar')
        oc = int(input('digite a opcao: '))
        if (oc == 1):
            op=int(input('digite o codigo do Lutador para continuar: '))
            for i in range(0,len(self.listaL)):
                if (self.listaL[i].cod == op):
                    print('cod: {}| nome: {}| sexo: {}' .format(self.listaL[i].cod, self.listaL[i].nome, self.listaL[i].sexo))
                    print('idade: {}| peso: {} quilos| pais de origem: {}| categoria de peso: {}' .format(self.listaL[i].idade, self.listaL[i].peso,
                                                                                                  self.listaL[i].pais_Origem, self.listaL[i].categoria_Peso))

    def defeniCategoria(self,peso,sx):
        cat1= 'Peso Mosca'
        cat2= 'Peso Galo'
        cat3= 'Peso Pena'
        cat4= 'Peso Leve'
        cat5= 'Peso Meio-Medio'
        cat6= 'Peso Medio'
        cat7= 'Peso Meio-Pesado'
        cat8= 'Peso Pesado'
        catf= 'Peso Palha'
        if (sx == 'M' or sx == 'm'):
            if (peso <= 56.7):
                return cat1
            elif (peso > 56.7 and peso <= 61.2):
                return cat2
            elif (peso > 61.2 and peso <= 65.7):
                return cat3
            elif (peso > 65.7 and peso <= 70.3):
                return cat4
            elif (peso > 70.3 and peso <= 77.1):
                return cat5
            elif (peso > 77.1 and peso <= 83.9):
                return cat6
            elif (peso > 83.9 and peso <= 92.9):
                return cat7
            elif (peso > 92.9):
                return cat8
        elif (sx == 'F' or sx == 'f'):
            if (peso <= 52):
                return catf
            elif (peso > 52 and peso <= 52.2):
                return cat1
            elif (peso > 52.2 and peso <= 61.1):
                return cat2
            elif (peso > 61.1 and peso <= 65.7):
                return cat3
            elif (peso > 65.7 and peso <= 70.3):
                return cat4
            elif (peso > 70.3 and peso <= 77.1):
                return cat5
            elif (peso > 77.1 and peso <= 83.9):
                return cat6
            elif (peso > 83.9 and peso <= 92.9):
                return cat7
            elif (peso > 92.9):
                return cat8
            
    def choiceOpC(self):
        print('1-peso palha')
        print('2-peso mosca')
        print('3-peso galo')
        print('4-peso pena')
        print('5-peso leve')
        print('6-peso meio-medio')
        print('7-peso medio')
        print('8-peso meio-pesado')
        print('9-peso pesado')
        cat_peso = int(input('escolha a categoria de peso: '))
        if (cat_peso == 1):
            return 'Peso Palha'
        elif(cat_peso == 2):
            return 'Peso Mosca'
        elif(cat_peso == 3):
            return 'Peso Galo'
        elif(cat_peso == 4):
            return 'Peso Pena'
        elif(cat_peso == 5):
            return 'Peso Leve'
        elif(cat_peso == 6):
            return 'Peso Meio-Medio'
        elif(cat_peso == 7):
            return 'Peso Medio'
        elif(cat_peso == 8):
            return 'Peso Meio-Pesado'
        elif(cat_peso == 9):
            return 'Peso Pesado'
        else:
            return ''

    def proxCat(self):
        print('\n')
        Pnome = input('digite o nome de um Lutador: ')
        Ppeso = float(input('digite o peso: '))
        Apeso = 0
        cat = ''
        var = ''
        sx = ''
        for i in range(0,len(self.listaL)):
            if(self.listaL[i].nome == Pnome):
                Apeso = self.listaL[i].peso
                cat = self.listaL[i].categoria_Peso
                sx = self.listaL[i].sexo
                break
        if (cat == ''):
            print('nenhum lutador encontrado !!!\n\n')
        else:
            print('Lutador %s esta na categoria %s' % (Pnome,cat) )
            cat = self.defeniCategoria(Ppeso,sx)
            pesoI = Ppeso - Apeso
            if (pesoI >= 0):
                var = 'ganhar'
            else:
                var = 'perder'
                pesoI = -pesoI
            print('ele deve %s %.2f quilos para chegar na categoria %s' % (var,pesoI,cat) )
            print('\n')

    def visualizarHis(self):
        print('\nesse programa foi desenvolvimento por: Matheus Almeida\n\n')
        his = open('historia do UFC.txt','r')
        print (his.read())
        his.close()
        print('\n\n\n')
                


m = main()









