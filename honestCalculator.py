msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = float(0)


def is_one_digit(v):
    if float(v) > -10 and float(v) < 10 and float(v).is_integer():
        output = True
        return output
    else:
        output = False
        return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split(" ")
        if x == "M":
            x = float(memory)
        if y == "M":
            y = float(memory)
        x = float(x) or int(x)
        y = float(y) or int(y)

        if oper != "+" and oper != "-" and oper != "*" and oper != "/":
            print(msg_2)
        elif oper == "+":
            check(x, y, oper)
            result = x + y
            print(result)
        elif oper == "-":
            check(x, y, oper)
            result = x - y
            print(result)
        elif oper == "*":
            check(x, y, oper)
            result = x * y
            print(result)
        elif oper == "/" and y != 0:
            check(x, y, oper)
            result = (x / y)
            print(result)
        elif oper == "/" and y == 0:
            check(x, y, oper)
            print(msg_3)
            continue

        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    print(msg_[msg_index])
                    answer3 = input()
                    if answer3 == "y":
                        msg_index = msg_index + 1
                    elif answer3 == "n":
                        break
                    else:
                        continue
                if msg_index == 13:
                    memory = result
            else:
                memory = result

            print(msg_5)
            answer2 = input()
            if answer2 == "y":
                continue
            elif answer2 == "n":
                break
        elif answer == "n":
            print(msg_5)
            answer2 = input()
            if answer2 == "y":
                continue
            elif answer2 == "n":
                break
    except ValueError:
        print(msg_1)
