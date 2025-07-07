# %% [markdown]
# ## Symmetric Key Cryptography

# %% [markdown]
# ### Modern Cryptography - Block Cipher

# %%
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import math
import random
import string
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.fernet import Fernet

# GERANDO UMA CHAVE (normalmente você salvaria em um lugar seguro!)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# TEXTO ORIGINAL
mensagem = "Mensagem de Alice: Encontro secreto às 21h na doca 5."
print("Texto original:", mensagem)

# CRIPTOGRAFANDO
mensagem_bytes = mensagem.encode()
print("Texto após encode:", mensagem_bytes)

mensagem_criptografada = cipher_suite.encrypt(mensagem_bytes)
print("Texto criptografado:", mensagem_criptografada.decode())

# DEIXANDO FÁCIL PARA UM ESPIÃO ROUBAR
print("\n[!!!] Chave secreta deixada de forma insegura:", key.decode())

# ESPIÃO CAPTUROU A CHAVE
captured_key = Fernet(key)

# DESCRIPTOGRAFANDO
mensagem_descriptografada = cipher_suite.decrypt(
    mensagem_criptografada).decode()
print("Texto recebido por Bob após a descriptografia:", mensagem_descriptografada)

# DESCRIPTOGRAFANDO
mensagem_descriptografada_espiao = captured_key.decrypt(
    mensagem_criptografada).decode()
print("Texto visualizado pelo espião após a descriptografia:",
      mensagem_descriptografada)


# %% [markdown]
# ### Modern Cryptography - Stream Cipher

# %%

# Geração de chave de 32 bytes para ChaCha20
key = os.urandom(32)

# Nonce (número único para cada operação)
nonce = os.urandom(16)

# Texto original
mensagem = "Mensagem de Alice: Encontro secreto às 21h na doca 5."
mensagem = mensagem.encode()
print("Texto original:", mensagem.decode())

# Configurando o algoritmo ChaCha20
algoritmo = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algoritmo, mode=None, backend=default_backend())
encryptor = cipher.encryptor()

# Criptografando
mensagem_criptografada = encryptor.update(mensagem)
print("Texto criptografado:", mensagem_criptografada)

# Simulando o espião capturando a chave
algoritmo_espiao = algorithms.ChaCha20(key, nonce)
cipher_espiao = Cipher(algoritmo_espiao, mode=None, backend=default_backend())
decryptor = cipher_espiao.decryptor()

# Descriptografando
mensagem_descriptografada = decryptor.update(mensagem_criptografada)
print("Texto após descriptografia:", mensagem_descriptografada.decode())


# %% [markdown]
# ### Classifical Cryptography - Substitution Cipher

# %%

# Texto original
mensagem = "Mensagem de Alice: Encontro secreto às 21h na doca 5.".upper()
print("Texto original:", mensagem)

# Criando alfabeto e chave aleatória
alfabeto = string.ascii_uppercase + "ÁÀÂÃÉÊÍÓÔÕÚÇ"
letras_validas = [c for c in mensagem if c in alfabeto]
alfabeto_ajustado = ''.join(sorted(set(letras_validas)))
substituicao = list(alfabeto_ajustado)
random.shuffle(substituicao)
chave = dict(zip(alfabeto_ajustado, substituicao))
print("Chave de substituição:", chave)

# Criptografando
mensagem_criptografada = ''
for c in mensagem:
    if c in chave:
        mensagem_criptografada += chave[c]
    else:
        mensagem_criptografada += c

print("Texto criptografado:", mensagem_criptografada)

# Descriptografando
chave_invertida = {v: k for k, v in chave.items()}
mensagem_descriptografada = ''
for c in mensagem_criptografada:
    if c in chave_invertida:
        mensagem_descriptografada += chave_invertida[c]
    else:
        mensagem_descriptografada += c

print("Texto descriptografado:", mensagem_descriptografada)


# %% [markdown]
# ### Classifical Cryptography - Substitution Cipher

# %%


def criptografar_transposicao(texto, chave):
    texto = texto.replace(" ", "").upper()
    colunas = len(chave)
    linhas = math.ceil(len(texto) / colunas)
    matriz = [['' for _ in range(colunas)] for _ in range(linhas)]

    index = 0
    for i in range(linhas):
        for j in range(colunas):
            if index < len(texto):
                matriz[i][j] = texto[index]
                index += 1

    ordem_chave = sorted([(letra, i) for i, letra in enumerate(chave)])
    texto_criptografado = ''
    for letra, col in ordem_chave:
        for linha in matriz:
            texto_criptografado += linha[col]

    return texto_criptografado


