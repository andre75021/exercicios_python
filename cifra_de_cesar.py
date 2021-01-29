MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def cesar(data, key, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''

    for i in data:
        index = alfabeto.find(i)
        if index == -1 :
            new_data += i
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alfabeto)
            new_data += alfabeto[new_index:new_index+1]
    return new_data

key = 5


print('Escolha 1 para Encriptar')
print('Escolha 0 para Decriptar')
try:
    mode = int(input())
except:
    print('Opção inválida')
    
if mode == 1:
    mode = MODE_ENCRYPT
elif mode == 0 :
    mode = MODE_DECRYPT
else:
    print('Opção inválida')

msg = 'Entre com o texto a ser encriptado' if mode == MODE_ENCRYPT else 'Entre com o texto a ser decriptado'
print(msg)
data = input()

new = cesar(data,key,mode)
print(new)
