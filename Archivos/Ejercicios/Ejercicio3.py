def notvim():
    x = None
    lines = list()
    n = 1
    while x != '::q':
        print(f'{n}| ',end='')
        x = input(r'')
        n += 1
        if x != '::q':
            lines.append(x)
            lines.append('\n')
    with open(input('File Name: '),'w+') as file:
        file.writelines(lines[:-1])
    # print(''.join(lines[:-1]))
    print(f'File: {int(len(lines)/2)}L written')
notvim()