gt = {} # gt is the acornym for gradetext

def main():

    print ('Types of Command lines:\nCommand 1(录入) \nCommand 2(查询) \nCommand 3(删除)')
    i = input('Your Command line is:')
    i = int(i)
    if i == 1:
        Command1()
    elif i == 2:
        Command2()
    elif i == 3:
        Command3()
    else:
        print ('You have entered an invalid Command line,please run this programme again.')

def Command1():
    while(True):
        Name = input('Name:')
        Grade = input('Grade:')
        try: # Make sure the input is an int or a float
            Grade = float(Grade)
            gt[Name] = Grade
            print ('You have successfully uploaded the file!')
            break;
        except ValueError:
            print ('Please enter an number!')


def Command2():
    Name = input('Name:')
    if Name in gt:
        print ('{}\'s grade is {}'.format(Name,gt[Name]) )
    else:
        print ('It is not included')


def Command3():
    Name = input('Name:')
    if Name in gt:
        n = input('Do you want to delete it?(Y/N):')
        if n == 'Y' or 'y':
            del gt[Name]
        else:
            print ('You have canceled this operation.')
    else:
        print ('This is not included.')


if __name__ == '__main__':
    while(True):
        main()
        j = input('Do you want to exit?(If so,please enter exit):')
        if j == 'exit':
            break
            print ('Done')
        else:
            continue

