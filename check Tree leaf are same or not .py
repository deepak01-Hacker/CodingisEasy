#User function Template for python3

#Your task is to complete this function
#function should return True/False or 1/0

def check(node):
    stack = []
    stack.append(node)
    while(True):
        length = len(stack)
        if length :
            check = length 
            counter = 0
            null_counter = 0
            while(length):
                curr = stack.pop(0)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                if curr.left or curr.right:
                    counter += 1
                else:
                    null_counter += 1
                length -= 1
            if check != counter and check != null_counter:
                return 0
        else:
            break
    return 1
                
