# Table of contents
- [`  2 programs of greater costs`](#--2-programs-of-greater-costs)
    - [`collatz_print.py`](#collatz_printpy)
    - [`fizzbuzz.py`](#fizzbuzzpy)
#   2 programs
##   2 programs of greater costs
### `collatz_print.py`
```python
def print_collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
```
-   1: `control_flow/conditional`
-   1: `control_flow/conditional/else`
-   1: `control_flow/loop/non_sequential`
-   2: `io/standard/print`
-   1: `operator/addition`
-   1: `operator/multiplication`
-   1: `operator/percent/modulo`
-   1: `subroutine_definition/argument/arg`
-   1: `subroutine_definition/procedure`
-   1: `test/divisibility/parity`
-   1: `test/equality`
-   1: `test/equality/not`
-   5: `type/elementary/number/integer`
-   1: `type/elementary/number/integer/zero`
-   1: `variable/assignment/conditional/verbose`
-   2: `variable/assignment/single`
### `fizzbuzz.py`
```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
-   1: `call/function/builtin/range`
-   3: `control_flow/conditional`
-   1: `control_flow/conditional/else`
-   2: `control_flow/conditional/else/if`
-   1: `control_flow/loop/sequential`
-   1: `control_flow/loop/sequential/arithmetic/start`
-   4: `io/standard/print`
-   3: `operator/percent/modulo`
-   3: `test/equality`
-   5: `type/elementary/number/integer`
-   3: `type/elementary/number/integer/zero`
-   3: `type/elementary/string`
# Quantitative summary
-   4 programs initially.
-   0 programs blacklisted.
-   0 programs tagged with a forbidden taxon.
-   0 programs not tagged with a mandatory taxon.
-   2 programs remaining.
