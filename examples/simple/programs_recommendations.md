# Table of contents
- [`4 programs of learning cost in [2, 4[`](#4-programs-of-learning-cost-in-2-4)
    - [`09_indent.py`](#program-09_indentpy-learning-cost-2375)
    - [`08_arguments.py`](#program-08_argumentspy-learning-cost-28125)
    - [`04_fibonacci.py`](#program-04_fibonaccipy-learning-cost-29375)
    - [`20_prime_numbers.py`](#program-20_prime_numberspy-learning-cost-375)
- [`5 programs of learning cost in [4, 8[`](#5-programs-of-learning-cost-in-4-8)
    - [`10_time.py`](#program-10_timepy-learning-cost-45625)
    - [`21_xml_html_parsing.py`](#program-21_xml_html_parsingpy-learning-cost-53125)
    - [`12_classes.py`](#program-12_classespy-learning-cost-553125)
    - [`14_median.py`](#program-14_medianpy-learning-cost-59375)
    - [`33_guess_the_number.py`](#program-33_guess_the_numberpy-learning-cost-603125)
# Recommended programs

## 4 programs of learning cost in [2, 4[

### Program `09_indent.py` (learning cost 2.375)

```python
1   import glob
2   python_files = glob.glob("*.py")
3   for file_name in sorted(python_files):
4       print("    ------" + file_name)
5       with open(file_name) as f:
6           for line in f:
7               print("    " + line.rstrip())
8       print()
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 7 |
| 0 | `appli/function/builtin/open` | 5 |
| 0 | `appli/function/builtin/print` | 4, 7, 8 |
| 0 | `appli/function/builtin/sorted` | 3 |
| 0 | `appli/function/without_arguments` | 8 |
| 0.375 | `appli/method/glob` | 2 |
| 0.375 | `appli/method/rstrip` | 7 |
| 0 | `flow/loop/exit/late` | 3-8, 6-7 |
| 0 | `flow/loop/for` | 3-8 |
| 0 | `flow/loop/for/elements` | 6-7 |
| 0 | `flow/loop/for/nested/1` | 6-7 |
| 0.875 | `library/standard/glob` | 1 |
| 0.125 | `operator/string/concatenation` | 4, 7 |
| 0 | `type/sequence/string` | 7 |
| 0 | `type/sequence/string/literal` | 2, 4, 7 |
| 0 | `variable/assignment/single` | 2 |
| 0 | `metadata/program` | 1-8 |
| 0 | `metadata/sloc/8` | 1-8 |

---

### Program `08_arguments.py` (learning cost 2.8125)

```python
1   import sys
2   try:
3       total = sum(int(arg) for arg in sys.argv[1:])
4       print("sum =", total)
5   except ValueError:
6       print("Please supply integer arguments")
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 3 |
| 0 | `appli/function/builtin/casting/int` | 3 |
| 0 | `appli/function/builtin/print` | 4, 6 |
| 0 | `appli/function/builtin/sum` | 3 |
| 0 | `flow/exception/catch/ValueError` | 2-6 |
| 0.875 | `library/standard/sys` | 1 |
| 0.875 | `subscript/slice/start` | 3 |
| 0.375 | `type/number/integer` | 3 |
| 0.4375 | `type/number/integer/literal` | 3 |
| 0 | `type/sequence/string/literal` | 4, 6 |
| 0 | `variable/assignment/single` | 3 |
| 0 | `metadata/program` | 1-6 |
| 0 | `metadata/sloc/6` | 1-6 |

---

### Program `04_fibonacci.py` (learning cost 2.9375)

```python
1   parents, babies = (1, 1)
2   while babies < 100:
3       print("This generation has {} babies".format(babies))
4       parents, babies = (babies, parents + babies)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 3 |
| 0 | `appli/function/builtin/print` | 3 |
| 0.375 | `appli/method/format` | 3 |
| 0 | `flow/loop/exit/late` | 2-4 |
| 0 | `flow/loop/while` | 2-4 |
| 0.375 | `operator/arithmetic/addition` | 4 |
| 0.75 | `test/inequality` | 2 |
| 0.25 | `type/boolean` | 2 |
| 0.4375 | `type/number/integer/literal` | 1, 1, 2 |
| 0 | `type/sequence/string` | 3 |
| 0 | `type/sequence/string/literal` | 3 |
| 0.1875 | `type/sequence/tuple/literal` | 1, 1, 4, 4 |
| 0.125 | `variable/assignment/parallel` | 1 |
| 0.1875 | `variable/assignment/parallel/slide` | 4 |
| 0 | `metadata/program` | 1-4 |
| 0 | `metadata/sloc/4` | 1-4 |

---

### Program `20_prime_numbers.py` (learning cost 3.75)

```python
1   import itertools
2   def iter_primes():
3       numbers = itertools.count(2)
4       while True:
5           prime = next(numbers)
6           yield prime
7           numbers = filter(prime.__rmod__, numbers)
8   for p in iter_primes():
9       if p > 1000:
10          break
11      print(p)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.375 | `abstr/argument/no` | 2-7 |
| 0.25 | `abstr/generator` | 2-7 |
| 0 | `appli/function/builtin/filter` | 7 |
| 0 | `appli/function/builtin/next` | 5 |
| 0 | `appli/function/builtin/print` | 11 |
| 0 | `appli/function/without_arguments` | 8 |
| 0.375 | `appli/method/count` | 3 |
| 0 | `flow/conditional/no_else` | 9-10 |
| 0 | `flow/loop/exit/early/break` | 8-11 |
| 0 | `flow/loop/exit/late` | 4-7 |
| 0 | `flow/loop/for` | 8-11 |
| 0 | `flow/loop/while/infinite` | 4-7 |
| 0.875 | `library/standard/itertools` | 1 |
| 0.75 | `test/inequality` | 9 |
| 0.25 | `type/boolean` | 9 |
| 0.4375 | `type/boolean/literal/True` | 4 |
| 0.4375 | `type/number/integer/literal` | 3, 9 |
| 0 | `type/sequence` | 3 |
| 0 | `variable/assignment/single` | 3, 5, 7 |
| 0 | `metadata/program` | 1-11 |
| 0 | `metadata/sloc/11` | 1-11 |

---

## 5 programs of learning cost in [4, 8[

### Program `10_time.py` (learning cost 4.5625)

```python
1   from time import localtime
2   activities = {
3       8: "Sleeping",
4       9: "Commuting",
5       17: "Working",
6       18: "Commuting",
7       20: "Eating",
8       22: "Resting",
9   }
10  time_now = localtime()
11  hour = time_now.tm_hour
12  for activity_time in sorted(activities.keys()):
13      if hour < activity_time:
14          print(activities[activity_time])
15          break
16  else:
17      print("Unknown, AFK or sleeping!")
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 12 |
| 0 | `appli/function/builtin/print` | 14, 17 |
| 0 | `appli/function/builtin/sorted` | 12 |
| 0 | `appli/function/localtime` | 10 |
| 0 | `appli/function/without_arguments` | 10 |
| 0.375 | `appli/method/keys` | 12 |
| 0 | `flow/conditional/no_else` | 13-15 |
| 0 | `flow/loop/exit/early/break/else` | 12-17 |
| 0 | `flow/loop/for` | 12-17 |
| 0.9375 | `library/standard/time/localtime` | 1 |
| 0.75 | `subscript/index` | 14 |
| 0.75 | `test/inequality` | 13 |
| 0.25 | `type/boolean` | 13 |
| 0.375 | `type/non_sequence/dictionary` | 12 |
| 0.4375 | `type/non_sequence/dictionary/literal` | 2 |
| 0.4375 | `type/number/integer/literal` | 3, 4, 5, 6, 7, 8 |
| 0 | `type/sequence/string/literal` | 3, 4, 5, 6, 7, 8, 17 |
| 0 | `variable/assignment/single` | 2, 10, 11 |
| 0 | `metadata/program` | 1-17 |
| 0 | `metadata/sloc/17` | 1-17 |

---

### Program `21_xml_html_parsing.py` (learning cost 5.3125)

```python
1   dinner_recipe = """<html><body><table>
2   <tr><th>amt</th><th>unit</th><th>item</th></tr>
3   <tr><td>24</td><td>slices</td><td>baguette</td></tr>
4   <tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
5   <tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
6   <tr><td>1</td><td>jar</td><td>pesto</td></tr>
7   </table></body></html>"""
8   import xml.etree.ElementTree as etree
9   tree = etree.fromstring(dinner_recipe)
10  pantry = {"olive oil", "pesto"}
11  for ingredient in tree.getiterator("tr"):
12      amt, unit, item = ingredient
13      if item.tag == "td" and item.text not in pantry:
14          print("{}: {} {}".format(item.text, amt.text, unit.text))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 14 |
| 0 | `appli/function/builtin/print` | 14 |
| 0.375 | `appli/method/format` | 14 |
| 0.375 | `appli/method/fromstring` | 9 |
| 0.375 | `appli/method/getiterator` | 11 |
| 0 | `flow/conditional/no_else` | 13-14 |
| 0 | `flow/loop/exit/late` | 11-14 |
| 0 | `flow/loop/for` | 11-14 |
| 0.875 | `library/standard/xml.etree.ElementTree` | 8 |
| 0.375 | `operator/boolean/and` | 13 |
| 0.875 | `test/belonging/not` | 13 |
| 0.75 | `test/equality` | 13 |
| 0.25 | `type/boolean` | 13, 13 |
| 0.4375 | `type/non_sequence/set/literal` | 10 |
| 0 | `type/sequence/string` | 14 |
| 0 | `type/sequence/string/literal` | 7, 10, 10, 11, 13, 14 |
| 0.1875 | `type/sequence/tuple/literal` | 12 |
| 0.1875 | `variable/assignment/parallel/more_than_two` | 12 |
| 0 | `variable/assignment/single` | 1, 9, 10 |
| 0 | `metadata/program` | 1-14 |
| 0 | `metadata/sloc/14` | 1-14 |

---

### Program `12_classes.py` (learning cost 5.53125)

```python
1   class BankAccount(object):
2       def __init__(self, initial_balance=0):
3           self.balance = initial_balance
4       def deposit(self, amount):
5           self.balance += amount
6       def withdraw(self, amount):
7           self.balance -= amount
8       def overdrawn(self):
9           return self.balance < 0
10  my_account = BankAccount(15)
11  my_account.withdraw(50)
12  print(my_account.balance, my_account.overdrawn())
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.375 | `abstr/argument/arg` | 2, 2, 4, 4, 6, 6, 8 |
| 0.25 | `abstr/function` | 8-9 |
| 0.4375 | `abstr/method/flavor/instance` | 2-3, 4-5, 6-7, 8-9 |
| 0.4375 | `abstr/method/naming/magic` | 2-3 |
| 0 | `abstr/procedure` | 2-3, 4-5, 6-7 |
| 0.375 | `abstr/return/something` | 9 |
| 0.375 | `appli/class_constructor/BankAccount` | 10 |
| 0.25 | `appli/composition` | 12 |
| 0 | `appli/function/builtin/print` | 12 |
| 0.375 | `appli/method/overdrawn` | 12 |
| 0.375 | `appli/method/withdraw` | 11 |
| 0.75 | `test/inequality` | 9 |
| 0.25 | `type/boolean` | 9 |
| 0.4375 | `type/number/integer/literal` | 10, 11 |
| 0.46875 | `type/number/integer/literal/zero` | 2, 9 |
| 0 | `variable/assignment` | 3 |
| 0.1875 | `variable/assignment/augmented/Add` | 5 |
| 0.1875 | `variable/assignment/augmented/Sub` | 7 |
| 0 | `variable/assignment/single` | 10 |
| 0 | `metadata/program` | 1-12 |
| 0 | `metadata/sloc/12` | 1-12 |

---

### Program `14_median.py` (learning cost 5.9375)

```python
1   def median(pool):
2       copy = sorted(pool)
3       size = len(copy)
4       if size % 2 == 1:
5           return copy[int((size - 1) / 2)]
6       else:
7           return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.375 | `abstr/argument/arg` | 1 |
| 0.25 | `abstr/function` | 1-7 |
| 0.375 | `abstr/return/something` | 5, 7 |
| 0 | `appli/function/builtin/casting/int` | 5, 7, 7 |
| 0 | `appli/function/builtin/len` | 3 |
| 0 | `appli/function/builtin/sorted` | 2 |
| 0 | `flow/conditional` | 4-7 |
| 0 | `flow/conditional/else` | 7 |
| 0.375 | `operator/arithmetic/addition` | 7 |
| 0.375 | `operator/arithmetic/division` | 5, 7, 7, 7 |
| 0.375 | `operator/arithmetic/modulo` | 4 |
| 0.375 | `operator/arithmetic/substraction` | 5, 7 |
| 0.75 | `subscript/index` | 5, 7, 7 |
| 0.875 | `test/divisibility/parity` | 4 |
| 0.75 | `test/equality` | 4 |
| 0.25 | `type/boolean` | 4 |
| 0.375 | `type/number/integer` | 5, 7, 7 |
| 0.4375 | `type/number/integer/literal` | 4, 4, 5, 5, 7, 7, 7, 7 |
| 0 | `variable/assignment/single` | 2, 3 |
| 0 | `metadata/program` | 1-7 |
| 0 | `metadata/sloc/7` | 1-7 |

---

### Program `33_guess_the_number.py` (learning cost 6.03125)

```python
1   import random
2   guesses_made = 0
3   name = input("Hello! What is your name?\n")
4   number = random.randint(1, 20)
5   print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
6   while guesses_made < 6:
7       guess = int(input("Take a guess: "))
8       guesses_made += 1
9       if guess < number:
10          print("Your guess is too low.")
11      if guess > number:
12          print("Your guess is too high.")
13      if guess == number:
14          break
15  if guess == number:
16      print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses_made))
17  else:
18      print("Nope. The number I was thinking of was {}".format(number))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.25 | `appli/composition` | 5, 7, 16, 18 |
| 0 | `appli/function/builtin/casting/int` | 7 |
| 0 | `appli/function/builtin/input` | 3, 7 |
| 0 | `appli/function/builtin/print` | 5, 10, 12, 16, 18 |
| 0.375 | `appli/method/format` | 5, 16, 18 |
| 0.375 | `appli/method/randint` | 4 |
| 0 | `flow/conditional` | 15-18 |
| 0 | `flow/conditional/else` | 18 |
| 0 | `flow/conditional/no_else` | 9-10, 11-12, 13-14 |
| 0 | `flow/loop/exit/early/break` | 6-14 |
| 0 | `flow/loop/while` | 6-14 |
| 0.875 | `library/standard/random` | 1 |
| 0.9375 | `pattern/states/accumulate/count` | 6-14 |
| 0.75 | `test/equality` | 13, 15 |
| 0.75 | `test/inequality` | 6, 9, 11 |
| 0.25 | `type/boolean` | 6, 9, 11, 13, 15 |
| 0.375 | `type/number/integer` | 7 |
| 0.4375 | `type/number/integer/literal` | 4, 4, 6, 8 |
| 0.46875 | `type/number/integer/literal/zero` | 2 |
| 0 | `type/sequence/string` | 5, 16, 18 |
| 0 | `type/sequence/string/literal` | 3, 5, 7, 10, 12, 16, 18 |
| 0.1875 | `variable/assignment/augmented/Add` | 8 |
| 0 | `variable/assignment/single` | 2, 3, 4, 7 |
| 0 | `metadata/program` | 1-18 |
| 0 | `metadata/sloc/18` | 1-18 |

---

# Summary
<details>
  <summary>21 initially.</summary>
  <ol>
    <li><code>01_hello_world.py</code></li>
    <li><code>02_input_name.py</code></li>
    <li><code>03_friends.py</code></li>
    <li><code>04_fibonacci.py</code></li>
    <li><code>05_greet.py</code></li>
    <li><code>06_regex.py</code></li>
    <li><code>07_grocery_bill.py</code></li>
    <li><code>08_arguments.py</code></li>
    <li><code>09_indent.py</code></li>
    <li><code>10_time.py</code></li>
    <li><code>11_bottles.py</code></li>
    <li><code>12_classes.py</code></li>
    <li><code>13_unit_testing.py</code></li>
    <li><code>14_median.py</code></li>
    <li><code>15_itertools_groupby.py</code></li>
    <li><code>16_csv.py</code></li>
    <li><code>18_queens.py</code></li>
    <li><code>20_prime_numbers.py</code></li>
    <li><code>21_xml_html_parsing.py</code></li>
    <li><code>28_queens.py</code></li>
    <li><code>33_guess_the_number.py</code></li>
  </ol>
</details>

<details>
  <summary>19 remaining after operation 1 (impart) has filtered out 2 programs.</summary>
  <ol>
    <li><code>01_hello_world.py</code></li>
    <li><code>02_input_name.py</code></li>
  </ol>
</details>

<details>
  <summary>18 remaining after operation 2 (exclude) has filtered out 1 program.</summary>
  <ol>
    <li><code>03_friends.py</code></li>
  </ol>
</details>

<details>
  <summary>12 remaining after operation 3 (exclude) has filtered out 6 programs.</summary>
  <ol>
    <li><code>07_grocery_bill.py</code></li>
    <li><code>11_bottles.py</code></li>
    <li><code>15_itertools_groupby.py</code></li>
    <li><code>16_csv.py</code></li>
    <li><code>18_queens.py</code></li>
    <li><code>28_queens.py</code></li>
  </ol>
</details>

<details>
  <summary>10 remaining after operation 4 (include) has filtered out 2 programs.</summary>
  <ol>
    <li><code>05_greet.py</code></li>
    <li><code>06_regex.py</code></li>
  </ol>
</details>

<details>
  <summary>10 remaining after operation 5 (hide) has filtered out 0 programs.</summary>
  
</details>
