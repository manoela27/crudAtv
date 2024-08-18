def consultar_relatorio_vendas(id_usuario):
    sql = """
    SELECT Anuncio.titulo, SUM(Compra.quantidade) as total_vendido, SUM(Compra.quantidade * Anuncio.preco) as valor_total
    FROM Compra
    JOIN Anuncio ON Compra.idAnuncio = Anuncio.id
    WHERE Anuncio.idUsuario = %s
    GROUP BY Anuncio.id
    """
    cursor.execute(sql, (id_usuario,))
    return cursor.fetchall()

def consultar_relatorio_compras(id_usuario):
    sql = """
    SELECT Anuncio.titulo, Compra.quantidade, Compra.dataCompra, Anuncio.preco, (Compra.quantidade * Anuncio.preco) as valor_total
    FROM Compra
    JOIN Anuncio ON Compra.idAnuncio = Anuncio.id
    WHERE Compra.idUsuario = %s
    """
    cursor.execute(sql, (id_usuario,))
    return cursor.fetchall()
