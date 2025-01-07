import arvore_rubro_negra
tree = arvore_rubro_negra.ArvoreRubroNegra()

# Inserir elementos na árvore
elements = [20, 18, 17, 15, 25, 10, 5, 3, 2, 1]
for elem in elements:
    tree.insert(elem)

print("Árvore após inserções:")
print(tree)

# Buscar um elemento na árvore
key_to_search = 15
search_result = tree.search(key_to_search)
if search_result.key is not None:
    print(f"\nElemento {key_to_search} encontrado na árvore.")
else:
    print(f"\nElemento {key_to_search} não encontrado na árvore.")

# Deletar um elemento da árvore
key_to_delete = 15
tree.delete(key_to_delete)
print(f"\nÁrvore após deletar o elemento {key_to_delete}:")
print(tree)

novo_valor = 22
print(f"\nInserindo o valor {novo_valor} na árvore...")
tree.insert(novo_valor)

# Imprime a árvore após a nova inserção
print("\nÁrvore após inserir o novo valor:")
print(tree)