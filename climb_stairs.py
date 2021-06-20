def climb_stairs(stairs_num):
    if stairs_num > 3:
        return (climb_stairs(stairs_num - 3) + climb_stairs(stairs_num - 2) +
                climb_stairs(stairs_num - 1))
    elif stairs_num == 3:
        solutions = [
            [1, 1, 1],
            [1, 2],
            [2, 1],
            [3],
        ]
        return len(solutions)
    elif stairs_num == 2:
        solutions = [
            [1, 1],
            [2],
        ]
        return len(solutions)
    elif stairs_num == 1 or stairs_num == 0:
        return 1
    else:
        raise ValueError("Input Error")


# solutions = []

# def climb_stairs(stairs_num, solutions):
#     if stairs_num > 2:
#         for solution in solutions:
#             solution.append(1)
#         return climb_stairs(stairs_num - 1, solutions)
#     elif stairs_num == 2:
#         solutions = [
#             [1, 1],
#             [2],
#         ]
#         return solutions
#     elif stairs_num == 1:
#         solutions = [
#             [1],
#         ]
#         return solutions
#     elif stairs_num = 0:
#         solutions = [
#             [0],
#         ]
#         return solutions
#     else:
#         raise("Input Error")
#         return 0

if __name__ == '__main__':
    while True:
        stairs_num = int(input("Input stairs num: "))
        if stairs_num < 0:
            break
        print(f'stairs_num: {stairs_num}')
        print(f'solutions: {climb_stairs(stairs_num)}')
