"""
product('ABCD', repeat=2)

AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

permutations('ABCD', 2)

AB AC AD BA BC BD CA CB CD DA DB DC

combinations('ABCD', 2)

AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2)

AA AB AC AD BB BC BD CC CD DD     """
import itertools
a = map(int, input().split())
b = map(int, input().split())
#print(a)
#print(b)
#b=input().split()
#print(a)
#print(b)
out = tuple(itertools.product(a,b))
#print(tuple(out))
for x in out:
    print(x,end=" ")