import itertools

class Solver:

    variables = None
    blocks = None

    def set_vars(self, s):
        if not isinstance(s, set):
            raise Exception("Needs to be set")
        self.variables = s    

    def map_to(self, s):
        if not isinstance(s, set):
            raise Exception("Needs to be set")
        if self.variables is None:
            raise Exception("Must set variables to map")
        self.blocks = {v: s for v in self.variables}


class Constraint:
    pass

class And(Constraint):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def get(self):
        return get(c1) + ' & ' + get(c2)

    
class Universal(Constraint):
    def __init__(self, values, do):
        self.do = do
        self.values = values
        from inspect import signature 
        self.var_count = len(signature(do).parameters)

    def get(self):
        perms = itertools.product(self.values, repeat=self.var_count)
        result = set()
        for s in perms:
            args = list(s) 
            if self.do(*args): result.add(frozenset(s))
        return result

    def __iter__(self):
        return iter(self.get())


class In(Constraint):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        result = set()
        for s in self.x:
            if s in self.y: 
                result.add(s)
        return result

