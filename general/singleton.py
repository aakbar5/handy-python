""" Force python class to have single object. """

def SingletonInterface(cls):
    class_instances = {}
    def get_instance():
        if cls not in class_instances:
            class_instances[cls] = cls()
        return class_instances[cls]
    return get_instance

@SingletonInterface
class TestClass:
    def __init__(self):
        print("Init is called")

    def fun(self):
        print("fun is called")


# Init should be called as first instance of the class
obj = TestClass()
obj.fun()

# Another class instance; no init function should be called
obj = TestClass()
obj.fun()

# Another class instance; no init function should be called
obj = TestClass()
obj.fun()

# Expected Output:
# Init is called
# fun is called
# fun is called
# fun is called
