class Buffer:
    def __init__(self):
        self.lst = list()

    def add(self, *a):
        for value in a:
            self.lst.append(value)

        while len(self.lst) >= 5:
            s = 0
            for i in range(5):
                s += self.lst.pop(0)
            print(s)

    def get_current_part(self):
        return self.lst
