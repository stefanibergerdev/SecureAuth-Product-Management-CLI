import random, time, os

def gerar_token(usuario):
    token_aleatorio = random.randint(100000, 999999)
    return token_aleatorio

def registrar_log(usuario, acao):
    if os.path.exists("logs"):
        time.sleep(1)
        return {
            "usuario": usuario,
            "acao": acao,
            "status": "REGISTRADO"
        }

