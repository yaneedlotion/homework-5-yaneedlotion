


if __name__ == "__main__":

    food = ['rice', 'beans']
    print(food)
    food.append('broccoli')
    print(food)
    food.extend(['bread', 'pizza'])
    print(food)
    print(food[0:2])
    print(food[-1])


    breakfast = "eggs, fruit, orange juice".split(", ")
    print(breakfast)

    print(len(breakfast) == 3)


    digit_list = []
    i = 0
    while i < 1:
        digit_value = input('floating-point val/stop:').lower()
        if digit_value == 'stop':
            print('stopped')
            print(f'list: {digit_list}')
            break
        digit_list.append(float(digit_value))
        print(f'current list: {digit_list}')

    len(digit_list) > 0
    avg_list = sum(digit_list) / len(digit_list)
    print(f'avg of list: {avg_list}')
    print(f'min val: {min(digit_list)}')
    print(f'max val: {max(digit_list)}')