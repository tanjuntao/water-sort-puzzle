import argparse
import time
from board import Board
from input import get_start_board


def bfs(init_board):
    """BFS searching algorithm

    Args:
        init_board: initial board/state

    Returns:
        curr_state: one possible final state
        steps: total moving steps
    """
    queue = []
    visited = set()
    steps = 0
    queue.append(init_board)
    visited.add(init_board.string)

    start = time.time()
    while queue:
        size = len(queue)
        print(f"Step: {steps}, #States total: {len(queue)}")

        for _ in range(size):
            curr_state = queue.pop(0)
            if curr_state.state_checking() is True:
                print('Elapsed time: {:.4f}s'.format(time.time() - start))
                return curr_state, steps

            for state in curr_state.next_boards():
                state_str = state.string

                if state_str not in visited:
                    queue.append(state)
                    visited.add(state_str)

        steps += 1


def dfs(init_board):
    """DFS searching algorithm

    Args:
        init_board: initial board/state

    Returns:
        curr_state: one possible final state
    """
    stack = []
    stack.append(init_board)
    visited = set()

    start = time.time()
    while stack:
        curr_state = stack.pop()
        if curr_state.state_checking() is True:
            print('Elapsed time: {:.4f}s'.format(time.time() - start))
            return curr_state

        if curr_state.string not in visited:
            visited.add(curr_state.string)
            for next_state in curr_state.next_boards():
                stack.append(next_state)


if __name__ == '__main__':
    # 1. prepare args parser
    parser = argparse.ArgumentParser('Choose searching method')
    parser.add_argument('--search', type=str, default='dfs')
    args = parser.parse_args()

    # 2. get initital game board
    start_board = Board(get_start_board(), parent=None)

    # 3. run searching algorithm
    if args.search == 'bfs':
        final_state, total_steps = bfs(init_board=start_board)
    elif args.search == 'dfs':
        final_state = dfs(init_board=start_board)
    else:
        raise ValueError('Unvalid searching algorithm, please check it again.')
    print('final state string: {}'.format(final_state.string))

    # 4. get actions
    total_actions = []
    total_strings = []
    while final_state:
        total_strings.append(final_state.string)
        action = f"Move {final_state.from_which + 1} to {final_state.to_which + 1}"
        total_actions.append(action)
        final_state = final_state.parent

    for idx, data in enumerate(zip(total_strings[::-1], total_actions[::-1])):
        print(f"Step: {idx}, Action: {data[1]}")
