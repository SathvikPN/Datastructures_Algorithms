# default_ factory function called automatically 
# whenever defaultdict needs to initialize the value of a missing key in the dictionary.
from collections import defaultdict
dd = defaultdict(list) # defaultdict( default_factory function )
d = {'a':1, 'b':2}

for k,v in d.items():
    print(dd[k]) # Not already in mapping. But wo't raise KeyError because
    # entry is automatically created using the default_factory function which returns an empty list here.
    dd[k] = v

    # dictionary equivalent is
    # d.setdefault(k, []).append(v)
    
print(dd.items())
