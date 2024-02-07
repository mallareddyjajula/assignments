class outer:
    def __init__(self):
        print("outer class object creations")
    
    class Inner:
        def __init__(self):
            print("inner class of creation")
        
        def m1(self):
            print("inner class method")

o=outer()
i=o.Inner()
i.m1()

class outer:
    def __init__(self):
        print("outer class object creations")
    
    class Inner:
        def __init__(self):
            print("inner class of creation")
    class Inner:
        def _inner_(self):
            print("inner class start")
        
        def m1(self):
            print("inner class method")

o=outer()
i=o.Inner()
i=o.Inner()
i.m1()

class outer:
    def __init__(self):
        print("outer class object creations")
    
    class Inner:
        def __init__(self):
            print("inner class of creation")
    class Inner:
        def _inner_(self):
            print("inner class of training")
        
        def m1(self):
            print("inner class method")

o=outer()
i=o.Inner()
i=o.Inner()
i.m1()
