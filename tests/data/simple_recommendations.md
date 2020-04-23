# Table of contents
- [`1 program of learning cost in ]0.5, 1[`](#1-program-of-learning-cost-in-05-1)
    - [`assignment.py`](#program-assignmentpy-learning-cost-0875)
- [`1 program of learning cost in [8, 16[`](#1-program-of-learning-cost-in-8-16)
    - [`collatz_print.py`](#program-collatz_printpy-learning-cost-1384375)
- [`2 programs of learning cost in [16, 32[`](#2-programs-of-learning-cost-in-16-32)
    - [`fizzbuzz.py`](#program-fizzbuzzpy-learning-cost-183125)
    - [`is_even.py`](#program-is_evenpy-learning-cost-198125)
# Recommended programs

## 1 program of learning cost in ]0.5, 1[

### Program `assignment.py` (learning cost 0.875)

```python
1   a = b
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0.875 | `variable/assignment/single` | 1 |
---

## 1 program of learning cost in [8, 16[

### Program `collatz_print.py` (learning cost 13.84375)

```python
1   def print_collatz(n):
2       while n != 1:
3           print(n)
4           if n % 2 == 0:
5               n = n // 2
6           else:
7               n = 3 * n + 1
8       print(n)
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0.75 | `flow/conditional` | 4-7 |
| 0.875 | `flow/conditional/else` | 7 |
| 0.875 | `flow/loop/while` | 2-7 |
| 0.875 | `io/standard/print` | 3, 8 |
| 0.875 | `operator/arithmetic/addition` | 7 |
| 0.875 | `operator/arithmetic/modulo` | 4 |
| 0.875 | `operator/arithmetic/multiplication` | 7 |
| 0.875 | `subroutine/argument/arg` | 1 |
| 0.75 | `subroutine/procedure` | 1-8 |
| 0.875 | `test/divisibility/parity` | 4 |
| 0.75 | `test/equality` | 4 |
| 0.875 | `test/equality/not` | 2 |
| 0.9375 | `type/elementary/number/integer` | 2, 4, 5, 7, 7 |
| 0.96875 | `type/elementary/number/integer/zero` | 4 |
| 0.9375 | `variable/assignment/conditional/verbose` | 4-7 |
| 0.875 | `variable/assignment/single` | 5, 7 |
---

## 2 programs of learning cost in [16, 32[

### Program `fizzbuzz.py` (learning cost 18.3125)

```python
1   import collatz_print
2   for i in range(1, 101):
3       if i % 15 == 0:
4           print("FizzBuzz")
5       elif i % 3 == 0:
6           print("Fizz")
7       elif i % 5 == 0:
8           print("Buzz")
9       else:
10          print(i)
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0.9375 | `call/function/builtin/range` | 2 |
| 0.75 | `flow/conditional` | 3-10, 5-10, 7-10 |
| 0.875 | `flow/conditional/else` | 10 |
| 0.9375 | `flow/conditional/else/if` | 6, 8 |
| 0.96875 | `flow/loop/for/arithmetic/start` | 2-10 |
| 0.875 | `flow/loop/while` | _imported_ |
| 0.875 | `io/standard/print` | 4, 6, 8, 10 |
| 0.75 | `library/personal` | 1 |
| 0.875 | `operator/arithmetic/addition` | _imported_ |
| 0.875 | `operator/arithmetic/modulo` | 3, 5, 7 |
| 0.875 | `operator/arithmetic/multiplication` | _imported_ |
| 0.875 | `subroutine/argument/arg` | _imported_ |
| 0.75 | `subroutine/procedure` | _imported_ |
| 0.875 | `test/divisibility/parity` | _imported_ |
| 0.75 | `test/equality` | 3, 5, 7 |
| 0.875 | `test/equality/not` | _imported_ |
| 0.9375 | `type/elementary/number/integer` | 2, 2, 3, 5, 7 |
| 0.96875 | `type/elementary/number/integer/zero` | 3, 5, 7 |
| 0.875 | `type/elementary/string` | 4, 6, 8 |
| 0.9375 | `variable/assignment/conditional/verbose` | _imported_ |
| 0.875 | `variable/assignment/single` | _imported_ |
---

### Program `is_even.py` (learning cost 19.8125)

```python
1   import fizzbuzz
2   def is_even(n):
3       return n % 2 == 0
```

| Cost  | Taxon | Lines |
|----|----|----|
| 0.9375 | `call/function/builtin/range` | _imported_ |
| 0.75 | `flow/conditional` | _imported_ |
| 0.875 | `flow/conditional/else` | _imported_ |
| 0.9375 | `flow/conditional/else/if` | _imported_ |
| 0.96875 | `flow/loop/for/arithmetic/start` | _imported_ |
| 0.875 | `flow/loop/while` | _imported_ |
| 0.875 | `io/standard/print` | _imported_ |
| 0.75 | `library/personal` | 1 |
| 0.875 | `operator/arithmetic/addition` | _imported_ |
| 0.875 | `operator/arithmetic/modulo` | 3 |
| 0.875 | `operator/arithmetic/multiplication` | _imported_ |
| 0.875 | `subroutine/argument/arg` | 2 |
| 0.75 | `subroutine/function` | 2-3 |
| 0.75 | `subroutine/predicate` | 2-3 |
| 0.75 | `subroutine/procedure` | _imported_ |
| 0.875 | `test/divisibility/parity` | 3 |
| 0.75 | `test/equality` | 3 |
| 0.875 | `test/equality/not` | _imported_ |
| 0.9375 | `type/elementary/number/integer` | 3 |
| 0.96875 | `type/elementary/number/integer/zero` | 3 |
| 0.875 | `type/elementary/string` | _imported_ |
| 0.9375 | `variable/assignment/conditional/verbose` | _imported_ |
| 0.875 | `variable/assignment/single` | _imported_ |
---

# Summary
<details>
  <summary>4 initially.</summary>
  <ol>
    <li><code>assignment.py</code></li>
    <li><code>collatz_print.py</code></li>
    <li><code>fizzbuzz.py</code></li>
    <li><code>is_even.py</code></li>
  </ol>
</details>
