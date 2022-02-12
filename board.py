from copy import deepcopy


class Board:
    """Abstraction of state"""
    def __init__(self, board, parent=None, from_which=-1, to_which=-1):
        """Initialize a board(state)

        Board and state are equivalent in our comments.

        Args:
            board [list[list]]: all bottles
            parent [Board]: the parent of current state
            from_which [int]: index of bottle which pops color blocks
            to_which [int]: index of bottle which push color blocks
        """
        self.board = board
        self.parent = parent
        self.from_which = from_which
        self.to_which = to_which

    def next_boards(self):
        """Successor function: all next states of the current state

        Returns: list[Board]
            All valid successive states from current state
        """
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
                if self.board[j].finished:
                    continue
                pseudo_push_res = self.board[j].push(pseudo_pop_res, pseudo=True)
                if pseudo_push_res == -1:
                    continue

                # Add your heuristic pruning strategies here
                if self.board[i].size == len(pseudo_pop_res) and self.board[j].size == 0:
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
        """Whether current state is our goal state"""
        for bottle in self.board:
            if not self._consisitent(bottle.data):
                return False

        return True

    def _consisitent(self, bottle_data):
        """Whether we have done with this bottle"""
        return bottle_data[0] == bottle_data[1] and \
            bottle_data[1] == bottle_data[2] and \
            bottle_data[2] == bottle_data[3]

    @property
    def string(self):
        """String representation of the current state"""
        return "".join([bottle.string for bottle in self.board])

    @classmethod
    def board_factory(cls, board, parent=None, from_which=-1, to_which=-1):
        """Generate new state"""
        return cls(board, parent=parent, from_which=from_which, to_which=to_which)

