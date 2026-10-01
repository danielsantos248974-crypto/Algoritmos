#Sistema de controle de qualidade para Indústrias de embalagem
 
#Declaração das variáveis globais ===========================================
caixas = [] #Lista  geral das caixas dos produtos
caixa = [] #Caixa das peças das embalagens
embalagem = ' ' #Conjunto das informações de cada embalagem -> id, cor, comprimento e peso
id = 0 #Indentificador único de cada embalagem
capacidade = 0 #Variável da capacidade da caixa
cores = [] #Lista das cores reprovadas
comprimentos = [] #Lista dos comprimentos reprovados
pesos = [] #Lista dos pesos reprovados
embalagem_aprovadas = 0 #Contador do número de embalagens aprovadas
embalagem_reprovadas = 0 #Contador do número de embalagens reprovadas
reprovadas = [] #Lista das embalagens reprovadas -> [id, cor, comprimento, peso]
 
print('Bem vindo ao sistema de controle de qualidade para embalagem.')
 
#Declaração das funções   
def cadastro(): #Funçaõ de cadastro de nova embalagem
    global caixas, caixa, id, capacidade, embalagem_aprovadas, embalagem_reprovadas, cores, comprimentos, pesos, embalagem #Declara as variáveis globais dentro da função
 
    #Cadastra as informações do objeto
    print('Responda as perguntas para cadastrar uma nova embalagem.')
    cor = input('Qual é a cor da embalagem? ')
    comprimento = int(input('Qual é o seu tamanho? (cm) '))
    peso = int(input('Quanto ela pesa? (g) '))
    embalagem = [id, cor, comprimento, peso] #Cria uma lista 'embalagem' com as características do objeto cadastrado
    id += 1 #Soma uma unidade ao id

#Avaliação da embalagem submetida a cadastro
    if (cor == 'azul' or cor == 'verde') and 10 <= comprimento <= 20 and 95 <= peso <= 105:
        if capacidade == 0: #Verifica se o contador está zerado
            caixa = [] #Cria uma lista 'caixa' vazia 
            print('Abrindo caixa...')
            caixas.append(caixa) #Adiciona a lista 'caixa' vazia na lista 'caixas'
            print('Caixa aberta com sucesso.')
 
        caixa.append(embalagem) #Adiciona no final da lista 'caixa' a lista 'embalagem'
        capacidade += 1 #Aumenta uma unidade no contador da capacidade
        embalagem_aprovadas += 1 #Registra que a embalagem foi registrada com sucesso
        print('Embalagem adicionada com sucesso.')
 
        if capacidade >= 10: #Verifica se a capacidade máxima foi atingida
            print('Caixa fechada, abrindo uma nova...')
            capacidade = 0  #Zera a capacidade
    else: #Registra as características que fizeram a embalagem submetida a cadastro ser reprovada
        if cor != 'azul' and cor != 'verde': 
            cores.append(cor)
        if not 10 <= comprimento <= 20 :
            comprimentos.append(comprimento)
        if not 95 <= peso <= 105:
            pesos.append(peso)
 
        reprovadas.append(embalagem) #Guarda a embalagem reprovada para listar e remover depois
        embalagem_reprovadas += 1
        print('Infelizmente essa embalagem não atende aos nossos padrões de qualidade')
        print('Tente cadastrar uma nova embalagem!')
 
#Função que monta os motivos de reprovação de uma embalagem
def motivos(embalagem):
    lista = []
    if embalagem[1] != 'azul' and embalagem[1] != 'verde':
        lista.append('cor')
    if not 10 <= embalagem[2] <= 20:
        lista.append('comprimento')
    if not 95 <= embalagem[3] <= 105:
        lista.append('peso')
    return ', '.join(lista)
 
def estoque(): #Função para exibir estoque (aprovadas e reprovadas)
        print('APROVADAS')
        print('id | cor | comprimento | peso')
        for caixa in caixas: #Percorre cada caixa em caixas
            for embalagem in caixa: #Percorre cada embalagem em caixa
                print(embalagem)
                print('-'*20)
            print('='*20)
 
        #Listagem das embalagens reprovadas
        print('REPROVADAS')
        print('id | cor | comprimento | peso | motivo')
        if not reprovadas:
            print('Nenhuma embalagem reprovada.')
        for embalagem in reprovadas:
            print(embalagem, '->', motivos(embalagem))
            print('-'*20)
 
