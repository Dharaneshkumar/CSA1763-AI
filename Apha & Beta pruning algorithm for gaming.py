import random
class Node:
    def __init__(self, heuristic=None, children=None):
        self.heuristic = heuristic  
        self.children = children if children is not None else []  
        self.terminal = False if children else True  
def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.terminal:
        return node.heuristic
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = alphabeta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = alphabeta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return minEval
def generate_random_tree(depth, branching_factor):
    if depth == 0:
        return Node(heuristic=random.randint(-10, 10)) 
    
    children = [generate_random_tree(depth - 1, branching_factor) for _ in range(branching_factor)]
    return Node(children=children)
if __name__ == "__main__":
    root = generate_random_tree(depth=3, branching_factor=2)
    result = alphabeta(root, depth=3, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
    
    print("Best heuristic value:", result)
