# Explicação de cada CRUD 

## Usuário

### Criar
criar_usuario: Cria um novo usuário no sistema com nome, e-mail, senha e data de cadastro.

### Consultar
consultar_usuario_por_id: Retorna os dados de um usuário específico, identificado pelo seu ID.

consultar_todos_usuarios: Retorna todos os usuários cadastrados no sistema.

### Atualizar
atualizar_usuario: Atualiza as informações de um usuário existente, como nome, e-mail ou senha.

### Deletar
deletar_usuario: Remove um usuário do sistema com base no ID fornecido.

## Anúncio

### Criar
criar_anuncio: Cria um novo anúncio com título, descrição, preço, data de criação, ID do usuário (proprietário) e ID da categoria.

### Consultar
consultar_anuncio_por_id: Retorna os detalhes de um anúncio específico, identificado pelo seu ID.
consultar_anuncios_por_usuario: Retorna todos os anúncios de um usuário específico.
consultar_anuncios_por_categoria: Retorna todos os anúncios de uma categoria específica.

### Atualizar
atualizar_anuncio: Atualiza os detalhes de um anúncio existente, como título, descrição ou preço.

### Deletar
deletar_anuncio: Remove um anúncio do sistema com base no ID fornecido.

## Categoria

### Criar
criar_categoria: Cria uma nova categoria no sistema com um nome especificado.

### Consultar
consultar_categoria_por_id: Retorna os detalhes de uma categoria específica, identificada pelo seu ID.
consultar_todas_categorias: Retorna todas as categorias cadastradas no sistema.

### Atualizar
atualizar_categoria: Atualiza o nome de uma categoria existente.

### Deletar
deletar_categoria: Remove uma categoria do sistema com base no ID fornecido.

## Pergunta

### Criar
criar_pergunta: Cria uma nova pergunta associada a um anúncio específico.

### Consultar
consultar_pergunta_por_id: Retorna os detalhes de uma pergunta específica, identificada pelo seu ID.
consultar_perguntas_por_anuncio: Retorna todas as perguntas associadas a um anúncio específico.

### Atualizar
atualizar_pergunta: Atualiza o conteúdo de uma pergunta existente.

### Deletar
deletar_pergunta: Remove uma pergunta do sistema com base no ID fornecido.

## Resposta

### Criar
criar_resposta: Cria uma nova resposta associada a uma pergunta específica.

### Consultar
consultar_resposta_por_id: Retorna os detalhes de uma resposta específica, identificada pelo seu ID.
consultar_respostas_por_pergunta: Retorna todas as respostas associadas a uma pergunta específica.

### Atualizar
atualizar_resposta: Atualiza o conteúdo de uma resposta existente.

### Deletar
deletar_resposta: Remove uma resposta do sistema com base no ID fornecido.

## Compra
criar_compra: Registra uma nova compra associada a um anúncio, especificando a quantidade comprada.

consultar_compra_por_id: Retorna os detalhes de uma compra específica, identificada pelo seu ID.

consultar_compras_por_usuario: Retorna todas as compras realizadas por um usuário específico.

consultar_compras_por_anuncio: Retorna todas as compras associadas a um anúncio específico.

atualizar_compra: Atualiza a quantidade de itens comprados em uma compra existente.

deletar_compra: Remove uma compra do sistema com base no ID fornecido.

## Favorito
adicionar_favorito: Adiciona um anúncio à lista de favoritos de um usuário.

consultar_favoritos_por_usuario: Retorna todos os anúncios favoritos de um usuário específico.

consultar_favoritos_por_anuncio: Retorna todos os usuários que favoritaram um anúncio específico.

remover_favorito: Remove um anúncio da lista de favoritos de um usuário.

## Relatórios

consultar_relatorio_vendas: Gera um relatório de vendas para um usuário, mostrando o total vendido e o valor arrecadado por anúncio.

consultar_relatorio_compras: Gera um relatório de compras para um usuário, mostrando os anúncios comprados, a quantidade e o valor total gasto.