def descriptografar_transposicao(texto_criptografado, chave):
    colunas = len(chave)
    linhas = math.ceil(len(texto_criptografado) / colunas)
    matriz = [['' for _ in range(colunas)] for _ in range(linhas)]

    ordem_chave = sorted([(letra, i) for i, letra in enumerate(chave)])
    index = 0
    for letra, col in ordem_chave:
        for linha in range(linhas):
            if index < len(texto_criptografado):
                matriz[linha][col] = texto_criptografado[index]
                index += 1

    texto_original = ''
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]:
                texto_original += matriz[i][j]

    return texto_original


# Mensagem e chave
mensagem = "MENSAGEMDEALICEENCONTROSECRETOAS21HNADOCA5"
chave = "SEGREDO"

# Criptografando
criptografado = criptografar_transposicao(mensagem, chave)
print("Texto criptografado:", criptografado)

# Descriptografando
descriptografado = descriptografar_transposicao(criptografado, chave)
print("Texto descriptografado:", descriptografado)


# %% [markdown]
# ## Asymmetric Key Cryptography

# %%

# GERANDO PAR DE CHAVES
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# TEXTO ORIGINAL
mensagem = "Mensagem de Alice: Encontro secreto às 21h na doca 5."
print("Texto original:", mensagem)

# CRIPTOGRAFANDO COM A CHAVE PÚBLICA
mensagem_bytes = mensagem.encode()
print("Texto após encode:", mensagem_bytes)

mensagem_criptografada = public_key.encrypt(
    mensagem_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
# print("Texto criptografado:", mensagem_criptografada.hex()[:100] + "...")  # Truncado para visualização
# Truncado para visualização
print("Texto criptografado:", mensagem_criptografada.hex())

# DEIXANDO A CHAVE PÚBLICA VAZADA (MAS ISSO É OK!)
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("\n[!!!] Chave pública vazada (espião pode ver isso):\n",
      public_key_pem.decode())

# TENTATIVA DO ESPIÃO (só tem a chave pública, não consegue descriptografar)
try:
    print("\nEspião tentando descriptografar com a chave pública...")
    mensagem_descriptografada_espiao = public_key.decrypt(  # Isso vai gerar erro
        mensagem_criptografada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
except Exception as e:
    print("⚠️ Falha! O espião não consegue descriptografar:", str(e))

# DESCRIPTOGRAFANDO COM A CHAVE PRIVADA
mensagem_descriptografada = private_key.decrypt(
    mensagem_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nTexto recebido por Bob após a descriptografia:",
      mensagem_descriptografada.decode())


# %%

# Alfabeto e substituições simples (rotores fictícios)
alfabeto = string.ascii_uppercase
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = dict(zip(alfabeto, alfabeto[::-1]))  # Refletor simples


def enigma_simples(mensagem, pos1, pos2, pos3):
    resultado = ""
    for letra in mensagem.upper():
        if letra not in alfabeto:
            resultado += letra
            continue

        # Passa pelo rotor 1
        idx = (alfabeto.index(letra) + pos1) % 26
        l1 = rotor1[idx]

        # Passa pelo rotor 2
        idx = (alfabeto.index(l1) + pos2) % 26
        l2 = rotor2[idx]

        # Passa pelo rotor 3
        idx = (alfabeto.index(l2) + pos3) % 26
        l3 = rotor3[idx]

        # Refletor
        l4 = reflector[l3]

        # Caminho inverso
        idx = rotor3.index(l4)
        l5 = alfabeto[(idx - pos3) % 26]

        idx = rotor2.index(l5)
        l6 = alfabeto[(idx - pos2) % 26]

        idx = rotor1.index(l6)
        l7 = alfabeto[(idx - pos1) % 26]

        resultado += l7

        # Roda os rotores
        pos1 = (pos1 + 1) % 26
        if pos1 == 0:
            pos2 = (pos2 + 1) % 26
            if pos2 == 0:
                pos3 = (pos3 + 1) % 26
    return resultado


# Exemplo de uso
mensagem = "ENCONTRO SECRETO AS 21H"
criptografada = enigma_simples(mensagem, pos1=4, pos2=11, pos3=5)
print('Mensagem original: ', mensagem)
print("Mensagem criptografada:", criptografada)
