from typing import Tuple


def _heap_perm_(n, A):
    if n == 1: yield A
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, A): yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in _heap_perm_(n-1, A): yield hp


if __name__ == "__main__":
    arr = [1,2,3]
    for each in _heap_perm_(3,arr):
        print(each)


"""
Algorithm:

  procedure permutations (N);
      begin c:=1;
          loop:
              if N>2 then permutations(N-1)
              endif;
          while c<N:
              # Sedgewick uses :=: as the swap operator
              # Also see note below
              if N odd then P[N]:=:P[1] else P[N]:=:P[c] endif;
              c:=c+l
          repeat
       end;
"""