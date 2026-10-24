"""App de login simples com vulnerabilidade de inserção.

Este arquivo é um exemplo didático. Ele mostra um login com SQL montado por
concatenação de strings, o que permite uma vulnerabilidade de SQL Injection
(a primeira falha mais famosa da ApiA).

O objetivo deste exemplo é ensinar: (1) reconhecer o problema, (2) explicar a
exploração de forma segura, (3) citar a técnica do MITRE ATT&CK e (4) reescrever
o código com consulta parametrizada.
"""

# Dados fictícios — um banco de teste com um usuário de exemplo.
DADOS_USUARIOS = [
    {"id": 1, "nome": "Ana Silva", "usuario": "ana", "senha": "senha123"},
]


def autenticar_login(usuario, senha):
    """Função que deve ser corrigida.

    Perigo: estende a string da consulta com os dados do usuário, permitindo que
    um atacante altere a consulta. Exemplo de entrada maliciosa:

        usuario = ' OR '1'='1' --
        senha = qualquer

    Isso transforma a consulta em algo que sempre retorna o primeiro usuário, e
    a cláusula de senha é ignorada pelo comentário (--).
    """
    sql = (
        "SELECT id, nome FROM usuarios WHERE usuario = '"
        + usuario
        + "' AND senha = '"
        + senha
        + "'"
    )

    # Simula o banco de dados com a consulta que foi construída.
    print("Consulta SQL montada:")
    print(sql)
    print()

    # Simula o resultado. Para um exemplo real, um banco consultaria esta SQL.
    return DADOS_USUARIOS[0] if DADOS_USUARIOS else None


if __name__ == "__main__":
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    usuario_logado = autenticar_login(usuario, senha)
    if usuario_logado:
        print("Login OK. Bem-vindo,", usuario_logado["nome"])
    else:
        print("Login falhou.")
