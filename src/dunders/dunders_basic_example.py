"""Dunders basic example."""

class MyString:
    """MyString class definition."""
    def __init__(self, string):
        self.string = string.encode('utf-8')

    def __str__(self):
        """String representation."""
        return self.string.decode('utf-8')

    def __add__(self, other):
        """Adding two strings."""
        return MyString(self.string.decode('utf-8') + other.string.decode('utf-8'))

    def __sub__(self, other):
        """Subtracting two strings."""
        left_op = self.string.decode('utf-8')
        right_op = other.string.decode('utf-8')
        if right_op in left_op:
            return MyString(left_op.replace(right_op, '', 1))
        return self.copy()

    def __mul__(self, times):
        """Multiplying the string n times."""
        return MyString(self.string.decode('utf-8') * int(times))

    def __truediv__(self, divisor):
        """Real division of the string — split into exactly `divisor` parts."""
        text = self.string.decode('utf-8')
        n = int(divisor)
        if n <= 0:
            raise ValueError("Division divisor must be a positive integer")
    
        L = len(text)
        # base size for each part and how many parts get an extra char
        base, rem = divmod(L, n)
    
        parts = []
        idx = 0
        for i in range(n):
            part_len = base + (1 if i < rem else 0)
            parts.append(MyString(text[idx:idx + part_len]))
            idx += part_len
    
        return parts


    def __len__(self):
        """Return the number of words in the string."""
        text = self.string.decode('utf-8').strip()
        return 0 if not text else len(text.split())

    def copy(self):
        """Make a shallow copy."""
        return MyString(self.string.decode('utf-8'))


if __name__ == '__main__':
    my_string = MyString('hello there')
    print(my_string)                # hello there
    my_new_string = my_string + MyString(' world')
    print(my_new_string)            
    print(my_new_string - MyString('world'))  # hello there 
    my_last_string = my_string.copy()
    print(my_string is my_last_string)        # False

    print(my_string * 3)           
    parts = my_string / 2
    for p in parts:
        print(p)                   
    print(len(MyString('')))       
    print(len(MyString('hello there')))  
