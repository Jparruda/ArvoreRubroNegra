import arvore_rubro_negra
tree = arvore_rubro_negra.ArvoreRubroNegra()

# Inserir elementos na árvore
elements = [30,20,10]
for elem in elements:
    tree.insert(elem)

print("Árvore após inserções:")
print(tree)

# Buscar um elemento na árvore
key_to_search = 20
search_result = tree.search(key_to_search)
if search_result.key is not None:
    print(f"\nElemento {key_to_search} encontrado na árvore.")
else:
    print(f"\nElemento {key_to_search} não encontrado na árvore.")

# Deletar um elemento da árvore
tree.delete(20)
#  print(f"\nÁrvore após deletar o elemento {20}:")
print(tree)


# print(f"\nInserindo o valor 22 na árvore...")
# tree.insert(22)

# # Imprime a árvore após a nova inserção
# print("\nÁrvore após inserir o novo valor:")
# print(tree)

# print(f"\deletando o valor 18 na árvore...")
# tree.delete(18)

# # Imprime a árvore após a nova inserção
# print("\nÁrvore após deletar valor:")
# print(tree)