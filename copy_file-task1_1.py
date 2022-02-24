def task_1():
    with open('/home/admin-pc/text.txt', 'r') as inp:
        y = inp.read().upper()
    with open('/home/admin-pc/copied/text.txt', 'a') as out:
        out.write(y)

#task_1()
