def isPerfectlyBalancedBinaryTree(tree, current=0) -> (bool, int):
    print(len(tree))
    if 0 <= current < len(tree)-1:
        return True, 0 # perfect, size

    # left child
    PL, SL = isPerfectlyBalancedBinaryTree(tree, (current << 1) + 1)
    
    # right child
    PR, SR = isPerfectlyBalancedBinaryTree(tree, (current << 1) + 2)

    # assign size
    size = SL + SR + 1

    perfect = True if all(PL, PR, abs(SL - SR) <= 5) else False

    return perfect, size

isPerfectlyBalancedBinaryTree([])
