#### Loop Variables and Filters

The `for` loop has a number of variables available within the loop, e.g. 
```python
    forloop.counter # the number of iterations so far (1-based)
    forloop.counter0 # the number of iterations so far (0-based)
    forloop.first # is this the first iteration? (True or False)
    forloop.last # is this the last iteration? (True or False)
```
and filters to help process data
```python
    value | divisibleby: 3 # returns True or False
    value | add: 2 # returns value + 2
    name | lower # returns name in lowercase
    # combining filters
    value | add: 2 | divisibleby: 3
    # sort list items by the `name` field
    locations | dictsort: 'name'
```