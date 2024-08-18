def atualizar_usuario(id_usuario, nome=None, email=None, senha=None):
    campos = []
    valores = []
    
    if nome:
        campos.append("nome = %s")
        valores.append(nome)
    if email:
        campos.append("email = %s")
        valores.append(email)
    if senha:
        campos.append("senha = %s")
        valores.append(senha)

    valores.append(id_usuario)
    
    sql = f"UPDATE Usuario SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def criar_usuario(nome, email, senha, dataCadastro):
    sql = """
    INSERT INTO Usuario (nome, email, senha, dataCadastro) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, email, senha, dataCadastro)
    cursor.execute(sql, valores)
    connection.commit()

def consultar_usuario_por_id(id_usuario):
    sql = "SELECT * FROM Usuario WHERE id = %s"
    cursor.execute(sql, (id_usuario,))
    return cursor.fetchone()

def consultar_todos_usuarios():
    sql = "SELECT * FROM Usuario"
    cursor.execute(sql)
    return cursor.fetchall()


def deletar_usuario(id_usuario):
    sql = "DELETE FROM Usuario WHERE id = %s"
    cursor.execute(sql, (id_usuario,))
    connection.commit()
