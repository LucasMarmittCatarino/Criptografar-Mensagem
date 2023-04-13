def teste():
    # Entrada de dados

    frase = input('Digite a frase a ser encriptada sem acentos: ')
    rotacao = int(input('Informe a chave: '))
    vetor_frase = list(frase)
    
    # Rotação dos caracteres
    for i in range(len(vetor_frase)):
        if vetor_frase[i].isalpha():
            valor_cifra = ord(vetor_frase[i].lower()) - ord('a')
            novo_valor_cifra = (valor_cifra + rotacao) % 26
            nova_letra = chr(ord('a') + novo_valor_cifra)
            vetor_frase[i] = nova_letra.upper() if vetor_frase[i].isupper() else nova_letra
    return ''.join(vetor_frase)

#Saida de dados
print(teste())