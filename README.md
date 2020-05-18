[![Build Status](https://travis-ci.com/laowantong/paroxython.svg?branch=master)](https://travis-ci.com/laowantong/paroxython)
[![codecov](https://img.shields.io/codecov/c/github/laowantong/paroxython/master)](https://codecov.io/gh/laowantong/paroxython)
[![Checked with mypy](https://img.shields.io/badge/typing-mypy-brightgreen)](http://mypy-lang.org/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/73432ed4c5294326ba6279bbbb0fe2e6)](https://www.codacy.com/manual/laowantong/paroxython)
[![Updates](https://pyup.io/repos/github/laowantong/paroxython/shield.svg)](https://pyup.io/repos/github/laowantong/paroxython/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/paroxython)
[![GitHub Release](https://img.shields.io/github/release/laowantong/paroxython.svg?style=flat)]()
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/laowantong/paroxython)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/laowantong/paroxython.svg?style=flat)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![](docs/logo.png)

Paroxython is a command-line tool which finds and tags algorithmic features (such as assignments, nested loops, tail-recursive functions, etc.) in a collection of small Python programs, typically gathered for educational purposes (e.g., examples, patterns, exercise corrections).

Each tag consists in a free-form label associated with its spanning lines. These labels are then mapped onto a knowledge taxonomy designed by the teacher with basic order constraints in mind (e.g., the fact that the introduction of the concept of early exit must come after that of loop, which itself requires that of control flow, is expressed with the following taxon: flow/loop/exit/early).

Source-codes, labels and taxons are stored in a database, which can finally be filtered through a pipeline of inclusion, exclusion and impartment commands on programs or taxons.

# Installation

```
pip install paroxython
```

# Test-drive

## Terminal
```
paroxython --help
```

## Jupyter notebook

Load the magic command:

```python
%load_ext paroxython
```

Run it on a cell of Python code (line numbers added for clarity):

```python
1	%%paroxython
2	def fibonacci(n):
3	    result = []
4	    (a, b) = (0, 1)
5	    while a < n:
6	        result.append(a)
7	        (a, b) = (b, a + b)
8	    return result
```


| Taxon | Lines |
|:--|--:|
| `call/method/append` | 6 |
| `flow/loop/exit/late` | 5-7 |
| `flow/loop/while` | 5-7 |
| `metadata/sloc/8` | 2-8 |
| `operator/arithmetic/addition` | 7 |
| `subroutine/argument/arg` | 2 |
| `subroutine/function` | 2-8 |
| `test/inequality` | 5 |
| `type/number/integer/literal` | 4 |
| `type/number/integer/literal/zero` | 4 |
| `type/sequence/list` | 6 |
| `type/sequence/list/literal/empty` | 3 |
| `type/sequence/tuple/literal` | 4, 4, 7, 7 |
| `variable/assignment/parallel` | 4 |
| `variable/assignment/parallel/slide` | 7 |
| `variable/assignment/single` | 3 |

# Documentation

Coming soon.
