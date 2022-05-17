class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def search(self, key):
        if key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        elif key == self.key:
            return self
