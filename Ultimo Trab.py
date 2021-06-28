#Criar um algoritmo que lê valor para um vetor de 20 elementos e após ler um valor do teclado, faz numa função uma busca binária, por meio de recursividade. A função retorna o índice do vetor se
#estiver ou um valor para informar se não estiver.
    
def new_search2(v, chave, esquerda, direita):
    
    print('entrando na função new_search')
    
    # achar a metade do array
    media = (esquerda + direita) // 2
    
    print('minha metadedo array é ', media)
    
    if(esquerda>direita):
        print('O valor da esquerda do array é maior qu o valor da direita do array: ',esquerda,' - ',direita)
        return(-1)
        
    if(v[media]==chave): 
        print('O valor da metade do array igual a chave passada: ',v[media],' = ',chave)
        return media
    
    
    if(v[media] < chave): 
        print('O valor da metadedo array é menor que minha chave: ',v[media],' < ',chave)
        return new_search2(v, chave, media + 1, direita)
    else:
        print('O valor da metadedo array é maior que minha chave: ',v[media],' < ',chave)
        return new_search2(v, chave, esquerda, media -1)
    
def controlaValor(arr, valor):
    if (valor in vet):
        return controlaValor(vet, int(input('O valor digitado já foi digitado, digite um novo valor: ')))
    else:
        return valor

vet=[0]*20
for i in range(20):
    valor=int(input('Digite valor: '))
    vet[i]=controlaValor(vet, valor)
    
valor=int(input('Digite o valor a ser procurado no vetor: '))

vet.sort()
ret = new_search2(vet, valor, 0, len(vet) - 1)
if(ret>=0):
    print('O valor ',valor,' esta no vetor na posicao:',ret+1)
else:
    print('O valor ',valor,' nao esta no vetor')
print(vet)
