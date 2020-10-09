# OEIS CLI

## How to use

Create a virtualenv with python 3.5 or higher

Clone this repository to your local machine.

From inside the repository, install the CLI

```bash
$ pip install .
```

Then run the CLI command to find the sequence
```bash
$ oeis_query 1 1 2 3 5 7

1 - a(n) is the number of partitions of n (the partition numbers).
2 - a(n) = floor(3^n / 2^n).
3 - Quarter-squares plus 1 (that is, a(n) =
4 - Triangular array T read by rows: T(n,0) = T(n,2n) = 1 for n >= 0; T(n,1) = 1 for n >= 1; T(n,k) = T(n-1,k-2) + T(n-1,k-1) for k = 2..2n-1, n >= 2.
5 - Number of rooted trees with n nodes with every leaf at the same height.
```

## Notes
- Showing only first five results if more
- Missing add the information about the total results
- Handling failure fetching the oeis website
- If no match found, show message about it and return success result

## Next steps
- Add test case
