def solution(order):
    answer = [order[0]]

    second_belt = list(range(1, order[0]))
    main_belt = list(range(order[0] + 1, len(order) + 1))

    goal = 1
    main_idx = 0

    while (main_idx < len(main_belt) or second_belt) and goal < len(order):
        if (
            main_idx < len(main_belt)
            and order[goal] == main_belt[main_idx]
        ):
            answer.append(order[goal])
            main_idx += 1
            goal += 1

        elif second_belt and order[goal] == second_belt[-1]:
            answer.append(order[goal])
            second_belt.pop()
            goal += 1

        elif main_idx < len(main_belt):
            second_belt.append(main_belt[main_idx])
            main_idx += 1

        else:
            break

    return len(answer)