# I have two Python dictionaries, and I want to write a single expression that returns these
# two dictionaries, merged. The update() method would be what I need, if it returned its result
# instead of modifying a dictionary in-place.
#
# >>> x = {'a': 1, 'b': 2}
# >>> y = {'b': 10, 'c': 11}
# >>> z = x.update(y)
# >>> print(z)
# None
# >>> x
# {'a': 1, 'b': 10, 'c': 11}
# How can I get that final merged dictionary in z, not x?

"""For dictionaries x and y, z becomes a shallowly merged dictionary with values from y replacing
 those from x.

In Python 3.5 or greater:

z = {**x, **y}
In Python 2, (or 3.4 or lower) write a function:

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
and now:

z = merge_two_dicts(x, y)
In Python 3.9.0a4 or greater (final release date approx October 2020): PEP-584, discussed here,
was implemented to further simplify this:

z = x | y          # NOTE: 3.9+ ONLY
"""