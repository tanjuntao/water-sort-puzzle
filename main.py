import time
from board import Board
from input import get_board



def bfs(init_board, output_file):
    queue = []
    visited = {}
    steps = 0
    queue.append(init_board)
    visited[init_board.string] = True

    start = time.time()
    while queue:
        size = len(queue)
        print(f"Step: {steps}, #States total: {len(queue)}")
        not_detected = 0
        for _ in range(size):
            curr_state = queue.pop(0)
            if curr_state.state_checking() is True:
                print('Elapsed time: {:.4f}'.format(time.time() - start))
                return curr_state, steps

            next_boards = curr_state.next_boards()
            output_file.write('\n' + str(steps) + '\n')
            for state in next_boards:
                state_str = state.string
                output_file.write(state_str + '\n')
                if state_str not in visited:
                    not_detected += 1
                    queue.append(state)
                    visited[state_str] = True

        print(f"Not detected: {not_detected}")
        steps += 1



if __name__ == '__main__':
    f = open('output.txt', 'w')
    init_board_ = Board(get_board(), parent=None)

    final_state, total_steps = bfs(init_board_, f)

    total_actions = []
    while final_state:
        print(final_state.string)
        action = f"Move {final_state.from_which + 1} to {final_state.to_which + 1}"
        total_actions.append(action)
        final_state = final_state.parent

    for idx, action in enumerate(total_actions[::-1]):
        print(f"Step: {idx}, Action: {action}")

    # print(final_state.string, total_steps)

