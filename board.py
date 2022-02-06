from copy import deepcopy

from bottle import Bottle


class Board:
    def __init__(self, board, parent=None, from_which=-1, to_which=-1):
        self.board = board
        self.parent = parent
        self.from_which = from_which
        self.to_which = to_which

    def next_boards(self):
        next_states = []
        n_bottles = len(self.board)

        for i in range(n_bottles):
            if self.board[i].finished:
                continue
            pseudo_pop_res = self.board[i].pop(pseudo=True)
            if pseudo_pop_res is None:
                continue

            for j in range(n_bottles):
                if i == j: continue
                pseudo_push_res = self.board[j].push(pseudo_pop_res, pseudo=True)
                if pseudo_push_res == -1:
                    continue

                # generate new boards(states)
                copied_board = deepcopy(self.board)
                copied_board[j].push(copied_board[i].pop())
                next_states.append(Board.board_factory(board=copied_board,
                                                       parent=self,
                                                       from_which=i,
                                                       to_which=j))

        return next_states

    def state_checking(self):
        for bottle in self.board:
            if not self._consisitent(bottle.data):
                return False

        return True

    def _consisitent(self, bottle_data):
        return bottle_data[0] == bottle_data[1] and \
            bottle_data[1] == bottle_data[2] and \
            bottle_data[2] == bottle_data[3]

    @property
    def string(self):
        return "".join([bottle.string for bottle in self.board])

    @classmethod
    def board_factory(cls, board, parent=None, from_which=-1, to_which=-1):
        return cls(board, parent=parent, from_which=from_which, to_which=to_which)

