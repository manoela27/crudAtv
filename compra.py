def atualizar_compra(id_compra, quantidade=None):
    campos = []
    valores = []
    
    if quantidade:
        campos.append("quantidade = %s")
        valores.append(quantidade)

    valores.append(id_compra)
    
    sql = f"UPDATE Compra SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def consultar_compras_por_anuncio(id_anuncio):
    sql = "SELECT * FROM Compra WHERE idAnuncio = %s"
    cursor.execute(sql, (id_anuncio,))
    return cursor.fetchall()

def criar_compra(dataCompra, quantidade, id_usuario, id_anuncio):
    sql = """
    INSERT INTO Compra (dataCompra, quantidade, idUsuario, idAnuncio) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (dataCompra, quantidade, id_usuario, id_anuncio)
    cursor.execute(sql, valores)
    connection.commit()

def deletar_compra(id_compra):
    sql = "DELETE FROM Compra WHERE id = %s"
    cursor.execute(sql, (id_compra,))
    connection.commit()
