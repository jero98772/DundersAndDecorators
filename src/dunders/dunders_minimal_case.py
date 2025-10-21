"""Minimal example for dunders."""

class MyObject:
    def __init__(self, value):
        self.value = value

    def __add__(self, right_obj):
        concatenated = str(self.value) + str(right_obj.value)
        # Return as new MyObject with integer value from concatenation
        return MyObject(int(concatenated))

    def __repr__(self):
        return f"MyObject({self.value})"

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    left_obj = MyObject(1)
    right_obj = MyObject(2)
    
    print(left_obj)         # prints "1"
    print(right_obj)        # prints "2"
    print(left_obj + right_obj)  # prints "12"
