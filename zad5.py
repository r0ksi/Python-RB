def listchecker(lst):
    for i in lst:
        if type(i) is list:
            return('True')
        else:
            return('False')
    if __name__ == '__main__':
        print(listchecker(lst1))
lst1 = [77, [1, 2, 3], {'haslo': 'Jozef Tkaczuk'}]
if __name__ == '__main__':
    listchecker(lst1)

