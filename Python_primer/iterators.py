# for element in iterable:
#    # do something with element

# ------------------------------------------------

demo = range(6) # range itself NOT an iterator object.
# range is a class of a list of immutable objects.

iter_obj = iter(demo) # create an iterator object from that iterable range object

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)

    except StopIteration:
        # if StopIteration is raised, break from loop
        break
