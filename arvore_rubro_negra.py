import node

class ArvoreRubroNegra:
    def __init__(self):
        self.TNULL = node.Node(key=None, cor='preto')
        self.root = self.TNULL

    def insert(self, key):
        new_node = node.Node(key)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.cor = 'vermelho'
        self._fix_insert(new_node)

    def _fix_insert(self, k):
        while k.parent and k.parent.cor == 'vermelho':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.cor == 'vermelho':
                    u.cor = 'preto'
                    k.parent.cor = 'preto'
                    k.parent.parent.cor = 'vermelho'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.cor = 'preto'
                    k.parent.parent.cor = 'vermelho'
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.cor == 'vermelho':
                    u.cor = 'preto'
                    k.parent.cor = 'preto'
                    k.parent.parent.cor = 'vermelho'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.cor = 'preto'
                    k.parent.parent.cor = 'vermelho'
                    self._left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.cor = 'preto'

    def delete(self, key):
        self._delete_node_helper(self.root, key)

    def _delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Não foi possível encontrar a chave na árvore")
            return

        y = z
        y_original_cor = y.cor
        if z.left == self.TNULL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_cor = y.cor
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.cor = z.cor

        if y_original_cor == 'preto':
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.cor == 'preto':
            if x == x.parent.left:
                s = x.parent.right
                if s.cor == 'vermelho':
                    s.cor = 'preto'
                    x.parent.cor = 'vermelho'
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.cor == 'preto' and s.right.cor == 'preto':
                    s.cor = 'vermelho'
                    x = x.parent
                else:
                    if s.right.cor == 'preto':
                        s.left.cor = 'preto'
                        s.cor = 'vermelho'
                        self._right_rotate(s)
                        s = x.parent.right

                    s.cor = x.parent.cor
                    x.parent.cor = 'preto'
                    s.right.cor = 'preto'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.cor == 'vermelho':
                    s.cor = 'preto'
                    x.parent.cor = 'vermelho'
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.cor == 'preto' and s.left.cor == 'preto':
                    s.cor = 'vermelho'
                    x = x.parent
                else:
                    if s.left.cor == 'preto':
                        s.right.cor = 'preto'
                        s.cor = 'vermelho'
                        self._left_rotate(s)
                        s = x.parent.left

                    s.cor = x.parent.cor
                    x.parent.cor = 'preto'
                    s.left.cor = 'preto'
                    self._right_rotate(x.parent)
                    x = self.root
        x.cor = 'preto'

    def _rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        return self._search_tree_helper(self.root, key)

    def _search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def to_string(self, node=None, level=0, is_left=None):
        """Retorna a representação da árvore no formato inclinado solicitado."""
        if node is None:
            node = self.root

        # Garante que o nó TNULL é tratado corretamente
        if node == self.TNULL or node.key is None:
            return ""

        result = ""

        # Recorre para o filho à direita
        if node.right != self.TNULL:
            result += self.to_string(node.right, level + 1, is_left=False)

        # Adiciona o nó atual ao resultado com cor
        prefix = "    " * level
        connector = "-" if is_left is None else "╭ " if not is_left else "╰ "
        cor = "\033[91m" if node.cor == 'vermelho' else "\033[94m"  # Vermelho ou azul
        reset = "\033[0m"
        result += f"{prefix}{connector}{cor}{node.key}{reset}\n"

        # Recorre para o filho à esquerda
        if node.left != self.TNULL:
            result += self.to_string(node.left, level + 1, is_left=True)

        return result

    def __str__(self):
        return self.to_string()




