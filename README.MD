# Projeto DIO — Simulação de Malwares em Python utilizando Ransomware e Keylogger

> Descrição do desafio: Implementar, documentar e compartilhar um projeto prático utilizando **Python** simulando o comportamento de malwares educacionais em um ambiente 100% controlado.

> O projeto envolve **Ransomware Simulado, Keylogger Simulado** e uma **reflexão sobre defesa, mitigação e boas práticas em segurança digital**.

>- **Ransomware Simulado: criptografar e descriptografar arquivos de teste, além de gerar uma nota de “resgate”.**
>- **Keylogger Simulado: registrar teclas em arquivo .txt, criar mecanismo de furtividade e implementar envio automático por e-mail.**
>- **Documentar as Evidências**: Keylogger Simulado: registrar teclas em arquivo .txt, criar mecanismo de furtividade e implementar envio automático por e-mail.
>- ⚠️ **Atenção: Este desafio é flexível!** Você pode seguir os cenários sugeridos ou adaptá-los, melhorando códigos, criando novos cenários e adicionando reflexões próprias. O principal é demonstrar entendimento prático, responsabilidade e aprendizado.


- Este repositório foi criado **exclusivamente para fins educacionais**, conforme orientações da DIO.

---

## Sumário
1. Objetivo
2. Arquitetura do laboratório
3. Pré-requisitos
4. Configuração do ambiente
5. Cenários de teste e comandos
   - Ransomware Simulado
   - Keylogger Simulado
   - Envio de Logs por E-mail
6. Scripts utilizados
7. Wordlists e arquivos auxiliares
8. Medidas de defesa e prevenção
9. Evidências e capturas
10. Referências

---

## 1. Objetivo
O objetivo desse README é de documentar e demonstrar em o funcionamento de dois malwares, **Ransomware** e **Keylogger** em ambiente controlado para fins educacionais, usando **Visual Studio Code**, e propor contramedidas.


## 2. Arquitetura do laboratório
- **Sistema operacional:** Windows, Linux ou macOS
- **Python 3.x instalado**
- **Scripts locais**
- **Ambiente completamente isolado ( recomendo)**

## 3. Pré-requisitos
- Python 3 instalado
- Editor de código (VSCode recomendado)
- Internet (somente para consulta às documentações oficiais)
- Conhecimento básico de:
 - arquivos e diretórios
 - execução de scripts
 - conceitos de segurança digital

Dependências opcionais:

| Biblioteca | Função | 
| -------- | ----- |
| cryptography        | Criptografia simétrica (Fernet)     |
| pynput        | Captura de teclado     | 
| smtplib        | Envio de e-mails pelo Python      | 


## 4. Configuração do ambiente
1. Crie os diretorios dentro do diretorio do projeto:
```bash
mkdir scripts output images
```
2. Criar ambiente virtual:
```bash
python -m venv venv
```
3. Ativar ambiente virtual:
Windows:
```bash
venv\Scripts\activate
```
Linux/macOS:
```bash
source venv/bin/activate
```
4. Instalar dependências:
```bash
pip install cryptography pynput
```

## 5. Cenários de teste e comandos
> Todos os comandos usados se encontram abaixo;

### 5.1 Ransomware Simulado
1. Criar arquivos de teste
```bash
echo "senha1:DIO_2025@hackers!@#" > ./test_files/senhas.txt
```
```bash
echo "John Doe
john.doe
Linkedn: John Doe
senha: 1234@" > ./test_files/dados_confidenciais.txt
```
2. Executar criptografia
```bash
python ./scripts/ransoware.py
```
Isso gera:

 - Arquivos criptografados
 - chave.key
 - LEIA ISSO.txt

3. Executar descriptografia
```bash
python ./scripts/descriptografar.py
```
- Acessar o servidor ftp utilizando os dados de sucessos do comando anterior.


### 5.2 Keylogger Simulado
- Captura de teclas em arquivo **.txt** e execução em background.

1. Executar keylogger
```bash
python ./scripts/keylogger.py
```
Saída gerada:
 - log.txt


### 5.3 Envio de Logs por E-mail
1. Configurar dentro do script:
```python
EMAIL_ORIGEM = "seuemail"
EMAIL_DESTINO = "destino"
SENHA_EMAIL = "suasenha"
```


## 6. Scripts utilizados
Os scripts completos estão localizados dentro do diretorio /scripts.

## 7. Wordlists e arquivos auxiliares
- Diretorio **/output**, contém:
 - arquivos gerados pelo ransoware
 - logs do keylogger
 - mensagem de resgate
 - chaves

- Diretorio **/test_files**, contém:
 - arquivos usados para criptografar e descriptografar.

## 8. Medidas de defesa e prevenção
| Categoria | Medidas recomendadas | 
| -------- | ----- |
| Antivírus        | Escaneamento em tempo real e assinaturas atualizadas     |
| Firewall        | Bloqueio de portas desnecessárias e tráfego suspeito     | 
| Sandboxing        | Testes de scripts desconhecidos em ambiente isolado     | 
| Boas práticas        | Não abrir anexos suspeitos, não executar programas desconhecidos     |
| Educação do usuário        | Treinamento contínuo sobre engenharia social e phishing    | 

## 9. Evidências e Capturas
Todas as evidencias serão encontradas nas pastas:
```bash
/output
/test_files
/scripts
/images
```
---

## 10. Referências
> As referências utilizadas neste projeto foram extraídas diretamente das orientações da DIO:
- Videoaulas e arquivos do curso Santander - Cibersegurança 2025 da DIO
- Instruções oficial do desafio
- Documentação Python https://docs.python.org/3/
- Cryptography (Fernet) https://cryptography.io/
- pynput – captura de teclado https://pypi.org/project/pynput/
- smtplib – envio de e-mails https://docs.python.org/3/library/smtplib.html


