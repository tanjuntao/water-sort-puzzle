from color import Colors


class Bottle:
    """Abstraction of a single bottle in the game"""
    MAXIMUM_SIZE = 4

    def __init__(self, number, colors):
        """Initialize a bottle

        Args:
            number[int]: number of the bottle
            colors[list]: colors in this bottle
        """
        self.number = number
        self.data = colors.copy()

        if self.string == '0000': # empty bottle
            self.top_pointer = -1
        else:
            curr = 0
            while curr < len(self.data) and self.data[curr] != 0:
                curr += 1

            self.top_pointer = curr - 1

    @property
    def size(self):
        """Number of color blocks in this bottle"""
        return self.top_pointer + 1

    @property
    def string(self):
        """String representation of this bottle"""
        return "".join([str(val) for val in self.data])

    def pop(self, pseudo=False):
        """Pop color blocks from this bottle

        Args:
            pseudo[bool]: if set True, we only GET the top
                color blocks of this bottle, which will not be
                removed from this bottle

        Returns:
             Color blocks[list]
        """
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
        """Push color blocks to this bottle

        Args:
            colors: new color blocks need to be pushed into this bottle
            pseudo: if set to True, we only test if the new color
                blocks could be pushed into this bottle, the bottle itself
                will not change.

        Returns: [status code]
            0: the new color blocks could be pushed into this bottle
            -1: the new color can NOT pushed into this bottle
        """
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
        """Whether we have done with this bottle.

        If true, then this bottle will not accept new pop and push operations"""
        return self.data[0] != Colors.BLANK and \
               self.data[0] == self.data[1] and \
               self.data[1] == self.data[2] and \
               self.data[2] == self.data[3]


if __name__ == '__main__':
    bow = Bottle(0, [1, 2, 2, 2])
    print(bow.pop())




