class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return

    queue = []  # Usamos una cola para el recorrido BFS
    queue.append(root)

    while queue:
        node = queue.pop(0)  # Sacamos el primer nodo de la cola
        print(node.value, end=' ')

        # Encolamos los hijos del nodo actual (si existen)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Crear un árbol binario de ejemplo
a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')
g = TreeNode('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

# Ejecutar BFS en el árbol
print("Recorrido BFS:")
bfs(a)