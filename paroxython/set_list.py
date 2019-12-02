from collections import UserList

class SetList(UserList):
    """List that eliminates redundant list items and implements set comparison methods.
    Adapted from ParallelRegression: https://github.com/rcbellamy/ParallelRegression
    """

    def __init__(self, values=None):
        UserList.__init__(self)
        if values != None:
            self.extend(values)
        if isinstance(values, (set, frozenset, type(dict().keys()))):
            self.data.sort()

    def __setitem__(self, key, value):
        if value in self.data:
            self.lastSIOutcome = False
        else:
            if key == len(self.data):
                self.data.append(value)
            else:
                self.data[key] = value
            self.lastSIOutcome = True

    def append(self, value):
        if value in self.data:
            return False
        else:
            self.data.append(value)
            return True

    def extend(self, values):
        return self.update(values)

    def add(self, value):
        return self.append(value)

    def discard(self, value):
        if value in self.data:
            self.data.remove(value)
            return True
        else:
            return False

    def pop(self, *, value=None, index=None):
        if index != None and not isinstance(index, int):
            raise KeyError("Index must be specified as an integer.", index)
        if value != None and index != None:
            raise KeyError(
                "Pop can remove an item by index or value but not"
                " both.  Value specified: %s, index specified: %d." % (value, index)
            )
        if index != None:
            return self.data.pop(index)
        elif value != None:
            if not value in self.data:
                raise KeyError("`%s` not in %s." % (value, self))
            i = self.data.index(value)
            return self.data.pop(i)
        else:
            raise KeyError(
                "One of `index` or `value` must be specified by "
                "keyword arguement when calling SetList.pop( )."
            )

    def update(self, values):
        if isinstance(values, (set, frozenset, type(dict().keys()))):
            values = list(values)
            values.sort()
        counter = 0
        for v in values:
            if self.append(v) == True:
                counter += 1
        return counter

    def difference(self, other):
        new = SetList()
        for value in self:
            if not value in other:
                new.append(value)
        return new

    def union(self, other):
        new = SetList()
        new.update(self)
        new.update(other)
        return new

    def intersection(self, other):
        new = SetList()
        for value in self:
            if value in other:
                new.append(value)
        return new

    def issubset(self, other):
        for value in self:
            if not value in other:
                return False
        return True

    def issuperset(self, other):
        for value in other:
            if not value in self:
                return False
        return True

    def symmetric_difference(self, other):
        new = self.difference(other)
        for value in other:
            if not value in self:
                new.append(value)
        return new

    @staticmethod
    def _re_sort(item):
        ## Exists so that it can be replaced by assignment on specific
        ## instances.
        return item

    @property
    def as_fsets(self):
        """set( ) of frozenset( )s of the items in each SetList( ) member.  The
        use of frozenset( )s enables the set( ) to contain otherwise non-
        hashable objects.  Useful for order-insensitive equality testing.
        """
        ret = set()
        for item in self.data:
            ret.add(frozenset(self._re_sort(item)))
        return ret

