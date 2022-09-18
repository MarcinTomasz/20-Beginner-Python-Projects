#Simply calculator that calculates...

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + '\n')

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + '\n')

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + '\n')

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + '\n')

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit \n')

    choice = input('Enter your choice: ')

    if choice == 'A':
        print('Addition \n')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        add(a, b)
    elif choice == 'B':
        print('Subtraction \n')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        sub(a, b)
    elif choice == 'C':
        print('Multiplication \n')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        mul(a, b)
    elif choice == 'D':
        print('Division \n')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        div(a, b)
    elif choice == 'E':
        print('Program ended')
        quit()