#Função para remover uma embalagem cadastrada pelo id
def remover():
    global capacidade, embalagem_aprovadas, embalagem_reprovadas
 
    try:
        id_remover = int(input('Digite o id da embalagem que deseja remover: '))
    except ValueError:
        print('Id inválido!')
        return
 
    for caixa in caixas: #Procura nas caixas das aprovadas
        for embalagem in caixa:
            if embalagem[0] == id_remover:
                caixa.remove(embalagem)
                embalagem_aprovadas -= 1
                if caixa is caixas[-1] and capacidade > 0: #A embalagem estava na caixa aberta
                    capacidade -= 1
                    if capacidade == 0: #A caixa aberta ficou vazia, então é descartada
                        caixas.remove(caixa)
                print('Embalagem removida com sucesso.')
                return
 
    for embalagem in reprovadas: #Procura nas reprovadas
        if embalagem[0] == id_remover:
            reprovadas.remove(embalagem)
            embalagem_reprovadas -= 1
            #Remove também os valores das listas de motivos
            if embalagem[1] in cores:
                cores.remove(embalagem[1])
            if embalagem[2] in comprimentos:
                comprimentos.remove(embalagem[2])
            if embalagem[3] in pesos:
                pesos.remove(embalagem[3])
            print('Embalagem removida com sucesso.')
            return
 
    print('Nenhuma embalagem encontrada com esse id.')
 
#Função que devolve apenas as caixas fechadas
def fechadas():
    if capacidade > 0: #Existe uma caixa aberta, que é sempre a última
        return caixas[:-1]
    return caixas
 
#Função para listar as caixas fechadas
def listar_caixas_fechadas():
    if not fechadas():
        print('Nenhuma caixa fechada até o momento.')
    for numero, caixa in enumerate(fechadas(), start=1):
        print(f'Caixa {numero} - {len(caixa)} embalagens')
        for embalagem in caixa:
            print(embalagem)
        print('='*20)
 
def relatorio():
    #Exibe o relatório do sistema
 
    print("=" * 40)
    print("       RELATÓRIO CONSOLIDADO DE PRODUÇÃO")
    print("=" * 40)
    print(f"Total de peças aprovadas: {embalagem_aprovadas}.")
    print(f"Total de peças reprovadas: {embalagem_reprovadas}.")
    print("-" * 40)
    print("Motivos das reprovações:")
    if cores: 
        print(f"Cores são diferentes de azul ou verde: {len(cores)} peça(s).") #COMPLEMENTO: quantidade
    if comprimentos:
        print(f"Tamanhos estão fora do intervalo de 10 cm a 20 cm: {len(comprimentos)} peça(s).")
    if pesos: 
        print(f"Pesos estão fora do intervalo de 95 g a 105 g: {len(pesos)} peça(s).")
    for embalagem in reprovadas: #COMPLEMENTO: motivo de cada peça reprovada
        print(f"id {embalagem[0]}: {motivos(embalagem)}")
    print("-" * 40)
    print(f"Quantidade de caixas utilizadas: {len(caixas)}.") #COMPLEMENTO
    print(f"Caixas fechadas: {len(fechadas())}.") #COMPLEMENTO
    print("=" * 40)
 
while True: #Loop do sistema
    #Menu de escolha das opções disponíveis
    print(""" 
    ============================
    MENU
 
    Opções disponíveis:
    1. Cadastrar nova embalagem
    2. Listar embalagens aprovadas/reprovadas
    3. Remover embalagem cadastrada
    4. Listar caixas fechadas
    5. Gerar relatório final
    0. Sair
    ============================
    """)
 
    try: 
        opcao = int(input('Escolha umas das opções: ' )) #Input para escolher a opção das disponíveis no menu
    except(ValueError): #Tratamento de erro para valores diferentes de Int
        print('Opção inválida!')
        print('Escolhe uma opção entre 0 e 5.')
        continue #Volta ao menu em vez de usar 'opcao' sem valor
 
    if not 0<= opcao <=5: #Tratamento de erro para valores fora do intervalo de 0 a 5
        print('Opção inválida!')
        print('Escolha uma das opções do menu.')
 
    match opcao: #Faz a associação da opção escolhida com o índice das opções do menu
        case 1:
            cadastro()
        case 2: 
            estoque()
        case 3: 
            remover()
        case 4: 
            listar_caixas_fechadas()
        case 5:
            relatorio()
        case 0: 
            print('Encerrando o sistema.')
            break