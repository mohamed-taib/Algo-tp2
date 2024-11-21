def swap(T, i, j):
    T[i], T[j] = T[j], T[i]


def entasser(T, n, i):
    big = i  
    left = (i * 2) + 1  
    right = (i * 2) + 2  

    if left < n and T[left] > T[big]:
        big = left

    if right < n and T[right] > T[big]:
        big = right

    if big != i:
        swap(T, i, big)  
        entasser(T, n, big)  


def construire_tas(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        parent = (i - 1) // 2  
        if parent >= 0 and T[parent] < T[i]:  
            swap(T, parent, i)
        entasser(T, n, i)

def tri_tas (r) :
      construire_tas(r)
      n = len(r)
      t=[]

      for i in range(n - 1, 0, -1):
        r[0], r[i] = r[i], r[0]
        t.append(r.pop())  
        entasser(r, len(r), 0)

      t.append(r[0])
      return t

# Example array
T = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
print("Original array:", T)

construire_tas(T)
print("Max heap:", T)

tri = tri_tas (T)
print("TAS tri :", tri) 

