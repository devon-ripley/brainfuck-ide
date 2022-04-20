import sys
import json


def run():
    f = open('config.json', 'r')
    settings = json.load(f)
    f.close()
    array_size = settings['memory_array']
    byte_size = settings['memory_block']

    data_array = [0 for x in range(array_size)]
    debug = False
    file_name = None
    if len(sys.argv) == 1:
        print('No file name argument')
        exit()
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    if len(sys.argv) == 3:
        if sys.argv[2].lower() == 'debug':
            debug = True
    with open(file_name, 'r') as f:
        bf_script_pre = f.readlines()
    memory_index = 0
    script_index = 0
    loop_control = []
    bf_script = []
    for line in bf_script_pre:
        for com in line:
            bf_script.append(com)
    total_length = len(bf_script)
    in_loop = False
# interpreting loop
    bounce_back = False
    while script_index < total_length:
        command = bf_script[script_index]
        if command == ']':
            if in_loop:
                if data_array[loop_control[-1][0]] <= 0:
                    loop_control[-1][1] = False
                    in_loop = False
                    bounce_back = False
                    del loop_control[-1]
                elif data_array[loop_control[-1][0]] > 0:
                    script_index = loop_control[-1][2]
                    bounce_back = True
            else:
                print('ERROR "]" before "["')
                exit()

        elif command == '[':
            if bounce_back:
                bounce_back = False

            else:
                loop_control.append([memory_index, True, script_index])
                in_loop = True

        elif command == '>':
            memory_index += 1
        elif command == '<':
            memory_index -= 1
        elif command == '+':
            data_array[memory_index] += 1
        elif command == '-':
            data_array[memory_index] -= 1
        elif command == ',':
            user_in = input()
            if len(user_in) > 1:
                print('ERROR only one input is allowed')
            else:
                data_array[memory_index] = ord(user_in)

        elif command == '.':
            print(chr(data_array[memory_index]), end='')
        if debug:
            print('script index', script_index)
            print('command', bf_script[script_index])
            print('memory_index', memory_index)
            print('memory amount', data_array[memory_index])
            input('Enter for next command ')
        script_index += 1
    print('')
    print('Script run successfully!')


if __name__ == '__main__':
    print('Brainfuck Interpreter by Devon Ripley')
    run()
