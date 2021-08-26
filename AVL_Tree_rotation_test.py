# only in python
root=0



# LL-rotation
arr = [30, 20, None, 10, None, None, None]
print(arr)
temp = [arr[root*2+1], arr[(root*2+1)*2+1], arr[root]]
arr = temp[:]
print(arr)



# LR-rotation
arr = [30, 10, None, None, 20, None, None]
print(arr)
root=root*2+1
temp = arr[:root] + [arr[root*2+2], arr[root]] + arr[root*2+3:]
root = root//2
arr = [arr[root*2+1], arr[(root*2+1)*2+1], arr[root]]
print(arr, root)



# RL-rotation
arr = [10, None, 20, None, None, 30, None]
print(arr)
root=root*2+2
arr = arr[:root] + [arr[root*2+1], arr[root]] + arr[root*2+2:]
root=root//2-1
arr = [arr[root*2+2], arr[root], arr[(root*2+2)*2+2]]
print(arr, root)

# RR-rotation
arr = [10, None, 20, None, None, None, 30]
print(arr)
arr = [arr[root*2+2], arr[root], arr[(root*2+2)*2+2]]
print(arr)
