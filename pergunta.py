def atualizar_pergunta(id_pergunta, conteudo=None):
    campos = []
    valores = []
    
    if conteudo:
        campos.append("conteudo = %s")
        valores.append(conteudo)

    valores.append(id_pergunta)
    
    sql = f"UPDATE Pergunta SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def consultar_pergunta_por_id(id_pergunta):
    sql = "SELECT * FROM Pergunta WHERE id = %s"
    cursor.execute(sql, (id_pergunta,))
    return cursor.fetchone()

def consultar_perguntas_por_anuncio(id_anuncio):
    sql = "SELECT * FROM Pergunta WHERE idAnuncio = %s"
    cursor.execute(sql, (id_anuncio,))
    return cursor.fetchall()

def criar_pergunta(conteudo, dataCriacao, id_usuario, id_anuncio):
    sql = """
    INSERT INTO Pergunta (conteudo, dataCriacao, idUsuario, idAnuncio) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (conteudo, dataCriacao, id_usuario, id_anuncio)
    cursor.execute(sql, valores)
    connection.commit()

def deletar_pergunta(id_pergunta):
    sql = "DELETE FROM Pergunta WHERE id = %s"
    cursor.execute(sql, (id_pergunta,))
    connection.commit()
