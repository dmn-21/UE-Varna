from collections import deque


def list_manipulator(numbers, *args):
    numbers_new = deque(numbers)

    if args[0] == 'add':

        if args[1] == 'beginning':
            for num in reversed(args[2:]):
                numbers_new.appendleft(num)

        elif args[1] == 'end':
            for num in args[2:]:
                numbers_new.append(num)

    elif args[0] == 'remove':
        if args[1] == 'beginning':

            if len(args[2:]) > 0:

                for _ in range(int(args[2])):
                    numbers_new.popleft()
            else:
                numbers_new.popleft()

        elif args[1] == 'end':
            if len(args[2:]) > 0:

                for _ in range(int(args[2])):
                    numbers_new.pop()
            else:
                numbers_new.pop()
    return list(numbers_new)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
