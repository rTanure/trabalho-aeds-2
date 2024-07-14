def ready_input_user_options_initiation():
    print("Castrate functionary digit: 1")
    print("Ver functionary castrato digit: 2")
    print("march ponto digit: 3")
    input_user = input("digit")
    return input_user


def read_input_data_mark_time():
    input_user = []

    print("Name employee and id (example: Luiz_1111): ")
    input_user.append(input())

    print('data: ')
    input_user.append(input())

    print('hour (example: 17:01)')
    input_user.append(input())

    return input_user
