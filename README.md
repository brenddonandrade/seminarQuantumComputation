# Demonstração de Técnicas de Criptografia

Este repositório contém uma implementação didática de diferentes técnicas de criptografia, tanto clássicas quanto modernas, utilizando Python. O código foi desenvolvido para fins educacionais, demonstrando conceitos fundamentais de criptografia de forma prática.

## Técnicas Implementadas

### Criptografia de Chave Simétrica
1. **Block Cipher (Fernet)**
   - Implementação de cifra de bloco utilizando a biblioteca `cryptography`
   - Demonstração de criptografia e descriptografia
   - Exposição intencional da chave para fins didáticos

2. **Stream Cipher (ChaCha20)**
   - Implementação de cifra de fluxo
   - Uso de nonce para maior segurança
   - Demonstração de criptografia e descriptografia

### Criptografia Clássica
1. **Cifra de Substituição**
   - Implementação de cifra de substituição simples
   - Geração aleatória de chave
   - Suporte a caracteres especiais do português

2. **Cifra de Transposição**
   - Implementação de cifra de transposição
   - Uso de chave para determinar a ordem das colunas
   - Demonstração de criptografia e descriptografia

### Criptografia de Chave Assimétrica
- Geração de par de chaves pública/privada com RSA
- Criptografia e descriptografia assimétrica
- Demonstração de troca segura de mensagens

### Máquina Enigma (Simples)
- Implementação simplificada do mecanismo de rotores da Enigma
- Demonstração de criptografia simétrica histórica

## Requisitos

- Python 3.6+
- Bibliotecas Python:
  - `cryptography`
  - `string`
  - `math`
  - `random`
  - `os`

## Como Executar

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd [NOME_DO_REPOSITORIO]
   ```

2. Instale as dependências:
   ```bash
   pip install cryptography
   ```

3. Execute o código:
   ```bash
   python code.py
   ```

## Uso Educacional

Este código foi desenvolvido para fins educacionais e de demonstração. Ele inclui vulnerabilidades intencionais (como exposição de chaves) para fins didáticos. Não utilize este código em ambientes de produção sem as devidas revisões de segurança.


## Autor

Brenddon Andrade - brenddonandrade@gmail.com

## Agradecimentos

- Universidade Federal Fluminense (UFF)
- Departamento de Ciência da Computação
- Disciplina de Computação Quântica
