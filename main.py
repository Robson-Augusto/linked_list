# Função principal [EXIGÊNCIA DE CÓDIGO 1 de 7];

def main(): 
    head = None 
    while True: 
        # [EXIGÊNCIA DE CÓDIGO 7 de 7];
        print("\n1 - Adicionar paciente a fila") 
        print("2 - Mostrar pacientes na fila") 
        print("3 - Chamar paciente") 
        print("4 - Sair") 
        selecao = int(input("Escolha uma opção acima: >> ")) 

        if selecao == 1: 
            head = inserir(head) 
        elif selecao == 2: 
            imprimirListaEspera(head) 
        elif selecao == 3: 
            head = atenderPaciente(head) 
        elif selecao == 4: 
            break 

class Nodo: 
    def __init__(self, numero, cor): 
        self.numero = numero 
        self.cor = cor 
        self.proximo = None 

 
# Função para inserir no final da lista [EXIGÊNCIA DE CÓDIGO 2 de 7];
def inserirSemPrioridade(Nodo, head): 
    if not head: 
        head = Nodo 
    else: 
        atual = head 
        while atual.proximo: 
            atual = atual.proximo 
        atual.proximo = Nodo 
    return head 


# Função para inserir após todos os Nodos com cor "A" [EXIGÊNCIA DE CÓDIGO 3 de 7];
def inserirComPrioridade(Nodo, head): 

    if not head: 
        head = Nodo 
    else: 
        if Nodo.cor == "A": 
            if Nodo.numero <= 201: 
                Nodo.proximo = head 
                head = Nodo 
            else: 
                atual = head 
                while atual.proximo and atual.proximo.cor == "A" and atual.proximo.numero <= 201: 
                    atual = atual.proximo 
                Nodo.proximo = atual.proximo 
                atual.proximo = Nodo 
        else: 
            atual = head 
            while atual.proximo and atual.proximo.cor == "A": 
                atual = atual.proximo 
            Nodo.proximo = atual.proximo 
            atual.proximo = Nodo 

    return head 


# Função para inserir um paciente na fila [EXIGÊNCIA DE CÓDIGO 4 de 7];
def inserir(head): 
    cor = input("Digite a cor do cartão (A/V): ") 
    
    if head == None:
        if cor == "V":
            numero = 1
        else:
            numero = 201
    else: 
        paciente = None 
        atual = head 
        while atual: 
            if atual.cor == cor and (paciente is None or atual.numero > paciente.numero): 
                paciente = atual 
            atual = atual.proximo 
        if paciente == None and cor == "V":
            numero = 1
        elif paciente == None and cor == "A":
             numero = 201
        else:
            numero =  paciente.numero+1

    Nodo_Nodo = Nodo(numero, cor) 
    if cor == "V": 
        head = inserirSemPrioridade(Nodo_Nodo, head) 
    elif cor == "A": 
        head = inserirComPrioridade(Nodo_Nodo, head) 
    return head 


# Função para imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista [EXIGÊNCIA DE CÓDIGO 5 de 7];
def imprimirListaEspera(head): 

    pacientes = [] 
    atual = head 
    while atual: 
        pacientes.append(atual) 
        atual = atual.proximo 
        
    pacientes.sort(key=lambda paciente: (paciente.cor != "A", paciente.numero)) 
        
    for paciente in pacientes: 
        print(f"Cartão {paciente.cor}: {paciente.numero}") 


# Função para atender o próximo paciente [EXIGÊNCIA DE CÓDIGO 6 de 7];
def atenderPaciente(head): 

    if not head: 
        print("Sem pacientes na fila.") 
        return head 
        
    paciente_atender = None 
    atual = head 
    while atual: 
        if atual.cor == "A" and (paciente_atender is None or atual.numero < paciente_atender.numero): 
            paciente_atender = atual 
        atual = atual.proximo 


    # Se não tiver pacientes com cartão A, atender o primeiro da fila 
    if paciente_atender is None: 
        paciente = head 
        head = head.proximo 
    else: 
        # Remover o paciente a ser atendido da lista 
        if paciente_atender == head: 
            head = head.proximo 
        else: 
            anterior = head 
            while anterior.proximo != paciente_atender: 
                anterior = anterior.proximo 
            anterior.proximo = paciente_atender.proximo 
        paciente = paciente_atender 
    print(f"Chamando paciente com cartão {paciente.cor}: {paciente.numero}") 
    return head 
main() 