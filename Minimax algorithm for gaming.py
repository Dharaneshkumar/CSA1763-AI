import random

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.terminal:
        return node.heuristic

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        self.terminal = False
        self.heuristic = 0

# Example usage
root = Node(0)
root.children = [Node(1), Node(2), Node(3)]

for child in root.children:
    child.children = [Node(4), Node(5), Node(6)]

print(minimax(root, 2, True))
