# Table of contents
- [`1 program of learning cost in [2, 4[`](#1-program-of-learning-cost-in-2-4)
    - [`01_hello_world.py`](#program-01_hello_worldpy-learning-cost-275)
- [`2 programs of learning cost in [4, 8[`](#2-programs-of-learning-cost-in-4-8)
    - [`05_greet.py`](#program-05_greetpy-learning-cost-5125)
    - [`02_input_ name.py`](#program-02_input_-namepy-learning-cost-63125)
- [`8 programs of learning cost in [8, 16[`](#8-programs-of-learning-cost-in-8-16)
    - [`06_regex.py`](#program-06_regexpy-learning-cost-8875)
    - [`08_arguments.py`](#program-08_argumentspy-learning-cost-1078125)
    - [`11_bottles.py`](#program-11_bottlespy-learning-cost-11625)
    - [`03_friends.py`](#program-03_friendspy-learning-cost-116875)
    - [`04_fibonacci.py`](#program-04_fibonaccipy-learning-cost-12375)
    - [`15_itertools_groupby.py`](#program-15_itertools_groupbypy-learning-cost-124375)
    - [`14_median.py`](#program-14_medianpy-learning-cost-1465625)
    - [`10_time.py`](#program-10_timepy-learning-cost-15859375)
- [`8 programs of learning cost in [16, 32[`](#8-programs-of-learning-cost-in-16-32)
    - [`09_indent.py`](#program-09_indentpy-learning-cost-1609375)
    - [`12_classes.py`](#program-12_classespy-learning-cost-1609375)
    - [`20_prime_numbers.py`](#program-20_prime_numberspy-learning-cost-1678125)
    - [`21_xml_html_parsing.py`](#program-21_xml_html_parsingpy-learning-cost-1696875)
    - [`13_unit_testing.py`](#program-13_unit_testingpy-learning-cost-2103125)
    - [`33_guess_the_number.py`](#program-33_guess_the_numberpy-learning-cost-2115625)
    - [`16_csv.py`](#program-16_csvpy-learning-cost-275)
    - [`18_queens.py`](#program-18_queenspy-learning-cost-2753125)
- [`1 program of learning cost in [32, 64[`](#1-program-of-learning-cost-in-32-64)
    - [`28_queens.py`](#program-28_queenspy-learning-cost-3621875)
# Recommended programs

## 1 program of learning cost in [2, 4[

### Program `01_hello_world.py` (learning cost 2.75)

```python
1   print ('Hello, world!')
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.9375 | `call/function/builtin/print` | 1 |
| 0.875 | `io/standard/print` | 1 |
| 0.9375 | `type/sequence/string/literal` | 1 |
| 0 | `metadata/program` | 1 |
| 0 | `metadata/sloc/1` | 1 |
---

## 2 programs of learning cost in [4, 8[

### Program `05_greet.py` (learning cost 5.125)

```python
1   def greet(name):
2       print ('Hello', name)
3   greet('Jack')
4   greet('Jill')
5   greet('Bob')
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/function` | 3, 4, 5 |
| 0.9375 | `call/function/builtin/print` | 2 |
| 0.875 | `io/standard/print` | 2 |
| 0.875 | `subroutine/argument/arg` | 1 |
| 0.75 | `subroutine/procedure` | 1-2 |
| 0.9375 | `type/sequence/string/literal` | 2, 3, 4, 5 |
| 0 | `metadata/program` | 1-5 |
| 0 | `metadata/sloc/5` | 1-5 |
---

### Program `02_input_ name.py` (learning cost 6.3125)

```python
1   name = input('What is your name?\n')
2   print ('Hi, %s.' % name)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.9375 | `call/function/builtin/input` | 1 |
| 0.9375 | `call/function/builtin/print` | 2 |
| 0.875 | `io/standard/input` | 1 |
| 0.875 | `io/standard/print` | 2 |
| 0.875 | `operator/string/format` | 2 |
| 0.9375 | `type/sequence/string/literal` | 1, 2 |
| 0.875 | `variable/assignment/single` | 1 |
| 0 | `metadata/program` | 1-2 |
| 0 | `metadata/sloc/2` | 1-2 |
---

## 8 programs of learning cost in [8, 16[

### Program `06_regex.py` (learning cost 8.875)

```python
1   import re
2   for test_string in ['555-1212', 'ILL-EGAL']:
3       if re.match(r'^\d{3}-\d{4}$', test_string):
4           print (test_string, 'is a valid US local phone number')
5       else:
6           print (test_string, 'rejected')
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.9375 | `call/function/builtin/print` | 4, 6 |
| 0.875 | `call/method/match` | 3 |
| 0.75 | `flow/conditional` | 3-6 |
| 0.875 | `flow/conditional/else` | 6 |
| 0.9375 | `flow/loop/exit/late` | 2-6 |
| 0.875 | `flow/loop/for` | 2-6 |
| 0.875 | `io/standard/print` | 4, 6 |
| 0.875 | `library/standard/re` | 1 |
| 0.9375 | `type/sequence/list/literal` | 2 |
| 0.9375 | `type/sequence/string/literal` | 2, 2, 3, 4, 6 |
| 0 | `metadata/program` | 1-6 |
| 0 | `metadata/sloc/6` | 1-6 |
---

### Program `08_arguments.py` (learning cost 10.78125)

```python
1   import sys
2   try:
3       total = sum(int(arg) for arg in sys.argv[1:])
4       print ('sum =', total)
5   except ValueError:
6       print ('Please supply integer arguments')
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 3 |
| 0.96875 | `call/function/builtin/casting/int` | 3 |
| 0.9375 | `call/function/builtin/print` | 4, 6 |
| 0.9375 | `call/function/builtin/sum` | 3 |
| 0.9375 | `flow/exception/catch/ValueError` | 2-6 |
| 0.875 | `io/standard/print` | 4, 6 |
| 0.875 | `library/standard/sys` | 1 |
| 0.875 | `subscript/slice/start` | 3 |
| 0.875 | `type/number/integer` | 3 |
| 0.9375 | `type/number/integer/literal` | 3 |
| 0.9375 | `type/sequence/string/literal` | 4, 6 |
| 0.875 | `variable/assignment/single` | 3 |
| 0 | `metadata/program` | 1-6 |
| 0 | `metadata/sloc/6` | 1-6 |
---

### Program `11_bottles.py` (learning cost 11.625)

```python
1   REFRAIN = '''
2   %d bottles of beer on the wall,
3   %d bottles of beer,
4   take one down, pass it around,
5   %d bottles of beer on the wall!
6   '''
7   bottles_of_beer = 9
8   while bottles_of_beer > 1:
9       print (REFRAIN % (bottles_of_beer, bottles_of_beer,
10          bottles_of_beer - 1))
11      bottles_of_beer -= 1
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.9375 | `call/function/builtin/print` | 9 |
| 0.9375 | `flow/loop/exit/late` | 8-11 |
| 0.875 | `flow/loop/while` | 8-11 |
| 0.875 | `io/standard/print` | 9 |
| 0.875 | `operator/arithmetic/modulo` | 9 |
| 0.875 | `operator/arithmetic/substraction` | 10 |
| 0.75 | `test/inequality` | 8 |
| 0.9375 | `type/number/integer/literal` | 7, 8, 10, 11 |
| 0.9375 | `type/sequence/string/literal` | 6 |
| 0.9375 | `type/sequence/tuple/literal` | 9 |
| 0.9375 | `variable/assignment/augmented/Sub` | 11 |
| 0.875 | `variable/assignment/constant` | 1 |
| 0.875 | `variable/assignment/single` | 1, 7 |
| 0 | `metadata/program` | 1-11 |
| 0 | `metadata/sloc/11` | 1-11 |
---

### Program `03_friends.py` (learning cost 11.6875)

```python
1   friends = ['john', 'pat', 'gary', 'michael']
2   for i, name in enumerate(friends):
3       print ("iteration {iteration} is {name}".format(iteration=i, name=name))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 3 |
| 0.9375 | `call/function/builtin/enumerate` | 2 |
| 0.9375 | `call/function/builtin/print` | 3 |
| 0.875 | `call/method/format` | 3 |
| 0.9375 | `flow/loop/exit/late` | 2-3 |
| 0.875 | `flow/loop/for` | 2-3 |
| 0.9375 | `flow/loop/for/elements_and_indexes` | 2-3 |
| 0.875 | `io/standard/print` | 3 |
| 0.9375 | `type/sequence/list/literal` | 1 |
| 0.875 | `type/sequence/string` | 3 |
| 0.9375 | `type/sequence/string/literal` | 1, 1, 1, 1, 3 |
| 0.9375 | `type/sequence/tuple/literal` | 2 |
| 0.875 | `variable/assignment/single` | 1 |
| 0 | `metadata/program` | 1-3 |
| 0 | `metadata/sloc/3` | 1-3 |
---

### Program `04_fibonacci.py` (learning cost 12.375)

```python
1   parents, babies = (1, 1)
2   while babies < 100:
3       print ('This generation has {0} babies'.format(babies))
4       parents, babies = (babies, parents + babies)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 3 |
| 0.9375 | `call/function/builtin/print` | 3 |
| 0.875 | `call/method/format` | 3 |
| 0.9375 | `flow/loop/exit/late` | 2-4 |
| 0.875 | `flow/loop/while` | 2-4 |
| 0.875 | `io/standard/print` | 3 |
| 0.875 | `operator/arithmetic/addition` | 4 |
| 0.75 | `test/inequality` | 2 |
| 0.9375 | `type/number/integer/literal` | 1, 1, 2 |
| 0.875 | `type/sequence/string` | 3 |
| 0.9375 | `type/sequence/string/literal` | 3 |
| 0.9375 | `type/sequence/tuple/literal` | 1, 1, 4, 4 |
| 0.875 | `variable/assignment/parallel` | 1 |
| 0.9375 | `variable/assignment/parallel/slide` | 4 |
| 0 | `metadata/program` | 1-4 |
| 0 | `metadata/sloc/4` | 1-4 |
---

### Program `15_itertools_groupby.py` (learning cost 12.4375)

```python
1   from itertools import groupby
2   lines = """
3   This is the
4   first paragraph.
5   This is the second.
6   """.splitlines()
7   for has_chars, frags in groupby(lines, bool):
8       if has_chars:
9           print(" ".join(frags))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 9 |
| 0.9375 | `call/function/builtin/print` | 9 |
| 0.875 | `call/function/groupby` | 7 |
| 0.875 | `call/method/join` | 9 |
| 0.875 | `call/method/splitlines` | 6 |
| 0.875 | `flow/conditional/no_else` | 8-9 |
| 0.9375 | `flow/loop/exit/late` | 7-9 |
| 0.875 | `flow/loop/for` | 7-9 |
| 0.875 | `io/standard/print` | 9 |
| 0.9375 | `library/standard/itertools/groupby` | 1 |
| 0.875 | `type/sequence/string` | 6, 9 |
| 0.9375 | `type/sequence/string/literal` | 6, 9 |
| 0.9375 | `type/sequence/tuple/literal` | 7 |
| 0.875 | `variable/assignment/single` | 2 |
| 0 | `metadata/program` | 1-9 |
| 0 | `metadata/sloc/9` | 1-9 |
---

### Program `14_median.py` (learning cost 14.65625)

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
| 0.96875 | `call/function/builtin/casting/int` | 5, 7, 7 |
| 0.9375 | `call/function/builtin/len` | 3 |
| 0.9375 | `call/function/builtin/sorted` | 2 |
| 0.75 | `flow/conditional` | 4-7 |
| 0.875 | `flow/conditional/else` | 7 |
| 0.875 | `operator/arithmetic/addition` | 7 |
| 0.875 | `operator/arithmetic/division` | 5, 7, 7, 7 |
| 0.875 | `operator/arithmetic/modulo` | 4 |
| 0.875 | `operator/arithmetic/substraction` | 5, 7 |
| 0.875 | `subroutine/argument/arg` | 1 |
| 0.75 | `subroutine/function` | 1-7 |
| 0.75 | `subscript/index` | 5, 7, 7 |
| 0.875 | `test/divisibility/parity` | 4 |
| 0.75 | `test/equality` | 4 |
| 0.875 | `type/number/integer` | 5, 7, 7 |
| 0.9375 | `type/number/integer/literal` | 4, 4, 5, 5, 7, 7, 7, 7 |
| 0.875 | `variable/assignment/single` | 2, 3 |
| 0 | `metadata/program` | 1-7 |
| 0 | `metadata/sloc/7` | 1-7 |
---

### Program `10_time.py` (learning cost 15.859375)

```python
1   from time import localtime
2   activities = {8: 'Sleeping',
3                 9: 'Commuting',
4                 17: 'Working',
5                 18: 'Commuting',
6                 20: 'Eating',
7                 22: 'Resting' }
8   time_now = localtime()
9   hour = time_now.tm_hour
10  for activity_time in sorted(activities.keys()):
11      if hour < activity_time:
12          print (activities[activity_time])
13          break
14  else:
15      print ('Unknown, AFK or sleeping!')
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 10 |
| 0.9375 | `call/function/builtin/print` | 12, 15 |
| 0.9375 | `call/function/builtin/sorted` | 10 |
| 0.875 | `call/function/localtime` | 8 |
| 0.875 | `call/function/without_arguments` | 8 |
| 0.875 | `call/method/keys` | 10 |
| 0.875 | `flow/conditional/no_else` | 11-13 |
| 0.984375 | `flow/loop/exit/early/break/else` | 10-15 |
| 0.875 | `flow/loop/for` | 10-15 |
| 0.875 | `io/standard/print` | 12, 15 |
| 0.9375 | `library/standard/time/localtime` | 1 |
| 0.75 | `subscript/index` | 12 |
| 0.75 | `test/inequality` | 11 |
| 0.875 | `type/non_sequence/dictionary` | 10 |
| 0.9375 | `type/non_sequence/dictionary/literal` | 2 |
| 0.9375 | `type/number/integer/literal` | 2, 3, 4, 5, 6, 7 |
| 0.9375 | `type/sequence/string/literal` | 2, 3, 4, 5, 6, 7, 15 |
| 0.875 | `variable/assignment/single` | 2, 8, 9 |
| 0 | `metadata/program` | 1-15 |
| 0 | `metadata/sloc/15` | 1-15 |
---

## 8 programs of learning cost in [16, 32[

### Program `09_indent.py` (learning cost 16.09375)

```python
1   import glob
2   python_files = glob.glob('*.py')
3   for file_name in sorted(python_files):
4       print ('    ------' + file_name)
5       with open(file_name) as f:
6           for line in f:
7               print ('    ' + line.rstrip())
8       print()
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 7 |
| 0.9375 | `call/function/builtin/open` | 5 |
| 0.9375 | `call/function/builtin/print` | 4, 7, 8 |
| 0.9375 | `call/function/builtin/sorted` | 3 |
| 0.875 | `call/function/without_arguments` | 8 |
| 0.875 | `call/method/glob` | 2 |
| 0.875 | `call/method/rstrip` | 7 |
| 0.9375 | `flow/loop/exit/late` | 3-8, 6-7 |
| 0.875 | `flow/loop/for` | 3-8 |
| 0.9375 | `flow/loop/for/elements` | 6-7 |
| 0.96875 | `flow/loop/for/nested/1` | 6-7 |
| 0.875 | `io/file/open` | 5 |
| 0.875 | `io/standard/print` | 4, 7, 8 |
| 0.875 | `library/standard/glob` | 1 |
| 0.875 | `operator/string/concatenation` | 4, 7 |
| 0.875 | `type/sequence/string` | 7 |
| 0.9375 | `type/sequence/string/literal` | 2, 4, 7 |
| 0.875 | `variable/assignment/single` | 2 |
| 0 | `metadata/program` | 1-8 |
| 0 | `metadata/sloc/8` | 1-8 |
---

### Program `12_classes.py` (learning cost 16.09375)

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
| 0.875 | `call/class_constructor/BankAccount` | 10 |
| 0.75 | `call/composition` | 12 |
| 0.9375 | `call/function/builtin/print` | 12 |
| 0.875 | `call/method/overdrawn` | 12 |
| 0.875 | `call/method/withdraw` | 11 |
| 0.5 | `class` | 1-9 |
| 0.875 | `io/standard/print` | 12 |
| 0.875 | `subroutine/argument/arg` | 2, 2, 4, 4, 6, 6, 8 |
| 0.75 | `subroutine/function` | 8-9 |
| 0.9375 | `subroutine/method/flavor/instance` | 2-3, 4-5, 6-7, 8-9 |
| 0.9375 | `subroutine/method/naming/magic` | 2-3 |
| 0.75 | `subroutine/procedure` | 2-3, 4-5, 6-7 |
| 0.75 | `test/inequality` | 9 |
| 0.9375 | `type/number/integer/literal` | 10, 11 |
| 0.96875 | `type/number/integer/literal/zero` | 2, 9 |
| 0.75 | `variable/assignment` | 3 |
| 0.9375 | `variable/assignment/augmented/Add` | 5 |
| 0.9375 | `variable/assignment/augmented/Sub` | 7 |
| 0.875 | `variable/assignment/single` | 10 |
| 0 | `metadata/program` | 1-12 |
| 0 | `metadata/sloc/12` | 1-12 |
---

### Program `20_prime_numbers.py` (learning cost 16.78125)

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
| 0.9375 | `call/function/builtin/filter` | 7 |
| 0.9375 | `call/function/builtin/next` | 5 |
| 0.9375 | `call/function/builtin/print` | 11 |
| 0.875 | `call/function/without_arguments` | 8 |
| 0.875 | `call/method/count` | 3 |
| 0.875 | `flow/conditional/no_else` | 9-10 |
| 0.96875 | `flow/loop/exit/early/break` | 8-11 |
| 0.9375 | `flow/loop/exit/late` | 4-7 |
| 0.875 | `flow/loop/for` | 8-11 |
| 0.9375 | `flow/loop/while/infinite` | 4-7 |
| 0.875 | `io/standard/print` | 11 |
| 0.875 | `library/standard/itertools` | 1 |
| 0.875 | `subroutine/argument/no` | 2-7 |
| 0.75 | `subroutine/generator` | 2-7 |
| 0.75 | `test/inequality` | 9 |
| 0.9375 | `type/boolean/literal/true` | 4 |
| 0.9375 | `type/number/integer/literal` | 3, 9 |
| 0.75 | `type/sequence` | 3 |
| 0.875 | `variable/assignment/single` | 3, 5, 7 |
| 0 | `metadata/program` | 1-11 |
| 0 | `metadata/sloc/11` | 1-11 |
---

### Program `21_xml_html_parsing.py` (learning cost 16.96875)

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
10  pantry = set(["olive oil", "pesto"])
11  for ingredient in tree.getiterator("tr"):
12      amt, unit, item = ingredient
13      if item.tag == "td" and item.text not in pantry:
14          print("%s: %s %s" % (item.text, amt.text, unit.text))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.96875 | `call/function/builtin/casting/set` | 10 |
| 0.9375 | `call/function/builtin/print` | 14 |
| 0.875 | `call/method/fromstring` | 9 |
| 0.875 | `call/method/getiterator` | 11 |
| 0.875 | `flow/conditional/no_else` | 13-14 |
| 0.9375 | `flow/loop/exit/late` | 11-14 |
| 0.875 | `flow/loop/for` | 11-14 |
| 0.875 | `io/standard/print` | 14 |
| 0.875 | `library/standard/xml.etree.ElementTree` | 8 |
| 0.875 | `operator/boolean/and` | 13 |
| 0.875 | `operator/string/format` | 14 |
| 0.875 | `test/belonging/not` | 13 |
| 0.75 | `test/equality` | 13 |
| 0.875 | `type/non_sequence/set` | 10 |
| 0.9375 | `type/sequence/list/literal` | 10 |
| 0.9375 | `type/sequence/string/literal` | 7, 10, 10, 11, 13, 14 |
| 0.9375 | `type/sequence/tuple/literal` | 12, 14 |
| 0.9375 | `variable/assignment/parallel/more_than_two` | 12 |
| 0.875 | `variable/assignment/single` | 1, 9, 10 |
| 0 | `metadata/program` | 1-14 |
| 0 | `metadata/sloc/14` | 1-14 |
---

### Program `13_unit_testing.py` (learning cost 21.03125)

```python
1   import unittest
2   def median(pool):
3       copy = sorted(pool)
4       size = len(copy)
5       if size % 2 == 1:
6           return copy[int((size - 1) / 2)]
7       else:
8           return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2
9   class TestMedian(unittest.TestCase):
10      def testMedian(self):
11          self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 11 |
| 0.75 | `call/function` | 11 |
| 0.96875 | `call/function/builtin/casting/int` | 6, 8, 8 |
| 0.9375 | `call/function/builtin/len` | 4 |
| 0.9375 | `call/function/builtin/sorted` | 3 |
| 0.875 | `call/method/assertEqual` | 11 |
| 0.5 | `class` | 9-11 |
| 0.75 | `flow/conditional` | 5-8 |
| 0.875 | `flow/conditional/else` | 8 |
| 0.875 | `library/standard/unittest` | 1 |
| 0.875 | `operator/arithmetic/addition` | 8 |
| 0.875 | `operator/arithmetic/division` | 6, 8, 8, 8 |
| 0.875 | `operator/arithmetic/modulo` | 5 |
| 0.875 | `operator/arithmetic/substraction` | 6, 8 |
| 0.875 | `subroutine/argument/arg` | 2, 10 |
| 0.75 | `subroutine/function` | 2-8 |
| 0.9375 | `subroutine/method/flavor/instance` | 10-11 |
| 0.75 | `subroutine/procedure` | 10-11 |
| 0.75 | `subscript/index` | 6, 8, 8 |
| 0.875 | `test/divisibility/parity` | 5 |
| 0.75 | `test/equality` | 5 |
| 0.875 | `type/number/integer` | 6, 8, 8 |
| 0.9375 | `type/number/integer/literal` | <details><summary>5, 5, 6, 6, 8, 8, 8, 8, 11,</summary>11, 11, 11, 11, 11, 11, 11,<br>11, 11</details> |
| 0.9375 | `type/sequence/list/literal` | 11 |
| 0.875 | `variable/assignment/single` | 3, 4 |
| 0 | `metadata/program` | 1-11 |
| 0 | `metadata/sloc/11` | 1-11 |
---

### Program `33_guess_the_number.py` (learning cost 21.15625)

```python
1   import random
2   guesses_made = 0
3   name = input("Hello! What is your name?\n")
4   number = random.randint(1, 20)
5   print("Well, {0}, I am thinking of a number between 1 and 20.".format(name))
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
16      print("Good job, {0}! You guessed my number in {1} guesses!".format(name, guesses_made))
17  else:
18      print("Nope. The number I was thinking of was {0}".format(number))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 5, 7, 16, 18 |
| 0.96875 | `call/function/builtin/casting/int` | 7 |
| 0.9375 | `call/function/builtin/input` | 3, 7 |
| 0.9375 | `call/function/builtin/print` | 5, 10, 12, 16, 18 |
| 0.875 | `call/method/format` | 5, 16, 18 |
| 0.875 | `call/method/randint` | 4 |
| 0.75 | `flow/conditional` | 15-18 |
| 0.875 | `flow/conditional/else` | 18 |
| 0.875 | `flow/conditional/no_else` | 9-10, 11-12, 13-14 |
| 0.96875 | `flow/loop/exit/early/break` | 6-14 |
| 0.875 | `flow/loop/while` | 6-14 |
| 0.875 | `io/standard/input` | 3, 7 |
| 0.875 | `io/standard/print` | 5, 10, 12, 16, 18 |
| 0.875 | `library/standard/random` | 1 |
| 0.9375 | `pattern/states/accumulate/count` | 6-14 |
| 0.75 | `test/equality` | 13, 15 |
| 0.75 | `test/inequality` | 6, 9, 11 |
| 0.875 | `type/number/integer` | 7 |
| 0.9375 | `type/number/integer/literal` | 4, 4, 6, 8 |
| 0.96875 | `type/number/integer/literal/zero` | 2 |
| 0.875 | `type/sequence/string` | 5, 16, 18 |
| 0.9375 | `type/sequence/string/literal` | 3, 5, 7, 10, 12, 16, 18 |
| 0.9375 | `variable/assignment/augmented/Add` | 8 |
| 0.875 | `variable/assignment/single` | 2, 3, 4, 7 |
| 0 | `metadata/program` | 1-18 |
| 0 | `metadata/sloc/18` | 1-18 |
---

### Program `16_csv.py` (learning cost 27.5)

```python
1   import csv
2   def cmp(a, b):
3       return (a > b) - (a < b)
4   with open("stocks.csv", "w", newline="") as stocksFileW:
5       writer = csv.writer(stocksFileW)
6       writer.writerows(
7           [
8               ["GOOG", "Google, Inc.", 505.24, 0.47, 0.09],
9               ["YHOO", "Yahoo! Inc.", 27.38, 0.33, 1.22],
10              ["CNET", "CNET Networks, Inc.", 8.62, -0.13, -1.4901],
11          ]
12      )
13  with open("stocks.csv", "r") as stocksFile:
14      stocks = csv.reader(stocksFile)
15      status_labels = {-1: "down", 0: "unchanged", 1: "up"}
16      for ticker, name, price, change, pct in stocks:
17          status = status_labels[cmp(float(change), 0.0)]
18          print("%s is %s (%.2f)" % (name, status, float(pct)))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 17, 18 |
| 0.75 | `call/function` | 17 |
| 0.96875 | `call/function/builtin/casting/float` | 17, 18 |
| 0.9375 | `call/function/builtin/open` | 4, 13 |
| 0.9375 | `call/function/builtin/print` | 18 |
| 0.875 | `call/method/reader` | 14 |
| 0.875 | `call/method/writer` | 5 |
| 0.875 | `call/method/writerows` | 6 |
| 0.9375 | `flow/loop/exit/late` | 16-18 |
| 0.875 | `flow/loop/for` | 16-18 |
| 0.9375 | `flow/loop/for/elements` | 16-18 |
| 0.875 | `io/file/open` | 4, 13 |
| 0.875 | `io/standard/print` | 18 |
| 0.875 | `library/standard/csv` | 1 |
| 0.875 | `operator/arithmetic/substraction` | 3 |
| 0.875 | `operator/string/format` | 18 |
| 0.875 | `subroutine/argument/arg` | 2, 2 |
| 0.75 | `subroutine/function` | 2-3 |
| 0.75 | `subscript/index` | 17 |
| 0.75 | `test/inequality` | 3, 3 |
| 0.9375 | `type/non_sequence/dictionary/literal` | 15 |
| 0.875 | `type/number/floating_point` | 17, 18 |
| 0.9375 | `type/number/floating_point/literal` | 8, 8, 8, 9, 9, 9, 10, 10, 10 |
| 0.96875 | `type/number/floating_point/literal/zero` | 17 |
| 0.9375 | `type/number/integer/literal` | 15, 15 |
| 0.96875 | `type/number/integer/literal/zero` | 15 |
| 0.9375 | `type/sequence/list/literal` | 7, 8, 9, 10 |
| 0.9375 | `type/sequence/string/literal` | <details><summary>4, 4, 8, 8, 9, 9, 10, 10,</summary>13, 13, 15, 15, 15, 18</details> |
| 0.96875 | `type/sequence/string/literal/empty` | 4 |
| 0.9375 | `type/sequence/tuple/literal` | 16, 18 |
| 0.875 | `variable/assignment/single` | 5, 14, 15, 17 |
| 0 | `metadata/program` | 1-18 |
| 0 | `metadata/sloc/18` | 1-18 |
---

### Program `18_queens.py` (learning cost 27.53125)

```python
1   BOARD_SIZE = 8
2   def under_attack(col, queens):
3       left = right = col
4       for r, c in reversed(queens):
5           left, right = left - 1, right + 1
6           if c in (left, col, right):
7               return True
8       return False
9   def solve(n):
10      if n == 0:
11          return [[]]
12      smaller_solutions = solve(n - 1)
13      return [
14          solution + [(n, i + 1)]
15          for i in range(BOARD_SIZE)
16          for solution in smaller_solutions
17          if not under_attack(i + 1, solution)
18      ]
19  for answer in solve(BOARD_SIZE):
20      print(answer)
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/function` | 12, 17, 19 |
| 0.9375 | `call/function/builtin/print` | 20 |
| 0.9375 | `call/function/builtin/range` | 15 |
| 0.9375 | `call/function/builtin/reversed` | 4 |
| 0.875 | `flow/conditional/guard` | 10-11 |
| 0.875 | `flow/conditional/no_else` | 6-7, 10-11 |
| 0.96875 | `flow/loop/exit/early/return` | 4-7 |
| 0.9375 | `flow/loop/exit/late` | 19-20 |
| 0.875 | `flow/loop/for` | 4-7, 19-20 |
| 0.875 | `io/standard/print` | 20 |
| 0.875 | `operator/arithmetic/addition` | 5, 17 |
| 0.875 | `operator/arithmetic/substraction` | 5, 12 |
| 0.875 | `operator/boolean/not` | 17 |
| 0.875 | `operator/list/concatenation` | 14 |
| 0.9375 | `pattern/elements/satisfy/some` | 4-7 |
| 0.875 | `subroutine/argument/arg` | 2, 2, 9 |
| 0.75 | `subroutine/function` | 2-8, 9-17 |
| 0.875 | `subroutine/recursive/body` | 9-17 |
| 0.75 | `test/belonging` | 6 |
| 0.75 | `test/equality` | 10 |
| 0.9375 | `type/boolean/literal/false` | 8 |
| 0.9375 | `type/boolean/literal/true` | 7 |
| 0.9375 | `type/number/integer/literal` | 1, 5, 5, 12, 14, 17 |
| 0.96875 | `type/number/integer/literal/zero` | 10 |
| 0.9375 | `type/sequence/list/literal` | 11, 14 |
| 0.96875 | `type/sequence/list/literal/empty` | 11 |
| 0.9375 | `type/sequence/tuple/literal` | 4, 5, 5, 6, 14 |
| 0.875 | `variable/assignment/chained` | 3 |
| 0.875 | `variable/assignment/constant` | 1 |
| 0.875 | `variable/assignment/parallel` | 5 |
| 0.875 | `variable/assignment/single` | 1, 12 |
| 0 | `metadata/program` | 1-20 |
| 0 | `metadata/sloc/20` | 1-20 |
---

## 1 program of learning cost in [32, 64[

### Program `28_queens.py` (learning cost 36.21875)

```python
1   BOARD_SIZE = 8
2   class BailOut(Exception):
3       pass
4   def validate(queens):
5       left = right = col = queens[-1]
6       for r in reversed(queens[:-1]):
7           left, right = left-1, right+1
8           if r in (left, col, right):
9               raise BailOut
10  def add_queen(queens):
11      for i in range(BOARD_SIZE):
12          test_queens = queens + [i]
13          try:
14              validate(test_queens)
15              if len(test_queens) == BOARD_SIZE:
16                  return test_queens
17              else:
18                  return add_queen(test_queens)
19          except BailOut:
20              pass
21      raise BailOut
22  queens = add_queen([])
23  print (queens)
24  print ("\n".join(". "*q + "Q " + ". "*(BOARD_SIZE-q-1) for q in queens))
```

| Cost  | Taxon | Location |
|----|----|----|
| 0.75 | `call/composition` | 24 |
| 0.75 | `call/function` | 14, 18, 22 |
| 0.9375 | `call/function/builtin/len` | 15 |
| 0.9375 | `call/function/builtin/print` | 23, 24 |
| 0.9375 | `call/function/builtin/range` | 11 |
| 0.9375 | `call/function/builtin/reversed` | 6 |
| 0.875 | `call/method/join` | 24 |
| 0.5 | `class` | 2-3 |
| 0.75 | `flow/conditional` | 15-18 |
| 0.875 | `flow/conditional/else` | 18 |
| 0.875 | `flow/conditional/no_else` | 8-9 |
| 0.9375 | `flow/exception/catch/` | 13-20 |
| 0.96875 | `flow/loop/exit/early/raise` | 6-9 |
| 0.96875 | `flow/loop/exit/early/return` | 11-20 |
| 0.875 | `flow/loop/for` | 6-9 |
| 0.9375 | `flow/loop/for/arithmetic` | 11-20 |
| 0.75 | `flow/null_operation` | 3, 20 |
| 0.875 | `io/standard/print` | 23, 24 |
| 0.875 | `operator/arithmetic/addition` | 7 |
| 0.875 | `operator/arithmetic/substraction` | 7, 24, 24 |
| 0.875 | `operator/list/concatenation` | 12 |
| 0.875 | `operator/string/concatenation` | 24 |
| 0.875 | `operator/string/replication` | 24, 24 |
| 0.875 | `subroutine/argument/arg` | 4, 10 |
| 0.75 | `subroutine/function` | 10-21 |
| 0.75 | `subroutine/procedure` | 4-9 |
| 0.875 | `subroutine/recursive/tail` | 10-21 |
| 0.75 | `subscript/index` | 5 |
| 0.9375 | `subscript/index/backwards/last` | 5 |
| 0.875 | `subscript/slice/stop` | 6 |
| 0.75 | `test/belonging` | 8 |
| 0.75 | `test/equality` | 15 |
| 0.9375 | `type/number/integer/literal` | 1, 5, 6, 7, 7, 24 |
| 0.9375 | `type/sequence/list/literal` | 12 |
| 0.96875 | `type/sequence/list/literal/empty` | 22 |
| 0.875 | `type/sequence/string` | 24 |
| 0.9375 | `type/sequence/string/literal` | 24, 24, 24, 24 |
| 0.9375 | `type/sequence/tuple/literal` | 7, 7, 8 |
| 0.875 | `variable/assignment/chained` | 5 |
| 0.875 | `variable/assignment/constant` | 1 |
| 0.875 | `variable/assignment/parallel` | 7 |
| 0.875 | `variable/assignment/single` | 1, 12, 22 |
| 0 | `metadata/program` | 1-24 |
| 0 | `metadata/sloc/24` | 1-24 |
---

# Summary
<details>
  <summary>20 initially.</summary>
  <ol>
    <li><code>01_hello_world.py</code></li>
    <li><code>02_input_ name.py</code></li>
    <li><code>03_friends.py</code></li>
    <li><code>04_fibonacci.py</code></li>
    <li><code>05_greet.py</code></li>
    <li><code>06_regex.py</code></li>
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
