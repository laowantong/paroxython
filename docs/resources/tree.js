// This file is auto-generated. Any changes here will be lost.
google.charts.load('current', {packages:['wordtree']});
google.charts.setOnLoadCallback(draw_tree);
google.charts.setOnLoadCallback(draw_full_tree);
function draw_tree() {
var data = google.visualization.arrayToDataTable([['node', 'occurrences'],
['🐍 call class construct.', 267],
['🐍 call composition.', 1036],
['🐍 call exception builtin AssertionError.', 1],
['🐍 call exception builtin AttributeError.', 4],
['🐍 call exception builtin Exception.', 16],
['🐍 call exception builtin IndexError.', 7],
['🐍 call exception builtin KeyError.', 1],
['🐍 call exception builtin TypeError.', 23],
['🐍 call exception builtin ValueError.', 57],
['🐍 call subroutine.', 941],
['🐍 call subroutine builtin abs.', 20],
['🐍 call subroutine builtin all.', 5],
['🐍 call subroutine builtin any.', 2],
['🐍 call subroutine builtin bin.', 2],
['🐍 call subroutine builtin casting bool.', 4],
['🐍 call subroutine builtin casting bytes.', 6],
['🐍 call subroutine builtin casting complex.', 1],
['🐍 call subroutine builtin casting dict.', 6],
['🐍 call subroutine builtin casting float.', 48],
['🐍 call subroutine builtin casting int.', 198],
['🐍 call subroutine builtin casting list.', 84],
['🐍 call subroutine builtin casting set.', 26],
['🐍 call subroutine builtin casting str.', 116],
['🐍 call subroutine builtin casting tuple.', 7],
['🐍 call subroutine builtin chr.', 18],
['🐍 call subroutine builtin divmod.', 13],
['🐍 call subroutine builtin enumerate.', 31],
['🐍 call subroutine builtin eval.', 3],
['🐍 call subroutine builtin filter.', 2],
['🐍 call subroutine builtin format.', 5],
['🐍 call subroutine builtin hasattr.', 2],
['🐍 call subroutine builtin hash.', 1],
['🐍 call subroutine builtin input.', 60],
['🐍 call subroutine builtin isinstance.', 111],
['🐍 call subroutine builtin iter.', 1],
['🐍 call subroutine builtin len.', 609],
['🐍 call subroutine builtin map.', 21],
['🐍 call subroutine builtin max.', 48],
['🐍 call subroutine builtin min.', 33],
['🐍 call subroutine builtin next.', 3],
['🐍 call subroutine builtin object.', 2],
['🐍 call subroutine builtin open.', 40],
['🐍 call subroutine builtin ord.', 28],
['🐍 call subroutine builtin pow.', 8],
['🐍 call subroutine builtin print.', 441],
['🐍 call subroutine builtin print attrs.', 1],
['🐍 call subroutine builtin print end.', 53],
['🐍 call subroutine builtin print n.', 1],
['🐍 call subroutine builtin print r.', 1],
['🐍 call subroutine builtin print sep.', 9],
['🐍 call subroutine builtin range.', 681],
['🐍 call subroutine builtin reversed.', 4],
['🐍 call subroutine builtin round.', 14],
['🐍 call subroutine builtin sorted.', 27],
['🐍 call subroutine builtin sum.', 33],
['🐍 call subroutine builtin super.', 6],
['🐍 call subroutine builtin type.', 15],
['🐍 call subroutine builtin zip.', 7],
['🐍 call subroutine method.', 1469],
['🐍 call subroutine method base64 a85decode.', 1],
['🐍 call subroutine method base64 b16decode.', 1],
['🐍 call subroutine method base64 b32decode.', 1],
['🐍 call subroutine method base64 decode.', 3],
['🐍 call subroutine method chaining.', 74],
['🐍 call subroutine method code append.', 1],
['🐍 call subroutine method doctest testmod.', 1],
['🐍 call subroutine method hashlib assertEqual.', 1],
['🐍 call subroutine method hashlib final_hash.', 1],
['🐍 call subroutine method hashlib hexdigest.', 1],
['🐍 call subroutine method hashlib sha1.', 1],
['🐍 call subroutine method heapq heappush.', 4],
['🐍 call subroutine method math floor.', 1],
['🐍 call subroutine method math sqrt.', 1],
['🐍 call subroutine method mutable_duck clear.', 1],
['🐍 call subroutine method mutable_duck copy.', 6],
['🐍 call subroutine method mutable_duck pop.', 58],
['🐍 call subroutine method mutable_duck remove.', 21],
['🐍 call subroutine method mutable_duck update.', 5],
['🐍 call subroutine method non_sequence dictionary get.', 39],
['🐍 call subroutine method non_sequence dictionary items.', 8],
['🐍 call subroutine method non_sequence dictionary keys.', 24],
['🐍 call subroutine method non_sequence dictionary values.', 2],
['🐍 call subroutine method non_sequence set add.', 28],
['🐍 call subroutine method non_sequence set intersection.', 1],
['🐍 call subroutine method non_sequence set isdisjoint.', 1],
['🐍 call subroutine method non_sequence set union.', 1],
['🐍 call subroutine method os stat.', 1],
['🐍 call subroutine method parser add_argument.', 4],
['🐍 call subroutine method pickle dump.', 1],
['🐍 call subroutine method queue Queue.', 3],
['🐍 call subroutine method queue append.', 13],
['🐍 call subroutine method random seed.', 2],
['🐍 call subroutine method random shuffle.', 3],
['🐍 call subroutine method sequence list append.', 342],
['🐍 call subroutine method sequence list extend.', 11],
['🐍 call subroutine method sequence list insert.', 74],
['🐍 call subroutine method sequence list reverse.', 5],
['🐍 call subroutine method sequence list sort.', 15],
['🐍 call subroutine method sequence string center.', 7],
['🐍 call subroutine method sequence string encode.', 4],
['🐍 call subroutine method sequence string find.', 17],
['🐍 call subroutine method sequence string format.', 40],
['🐍 call subroutine method sequence string isalpha.', 3],
['🐍 call subroutine method sequence string isdigit.', 2],
['🐍 call subroutine method sequence string islower.', 4],
['🐍 call subroutine method sequence string isupper.', 4],
['🐍 call subroutine method sequence string join.', 79],
['🐍 call subroutine method sequence string ljust.', 8],
['🐍 call subroutine method sequence string lower.', 27],
['🐍 call subroutine method sequence string lstrip.', 1],
['🐍 call subroutine method sequence string replace.', 9],
['🐍 call subroutine method sequence string rjust.', 4],
['🐍 call subroutine method sequence string rstrip.', 2],
['🐍 call subroutine method sequence string split.', 49],
['🐍 call subroutine method sequence string splitlines.', 1],
['🐍 call subroutine method sequence string startswith.', 14],
['🐍 call subroutine method sequence string strip.', 13],
['🐍 call subroutine method sequence string title.', 17],
['🐍 call subroutine method sequence string upper.', 23],
['🐍 call subroutine method sequence string zfill.', 1],
['🐍 call subroutine method sequence_duck count.', 31],
['🐍 call subroutine method sequence_duck index.', 23],
['🐍 call subroutine method sys exit.', 12],
['🐍 call subroutine method webbrowser get.', 1],
['🐍 call subroutine method webbrowser open.', 1],
['🐍 call subroutine no_arguments.', 115],
['🐍 condition belonging.', 64],
['🐍 condition belonging not.', 44],
['🐍 condition divisibility.', 42],
['🐍 condition divisibility parity.', 42],
['🐍 condition equality.', 667],
['🐍 condition equality chained 2.', 4],
['🐍 condition equality chained 3.', 1],
['🐍 condition equality chained 5.', 1],
['🐍 condition equality not.', 200],
['🐍 condition identity.', 100],
['🐍 condition identity not.', 54],
['🐍 condition inequality.', 770],
['🐍 condition inequality chained 2.', 18],
['🐍 def class.', 104],
['🐍 def subroutine decorated.', 34],
['🐍 def subroutine function.', 303],
['🐍 def subroutine function anonymous.', 24],
['🐍 def subroutine function impure.', 524],
['🐍 def subroutine function predicate.', 26],
['🐍 def subroutine function pure.', 132],
['🐍 def subroutine generator.', 15],
['🐍 def subroutine higher_order.', 11],
['🐍 def subroutine method flavor class.', 2],
['🐍 def subroutine method flavor instance.', 566],
['🐍 def subroutine method flavor static.', 5],
['🐍 def subroutine method naming internal_use.', 34],
['🐍 def subroutine method naming internal_use mangling.', 13],
['🐍 def subroutine method naming magic __add__.', 4],
['🐍 def subroutine method naming magic __bool__.', 2],
['🐍 def subroutine method naming magic __call__.', 1],
['🐍 def subroutine method naming magic __contains__.', 1],
['🐍 def subroutine method naming magic __eq__.', 3],
['🐍 def subroutine method naming magic __ge__.', 1],
['🐍 def subroutine method naming magic __getitem__.', 3],
['🐍 def subroutine method naming magic __gt__.', 1],
['🐍 def subroutine method naming magic __hash__.', 1],
['🐍 def subroutine method naming magic __init__.', 92],
['🐍 def subroutine method naming magic __le__.', 1],
['🐍 def subroutine method naming magic __len__.', 2],
['🐍 def subroutine method naming magic __lt__.', 3],
['🐍 def subroutine method naming magic __mul__.', 5],
['🐍 def subroutine method naming magic __ne__.', 2],
['🐍 def subroutine method naming magic __neg__.', 2],
['🐍 def subroutine method naming magic __pow__.', 1],
['🐍 def subroutine method naming magic __prepare__.', 1],
['🐍 def subroutine method naming magic __repr__.', 14],
['🐍 def subroutine method naming magic __setitem__.', 2],
['🐍 def subroutine method naming magic __str__.', 13],
['🐍 def subroutine method naming magic __sub__.', 4],
['🐍 def subroutine nested.', 14],
['🐍 def subroutine nested closure.', 2],
['🐍 def subroutine no_parameter.', 143],
['🐍 def subroutine procedure.', 419],
['🐍 def subroutine procedure test.', 48],
['🐍 def subroutine recursive body.', 91],
['🐍 def subroutine recursive call_count 1.', 49],
['🐍 def subroutine recursive call_count 2.', 45],
['🐍 def subroutine recursive call_count 3.', 8],
['🐍 def subroutine recursive call_count 4.', 2],
['🐍 def subroutine recursive tail.', 13],
['🐍 def subroutine return nothing.', 92],
['🐍 def subroutine return something.', 649],
['🐍 flow assertion.', 159],
['🐍 flow conditional.', 464],
['🐍 flow conditional else.', 329],
['🐍 flow conditional else if.', 168],
['🐍 flow conditional guard.', 191],
['🐍 flow conditional nested 1.', 221],
['🐍 flow conditional nested 2.', 32],
['🐍 flow conditional nested 3.', 9],
['🐍 flow conditional nested 4.', 2],
['🐍 flow conditional no_else.', 914],
['🐍 flow exception catch .', 4],
['🐍 flow exception catch Exception.', 1],
['🐍 flow exception catch IndexError.', 2],
['🐍 flow exception catch StopIteration.', 1],
['🐍 flow exception catch TypeError.', 9],
['🐍 flow exception catch UnboundLocalError.', 1],
['🐍 flow exception catch ValueError.', 9],
['🐍 flow exception raise .', 3],
['🐍 flow exception raise TypeError.', 8],
['🐍 flow exception raise ValueError.', 1],
['🐍 flow loop continue.', 23],
['🐍 flow loop exit early break.', 62],
['🐍 flow loop exit early break else.', 3],
['🐍 flow loop exit early raise.', 10],
['🐍 flow loop exit early return.', 99],
['🐍 flow loop exit late.', 923],
['🐍 flow loop for.', 90],
['🐍 flow loop for arithmetic.', 267],
['🐍 flow loop for arithmetic start.', 182],
['🐍 flow loop for arithmetic start step.', 36],
['🐍 flow loop for arithmetic start step backwards.', 30],
['🐍 flow loop for elements.', 145],
['🐍 flow loop for indexes.', 107],
['🐍 flow loop for indexes_and_elements.', 25],
['🐍 flow loop for nested 1.', 157],
['🐍 flow loop for nested 2.', 17],
['🐍 flow loop for nested 3.', 1],
['🐍 flow loop for nested square.', 29],
['🐍 flow loop for nested triangular.', 5],
['🐍 flow loop for throwaway.', 11],
['🐍 flow loop while.', 259],
['🐍 flow loop while infinite.', 44],
['🐍 flow no_operation.', 18],
['🐍 import personal.', 11],
['🐍 import standard __future__ absolute_import.', 1],
['🐍 import standard __future__ division.', 2],
['🐍 import standard __future__ print_function.', 1],
['🐍 import standard abc abstractmethod.', 1],
['🐍 import standard argparse.', 4],
['🐍 import standard base64.', 3],
['🐍 import standard bisect.', 1],
['🐍 import standard bisect bisect.', 1],
['🐍 import standard collections.', 3],
['🐍 import standard collections Counter.', 1],
['🐍 import standard collections defaultdict.', 3],
['🐍 import standard collections deque.', 5],
['🐍 import standard copy.', 1],
['🐍 import standard datetime.', 1],
['🐍 import standard decimal Decimal.', 3],
['🐍 import standard decimal getcontext.', 2],
['🐍 import standard doctest.', 2],
['🐍 import standard doctest testmod.', 3],
['🐍 import standard functools.', 1],
['🐍 import standard functools reduce.', 1],
['🐍 import standard gzip.', 1],
['🐍 import standard hashlib.', 1],
['🐍 import standard heapq.', 2],
['🐍 import standard itertools.', 3],
['🐍 import standard itertools accumulate.', 1],
['🐍 import standard itertools permutations.', 1],
['🐍 import standard itertools takewhile.', 1],
['🐍 import standard logging.', 1],
['🐍 import standard math.', 33],
['🐍 import standard math ceil.', 1],
['🐍 import standard math exp.', 1],
['🐍 import standard math factorial.', 4],
['🐍 import standard math log10.', 1],
['🐍 import standard math pi.', 1],
['🐍 import standard math sqrt.', 6],
['🐍 import standard multiprocessing Lock.', 1],
['🐍 import standard multiprocessing Pipe.', 1],
['🐍 import standard multiprocessing Process.', 1],
['🐍 import standard numbers Number.', 1],
['🐍 import standard operator.', 1],
['🐍 import standard os.', 20],
['🐍 import standard pickle.', 1],
['🐍 import standard pprint.', 1],
['🐍 import standard pprint pformat.', 2],
['🐍 import standard queue.', 2],
['🐍 import standard random.', 18],
['🐍 import standard random choice.', 1],
['🐍 import standard random randint.', 1],
['🐍 import standard random random.', 1],
['🐍 import standard random shuffle.', 2],
['🐍 import standard statistics.', 1],
['🐍 import standard string.', 3],
['🐍 import standard string ascii_letters.', 1],
['🐍 import standard string digits.', 1],
['🐍 import standard string punctuation.', 1],
['🐍 import standard struct.', 1],
['🐍 import standard sys.', 23],
['🐍 import standard sys maxsize.', 1],
['🐍 import standard tempfile TemporaryFile.', 1],
['🐍 import standard time.', 5],
['🐍 import standard time time.', 1],
['🐍 import standard timeit.', 1],
['🐍 import standard turtle.', 1],
['🐍 import standard typing Any.', 2],
['🐍 import standard typing Callable.', 1],
['🐍 import standard typing Dict.', 1],
['🐍 import standard typing Iterator.', 1],
['🐍 import standard typing List.', 13],
['🐍 import standard typing Optional.', 2],
['🐍 import standard typing Sequence.', 1],
['🐍 import standard typing Tuple.', 3],
['🐍 import standard typing TypeVar.', 1],
['🐍 import standard unittest.', 4],
['🐍 import standard urllib.request.', 1],
['🐍 import standard webbrowser.', 1],
['🐍 import third_party PIL Image.', 2],
['🐍 import third_party abs abs_val.', 1],
['🐍 import third_party bs4 BeautifulSoup.', 2],
['🐍 import third_party build_directory_md good_filepaths.', 1],
['🐍 import third_party cryptomath_module.', 3],
['🐍 import third_party cv2.', 3],
['🐍 import third_party cv2 COLOR_BGR2GRAY.', 5],
['🐍 import third_party cv2 cvtColor.', 5],
['🐍 import third_party cv2 imread.', 5],
['🐍 import third_party cv2 imshow.', 4],
['🐍 import third_party cv2 waitKey.', 4],
['🐍 import third_party fake_useragent UserAgent.', 1],
['🐍 import third_party hash_table HashTable.', 3],
['🐍 import third_party input_data.', 1],
['🐍 import third_party lib Matrix.', 1],
['🐍 import third_party lib Vector.', 1],
['🐍 import third_party lib axpy.', 1],
['🐍 import third_party lib squareZeroMatrix.', 1],
['🐍 import third_party lib unitBasisVector.', 1],
['🐍 import third_party lib zeroVector.', 1],
['🐍 import third_party matplotlib.colors ListedColormap.', 1],
['🐍 import third_party matplotlib.gridspec.', 1],
['🐍 import third_party matplotlib.pyplot.', 7],
['🐍 import third_party matplotlib pyplot.', 3],
['🐍 import third_party matrix matrix_operation.', 1],
['🐍 import third_party mpmath.', 1],
['🐍 import third_party number_theory.prime_numbers check_prime.', 1],
['🐍 import third_party number_theory.prime_numbers next_prime.', 2],
['🐍 import third_party numpy.', 29],
['🐍 import third_party numpy array.', 4],
['🐍 import third_party numpy cos.', 1],
['🐍 import third_party numpy cross.', 1],
['🐍 import third_party numpy divide.', 1],
['🐍 import third_party numpy dot.', 2],
['🐍 import third_party numpy exp.', 2],
['🐍 import third_party numpy int8.', 1],
['🐍 import third_party numpy mgrid.', 1],
['🐍 import third_party numpy multiply.', 1],
['🐍 import third_party numpy pad.', 1],
['🐍 import third_party numpy pi.', 2],
['🐍 import third_party numpy radians.', 1],
['🐍 import third_party numpy ravel.', 3],
['🐍 import third_party numpy sin.', 1],
['🐍 import third_party numpy sort.', 1],
['🐍 import third_party numpy sqrt.', 1],
['🐍 import third_party numpy square.', 1],
['🐍 import third_party numpy uint8.', 3],
['🐍 import third_party numpy zeros.', 2],
['🐍 import third_party numpy zeros_like.', 1],
['🐍 import third_party pandas.', 2],
['🐍 import third_party prime_check Test.', 1],
['🐍 import third_party pytest.', 1],
['🐍 import third_party rabin_miller.', 2],
['🐍 import third_party requests.', 6],
['🐍 import third_party rsa_key_generator.', 1],
['🐍 import third_party six.moves urllib.', 1],
['🐍 import third_party six.moves xrange.', 1],
['🐍 import third_party skfuzzy.', 1],
['🐍 import third_party sklearn.datasets.', 1],
['🐍 import third_party sklearn.datasets load_iris.', 2],
['🐍 import third_party sklearn.datasets make_blobs.', 1],
['🐍 import third_party sklearn.datasets make_circles.', 1],
['🐍 import third_party sklearn.linear_model LinearRegression.', 1],
['🐍 import third_party sklearn.metrics pairwise_distances.', 1],
['🐍 import third_party sklearn.model_selection train_test_split.', 4],
['🐍 import third_party sklearn.neighbors KNeighborsClassifier.', 1],
['🐍 import third_party sklearn.preprocessing PolynomialFeatures.', 1],
['🐍 import third_party sklearn.preprocessing StandardScaler.', 1],
['🐍 import third_party sklearn.utils shuffle.', 1],
['🐍 import third_party sklearn datasets.', 2],
['🐍 import third_party sklearn svm.', 1],
['🐍 import third_party stack Stack.', 2],
['🐍 import third_party sympy diff.', 1],
['🐍 import third_party tensorflow.', 1],
['🐍 import third_party tensorflow.python.framework dtypes.', 1],
['🐍 import third_party tensorflow.python.framework random_seed.', 1],
['🐍 import third_party tensorflow.python.platform gfile.', 1],
['🐍 import third_party tensorflow.python.util.deprecation deprecated.', 1],
['🐍 import third_party transposition_cipher.', 1],
['🐍 meta ast EmptyProgramError.', 4],
['🐍 meta ast SyntaxError.', 2],
['🐍 meta program.', 417],
['🐍 operator arithmetic addition.', 1008],
['🐍 operator arithmetic division.', 253],
['🐍 operator arithmetic integer_division.', 86],
['🐍 operator arithmetic minus.', 31],
['🐍 operator arithmetic modulo.', 223],
['🐍 operator arithmetic multiplication.', 717],
['🐍 operator arithmetic power.', 109],
['🐍 operator arithmetic substraction.', 879],
['🐍 operator bitwise and.', 31],
['🐍 operator bitwise complement.', 1],
['🐍 operator bitwise or.', 6],
['🐍 operator bitwise shift left.', 13],
['🐍 operator bitwise shift right.', 13],
['🐍 operator bitwise xor.', 19],
['🐍 operator boolean and.', 231],
['🐍 operator boolean not.', 174],
['🐍 operator boolean or.', 107],
['🐍 operator list concatenation.', 15],
['🐍 operator list replication.', 66],
['🐍 operator matrix multiplication.', 3],
['🐍 operator string concatenation.', 107],
['🐍 operator string format.', 70],
['🐍 operator string replication.', 11],
['🐍 operator ternary.', 61],
['🐍 pattern elements accumulate all.', 147],
['🐍 pattern elements accumulate count.', 14],
['🐍 pattern elements accumulate count some.', 23],
['🐍 pattern elements accumulate find best.', 13],
['🐍 pattern elements accumulate find best index.', 1],
['🐍 pattern elements accumulate find best max.', 8],
['🐍 pattern elements accumulate find best min.', 2],
['🐍 pattern elements accumulate into_list.', 55],
['🐍 pattern elements accumulate into_list extension.', 2],
['🐍 pattern elements accumulate into_set.', 4],
['🐍 pattern elements accumulate product.', 12],
['🐍 pattern elements accumulate some.', 76],
['🐍 pattern elements accumulate substraction.', 3],
['🐍 pattern elements accumulate summation.', 115],
['🐍 pattern elements find first_good.', 1],
['🐍 pattern elements find first_good index.', 1],
['🐍 pattern elements satisfy all.', 25],
['🐍 pattern elements satisfy some.', 3],
['🐍 pattern expression mid_value.', 12],
['🐍 pattern inputs find first_good.', 4],
['🐍 pattern states accumulate count.', 66],
['🐍 pattern states accumulate count some.', 17],
['🐍 style functional.', 21],
['🐍 style functional_trait accumulate.', 1],
['🐍 style functional_trait filter.', 2],
['🐍 style functional_trait higher_order.', 11],
['🐍 style functional_trait map.', 21],
['🐍 style functional_trait pure_function.', 132],
['🐍 style functional_trait reduce.', 1],
['🐍 style imperative.', 2],
['🐍 style imperative flat.', 4],
['🐍 style naive mid_value.', 12],
['🐍 style naive return_condition.', 5],
['🐍 style object_oriented.', 75],
['🐍 style one_liner.', 12],
['🐍 style procedural.', 315],
['🐍 style unpythonic augmented_assignment.', 85],
['🐍 style unpythonic chained_comparison.', 1],
['🐍 style unpythonic find_best_element_index.', 1],
['🐍 style unpythonic swap.', 13],
['🐍 style unpythonic yoda_comparison.', 6],
['🐍 subscript index.', 2364],
['🐍 subscript index arithmetic.', 299],
['🐍 subscript index backwards last.', 25],
['🐍 subscript index shape 2.', 392],
['🐍 subscript index shape 3.', 14],
['🐍 subscript slice copy.', 14],
['🐍 subscript slice start.', 94],
['🐍 subscript slice step backwards.', 15],
['🐍 subscript slice stop.', 90],
['🐍 type boolean.', 4],
['🐍 type boolean literal False.', 193],
['🐍 type boolean literal True.', 241],
['🐍 type non_sequence dictionary.', 79],
['🐍 type non_sequence dictionary literal.', 57],
['🐍 type non_sequence dictionary literal empty.', 26],
['🐍 type non_sequence set.', 57],
['🐍 type non_sequence set literal.', 6],
['🐍 type null literal.', 362],
['🐍 type number complex.', 1],
['🐍 type number complex literal.', 1],
['🐍 type number floating_point.', 48],
['🐍 type number floating_point literal.', 292],
['🐍 type number floating_point literal zero.', 22],
['🐍 type number integer.', 198],
['🐍 type number integer literal.', 5119],
['🐍 type number integer literal zero.', 1750],
['🐍 type number magic.', 2311],
['🐍 type sequence.', 54],
['🐍 type sequence list.', 531],
['🐍 type sequence list literal.', 629],
['🐍 type sequence list literal empty.', 285],
['🐍 type sequence string.', 445],
['🐍 type sequence string literal.', 1808],
['🐍 type sequence string literal empty.', 128],
['🐍 type sequence string literal formatted.', 62],
['🐍 type sequence string literal special \\D.', 1],
['🐍 type sequence string literal special \\n.', 103],
['🐍 type sequence string literal special \\r.', 9],
['🐍 type sequence string literal special \\t.', 14],
['🐍 type sequence string literal special cjk_unified_ideographs.', 1],
['🐍 type sequence string literal special emojis.', 2],
['🐍 type sequence tuple.', 7],
['🐍 type sequence tuple literal.', 891],
['🐍 var assignment explicit.', 566],
['🐍 var assignment explicit augmented Add.', 405],
['🐍 var assignment explicit augmented BitXor.', 6],
['🐍 var assignment explicit augmented Div.', 3],
['🐍 var assignment explicit augmented FloorDiv.', 6],
['🐍 var assignment explicit augmented Mod.', 2],
['🐍 var assignment explicit augmented Mult.', 26],
['🐍 var assignment explicit augmented Pow.', 1],
['🐍 var assignment explicit augmented RShift.', 6],
['🐍 var assignment explicit augmented Sub.', 50],
['🐍 var assignment explicit augmented subscript Add.', 29],
['🐍 var assignment explicit augmented subscript Mult.', 1],
['🐍 var assignment explicit augmented subscript Sub.', 13],
['🐍 var assignment explicit chained.', 6],
['🐍 var assignment explicit conditional compact.', 21],
['🐍 var assignment explicit conditional corrective.', 14],
['🐍 var assignment explicit conditional verbose.', 38],
['🐍 var assignment explicit constant.', 178],
['🐍 var assignment explicit index.', 384],
['🐍 var assignment explicit negate.', 1],
['🐍 var assignment explicit parallel.', 163],
['🐍 var assignment explicit parallel more_than_two.', 35],
['🐍 var assignment explicit parallel slide.', 11],
['🐍 var assignment explicit parallel swap.', 30],
['🐍 var assignment explicit sequence swap.', 13],
['🐍 var assignment explicit single.', 3458],
['🐍 var assignment explicit slice.', 4],
['🐍 var assignment explicit throwaway.', 5],
['🐍 var assignment implicit iteration_variable.', 1056],
['🐍 var assignment implicit iteration_variable throwaway.', 48],
['🐍 var assignment implicit parameter.', 1912],
['🐍 var assignment implicit parameter kwarg.', 6],
['🐍 var assignment implicit parameter self.', 568],
['🐍 var assignment implicit parameter vararg.', 5],
['🐍 var deletion index.', 7],
['🐍 var deletion unbinding.', 3],
['🐍 var scope global.', 113],
['🐍 var scope local.', 1653],
['🐍 var scope outer constant.', 43],
['🐍 var scope outer variable.', 70],
['🐍 var scope shadowing.', 127]]);
var options = {
    wordtree: {
    format: 'implicit',
    word: '🐍',
    },
};
var tree = new google.visualization.WordTree(document.getElementById('tree'));
tree.draw(data, options);
}
