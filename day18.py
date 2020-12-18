with open("inputs/day18.txt") as file:
    data = [line.strip().replace(" ", "") for line in file]

#  Not the prettiest solution, will improve later.

# Part 1 ===
part1 = 0

for line in data:

    stack = [0]
    operation_stack = []
    operation = "+"

    for char in line:

        if char.isnumeric():
            if operation == "+":
                stack[-1] += int(char)

            elif operation == "*":
                stack[-1] *= int(char)

        elif char in {"+", "*"}:
            operation = char

        elif char == "(":
            operation_stack.append(operation)
            stack.append(0)
            operation = "+"

        elif char == ")":
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer
            elif operation == "*":
                stack[-1] *= answer

    part1 += stack[0]


# Part 2 ===
part2 = 0

for line in data:

    stack = [0]
    operation_stack = [None]
    operation = "+"

    for char in line:

        if char.isnumeric():
            if operation == "+":
                stack[-1] += int(char)

        elif char == "*":
            if operation_stack[-1] == "*":  # End * group
                operation_stack.pop()
                answer = stack.pop()
                stack[-1] *= answer

            operation_stack.append("*")  # Start new * group
            operation = "+"
            stack.append(0)

        elif char == "+":
            operation = "+"

        elif char == "(":
            operation_stack.append(operation)
            operation = "+"
            stack.append(0)

        elif char == ")":
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer
            elif operation == "*":
                stack[-1] *= answer

                # Do it again if we have multiplication ending just before a closing parenthesis
                answer = stack.pop()
                operation = operation_stack.pop()

                if operation == "+":
                    stack[-1] += answer
                elif operation == "*":
                    stack[-1] *= answer

    if len(stack) > 1:  # Finish everything up if some numbers left in the stack
        for i in stack:
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer

            elif operation == "*":
                stack[-1] *= answer

    part2 += stack[0]


print("Part 1:", part1)
print("Part 2:", part2)
print(part1 == 67800526776934 and part2 == 340789638435483)
