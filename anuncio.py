def atualizar_anuncio(id_anuncio, titulo=None, descricao=None, preco=None):
    campos = []
    valores = []
    
    if titulo:
        campos.append("titulo = %s")
        valores.append(titulo)
    if descricao:
        campos.append("descricao = %s")
        valores.append(descricao)
    if preco:
        campos.append("preco = %s")
        valores.append(preco)

    valores.append(id_anuncio)
    
    sql = f"UPDATE Anuncio SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def consultar_anuncio_por_id(id_anuncio):
    sql = "SELECT * FROM Anuncio WHERE id = %s"
    cursor.execute(sql, (id_anuncio,))
    return cursor.fetchone()

def consultar_anuncios_por_usuario(id_usuario):
    sql = "SELECT * FROM Anuncio WHERE idUsuario = %s"
    cursor.execute(sql, (id_usuario,))
    return cursor.fetchall()

def consultar_anuncios_por_categoria(id_categoria):
    sql = "SELECT * FROM Anuncio WHERE idCategoria = %s"
    cursor.execute(sql, (id_categoria,))
    return cursor.fetchall()

def criar_anuncio(titulo, descricao, preco, dataCriacao, id_usuario, id_categoria):
    sql = """
    INSERT INTO Anuncio (titulo, descricao, preco, dataCriacao, idUsuario, idCategoria) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (titulo, descricao, preco, dataCriacao, id_usuario, id_categoria)
    cursor.execute(sql, valores)
    connection.commit()

def deletar_anuncio(id_anuncio):
    sql = "DELETE FROM Anuncio WHERE id = %s"
    cursor.execute(sql, (id_anuncio,))
    connection.commit()
