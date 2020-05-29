# Factory functions
# define our function  here

# As a user, I can use the make_dough with 'water' and 'flour' to make 'dough'.

def make_dough(arg1, arg2):
    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    else:
        return 'not dough'

# As a user, I can use the bake_dough with dough to get naan.

def bake_dough(arg1):
    if arg1 == 'dough':
        return 'naan'
    else:
        return 'not naan'

# As a user, I can user the run_factory with water and flour and get naan.

def run_factory(arg1, arg2):
    if make_dough(arg1, arg2) == 'dough':
        arg3 = make_dough(arg1, arg2)
        return bake_dough(arg3)
    else:
        return bake_dough(arg1)