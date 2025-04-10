import unicodedata
import random

def gerar_serial(nome: str) -> str:
    nome_normalizado = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
    nome_formatado = nome_normalizado.upper().replace(" ", "-")
    sufixo = f"{random.randint(100000, 999999)}"
    return f"{nome_formatado}-{sufixo}"
