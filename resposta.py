def atualizar_resposta(id_resposta, conteudo=None):
    campos = []
    valores = []
    
    if conteudo:
        campos.append("conteudo = %s")
        valores.append(conteudo)

    valores.append(id_resposta)
    
    sql = f"UPDATE Resposta SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def criar_resposta(conteudo, dataCriacao, id_pergunta, id_usuario):
    sql = """
    INSERT INTO Resposta (conteudo, dataCriacao, idPergunta, idUsuario) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (conteudo, dataCriacao, id_pergunta, id_usuario)
    cursor.execute(sql, valores)
    connection.commit()


def consultar_resposta_por_id(id_resposta):
    sql = "SELECT * FROM Resposta WHERE id = %s"
    cursor.execute(sql, (id_resposta,))
    return cursor.fetchone()

def consultar_respostas_por_pergunta(id_pergunta):
    sql = "SELECT * FROM Resposta WHERE idPergunta = %s"
    cursor.execute(sql, (id_pergunta,))
    return cursor.fetchall()

def deletar_resposta(id_resposta):
    sql = "DELETE FROM Resposta WHERE id = %s"
    cursor.execute(sql, (id_resposta,))
    connection.commit()
