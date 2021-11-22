with open ('C:/Log/file.txt') as file:
    line_num = 1
    for line in file:
        print('{}:{}'.format(line_num, line.rstrip()))
        line_num += 1