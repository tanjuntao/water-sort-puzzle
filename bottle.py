from color import Colors


class Bottle:
    MAXIMUM_SIZE = 4

    def __init__(self, number, colors):
        self.number = number
        self.data = colors.copy()

        if self.string == '0000':
            self.top_pointer = -1
        else:
            self.top_pointer = 3

    @property
    def size(self):
        return self.top_pointer + 1

    @property
    def string(self):
        return "".join([str(val) for val in self.data])

    def pop(self, pseudo=False):
        if self.top_pointer == -1:
            return None
        curr = self.top_pointer
        while curr >= 1:
            if self.data[curr] == self.data[curr - 1]:
                curr -= 1
            else:
                break

        res = self.data[curr:self.top_pointer + 1]
        if not pseudo:
            for idx in range(curr, self.top_pointer + 1):
                self.data[idx] = 0
            self.top_pointer = curr - 1

        return res

    def push(self, colors, pseudo=False):
        space_remain = Bottle.MAXIMUM_SIZE - (self.top_pointer + 1)
        if len(colors) > space_remain:
            return -1

        if self.top_pointer != -1 and self.data[self.top_pointer] != colors[0]:
            return -1

        if not pseudo:
            self.data[self.top_pointer+1:self.top_pointer+1+len(colors)] = colors
            self.top_pointer += len(colors)
        return 0

    @property
    def finished(self):
        return self.data[0] != Colors.BLANK and \
               self.data[0] == self.data[1] and \
               self.data[1] == self.data[2] and \
               self.data[2] == self.data[3]

if __name__ == '__main__':
    bow = Bottle(0, [1, 2, 2, 2])
    print(bow.pop())




