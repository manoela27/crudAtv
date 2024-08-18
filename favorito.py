def adicionar_favorito(id_usuario, id_anuncio):
    sql = "INSERT INTO Favorito (idUsuario, idAnuncio) VALUES (%s, %s)"
    cursor.execute(sql, (id_usuario, id_anuncio))
    connection.commit()

def consultar_favoritos_por_usuario(id_usuario):
    sql = "SELECT * FROM Favorito WHERE idUsuario = %s"
    cursor.execute(sql, (id_usuario,))
    return cursor.fetchall()

def consultar_favoritos_por_anuncio(id_anuncio):
    sql = "SELECT * FROM Favorito WHERE idAnuncio = %s"
    cursor.execute(sql, (id_anuncio,))
    return cursor.fetchall()

def remover_favorito(id_usuario, id_anuncio):
    sql = "DELETE FROM Favorito WHERE idUsuario = %s AND idAnuncio = %s"
    cursor.execute(sql, (id_usuario, id_anuncio))
    connection.commit()
