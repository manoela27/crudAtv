def atualizar_categoria(id_categoria, nome=None):
    campos = []
    valores = []
    
    if nome:
        campos.append("nome = %s")
        valores.append(nome)

    valores.append(id_categoria)
    
    sql = f"UPDATE Categoria SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    connection.commit()

def consultar_categoria_por_id(id_categoria):
    sql = "SELECT * FROM Categoria WHERE id = %s"
    cursor.execute(sql, (id_categoria,))
    return cursor.fetchone()

def consultar_todas_categorias():
    sql = "SELECT * FROM Categoria"
    cursor.execute(sql)
    return cursor.fetchall()

def criar_categoria(nome):
    sql = "INSERT INTO Categoria (nome) VALUES (%s)"
    cursor.execute(sql, (nome,))
    connection.commit()

def deletar_categoria(id_categoria):
    sql = "DELETE FROM Categoria WHERE id = %s"
    cursor.execute(sql, (id_categoria,))
    connection.commit()
