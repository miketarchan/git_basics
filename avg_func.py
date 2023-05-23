def avg(*iterable):
    
    def calc(param):
        return 0.0 if len(param) < 1 else sum(param) / len(param)
    
    return calc( iterable[0] if len(iterable) == 1 and hasattr(iterable[0],'__iter__') else iterable)

print(avg(1,2,3))