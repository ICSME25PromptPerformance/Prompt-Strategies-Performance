class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        BitStatusUtil.check([states, stat])
        return states | stat
    
    @staticmethod
    def has(states, stat):
        BitStatusUtil.check([states, stat])
        return (states & stat) == stat
    
    @staticmethod
    def remove(states, stat):
        BitStatusUtil.check([states, stat])
        return states & ~stat
    
    @staticmethod
    def check(args):
        for arg in args:
            if arg < 0 or arg % 2 != 0:
                raise ValueError(f"{arg} not even")