# Table of contents
- [`  2 programs of greater learning costs`](#2-programs-of-greater-learning-costs)
    - [`prg3.py`](#program-prg3py-learning-cost-256)
    - [`prg2.py`](#program-prg2py-learning-cost-928)
#   2 programs

##   2 programs of greater learning costs

### Program `prg3.py` (learning cost 256)

```python
1   1   O/N/P  X/K  Y/T
2   2   X/S/M/L/V
3   3   O/C/H/B
4   4   X/S/M/L/R+4
5   5   O/J  X/S/M  O/C/F/U  O/C/H
6   6   O/N/P  X/S  Y
7   7   O
8   8   X/S/M/L  Y/E
9   9   O/C/H/B  O/J
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0 | `O/N/P` | 1, 6 |
| 0 | `X/K` | 1 |
| 256 | `Y/T` | 1 |
| 0 | `X/S/M/L/V` | 2 |
| 0 | `O/C/H/B` | 3, 9 |
| 0 | `X/S/M/L/R` | 4-8 |
| 0 | `O/J` | 5, 9 |
| 0 | `X/S/M` | 5 |
| 0 | `O/C/F/U` | 5 |
| 0 | `O/C/H` | 5 |
| 0 | `X/S` | 6 |
| 0 | `Y` | 6 |
| 0 | `O` | 7 |
| 0 | `X/S/M/L` | 8 |
| 0 | `Y/E` | 8 |

### Program `prg2.py` (learning cost 928)

```python
1   1   O/N/P  Y/T/Q  Y
2   2   X/S/M/L/R/D  O
3   3   O/C/H/B  X/S/M/L/R/D
4   4
5   5
6   6   X/S/M  O
7   7   X/S/M/L/R  Y/T  O/C
8   8   X/G  X/S/M/L/V+1
9   9   X/S/M/L/R/D  X/S/M/L/V  Y/T/Q  O/C/H/B/I
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0 | `O/N/P` | 1 |
| 384 | `Y/T/Q` | 1, 9 |
| 0 | `Y` | 1 |
| 0 | `X/S/M/L/R/D` | 2, 3, 9 |
| 0 | `O` | 2, 6 |
| 0 | `O/C/H/B` | 3 |
| 0 | `X/S/M` | 6 |
| 0 | `X/S/M/L/R` | 7 |
| 256 | `Y/T` | 7 |
| 0 | `O/C` | 7 |
| 256 | `X/G` | 8 |
| 0 | `X/S/M/L/V` | 8-9, 9 |
| 32 | `O/C/H/B/I` | 9 |

# Quantitative summary
-   9 programs initially.
-   1 program filtered out by impart/programs/name.
-   2 programs filtered out by exclude/programs/name.
-   3 programs filtered out by exclude/taxons/pattern.
-   1 program filtered out by include/taxons/pattern.
-   2 programs remaining.
