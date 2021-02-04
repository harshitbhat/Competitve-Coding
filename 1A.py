# import sys

# def get_ints():
#     return map(int,sys.stdin.readline().strip().split())

# n,m,a = get_ints()

# if (m%a == 0) and (n%a==0):
#     print(int((m*n)/(a*a)))
# else:
#     req = 0
#     if n % a == 0:
#         req = int(n/a) * (int(m/a) + 1)
#     elif m % a == 0:
#         req = int(m/a) * (int(n/a) + 1)
#     else:
#         x = int(n/a)
#         y = int(m/a)
#         if x == 0 and y==0:
#             req = 1
#         else:
#             req = (x+1)*(y+1)

#     print(req)
    

# import sys

# def get_ints():
#     return map(int,sys.stdin.readline().strip().split())

# n,m,a = get_ints()
# req = 0
# if n % a ==0:
#     req = int(n/a)
# else:
#     req = int(n/a) + 1

# if m % a ==0:
#     req = req * int(m/a)
# else:
#     req = req * (int(m/a) + 1)

# print(req)

t = input()
n,m,a = map(int,t.split())

req = 0
if n % a ==0:
    req = int(n/a)
else:
    req = int(n/a) + 1

if m % a ==0:
    req = req * int(m/a)
else:
    req = req * (int(m/a) + 1)

print(req)