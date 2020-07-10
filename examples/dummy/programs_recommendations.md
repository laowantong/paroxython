# Table of contents
- [`1 program of learning cost in [0.25, 0.5[`](#1-program-of-learning-cost-in-025-05)
    - [`prg3.py`](#program-prg3py-learning-cost-025)
- [`1 program of learning cost in [0.5, 1[`](#1-program-of-learning-cost-in-05-1)
    - [`prg2.py`](#program-prg2py-learning-cost-090625)
# Recommended programs

## 1 program of learning cost in [0.25, 0.5[

### Program `prg3.py` (learning cost 0.25)

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

| Cost  | Taxon | Location |
|----|----|----|
| 0 | `O` | 7 |
| 0 | `O/C/F/U` | 5 |
| 0 | `O/C/H` | 5 |
| 0 | `O/J` | 5, 9 |
| 0 | `O/N/P` | 1, 6 |
| 0 | `X/K` | 1 |
| 0 | `X/S` | 6 |
| 0 | `X/S/M` | 5 |
| 0 | `X/S/M/L` | 8 |
| 0 | `X/S/M/L/R` | 4-8 |
| 0 | `X/S/M/L/V` | 2 |
| 0 | `Y` | 6 |
| 0 | `Y/E` | 8 |
| 0.25 | `Y/T` | 1 |

---

## 1 program of learning cost in [0.5, 1[

### Program `prg2.py` (learning cost 0.90625)

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

| Cost  | Taxon | Location |
|----|----|----|
| 0 | `O` | 2, 6 |
| 0 | `O/C` | 7 |
| 0 | `O/N/P` | 1 |
| 0.25 | `X/G` | 8 |
| 0 | `X/S/M` | 6 |
| 0 | `X/S/M/L/R` | 7 |
| 0 | `X/S/M/L/R/D` | 2, 3, 9 |
| 0 | `X/S/M/L/V` | 8-9, 9 |
| 0 | `Y` | 1 |
| 0.25 | `Y/T` | 7 |
| 0.375 | `Y/T/Q` | 1, 9 |

---

# Summary
<details>
  <summary>9 initially.</summary>
  <ol>
    <li><code>prg1.py</code></li>
    <li><code>prg2.py</code></li>
    <li><code>prg3.py</code></li>
    <li><code>prg4.py</code></li>
    <li><code>prg5.py</code></li>
    <li><code>prg6.py</code></li>
    <li><code>prg7.py</code></li>
    <li><code>prg8.py</code></li>
    <li><code>prg9.py</code></li>
  </ol>
</details>

<details>
  <summary>8 remaining after operation 5 (impart) has filtered out 1 program.</summary>
  <ol>
    <li><code>prg8.py</code></li>
  </ol>
</details>

<details>
  <summary>6 remaining after operation 6 (exclude) has filtered out 2 programs.</summary>
  <ol>
    <li><code>prg7.py</code></li>
    <li><code>prg9.py</code></li>
  </ol>
</details>

<details>
  <summary>3 remaining after operation 7 (exclude) has filtered out 3 programs.</summary>
  <ol>
    <li><code>prg4.py</code></li>
    <li><code>prg5.py</code></li>
    <li><code>prg6.py</code></li>
  </ol>
</details>

<details>
  <summary>2 remaining after operation 8 (include) has filtered out 1 program.</summary>
  <ol>
    <li><code>prg1.py</code></li>
  </ol>
</details>

<details>
  <summary>2 remaining after operation 9 (hide) has filtered out 0 programs.</summary>
  
</details>
