print('Welcome to calculator !! \n For calculation enter number and operator in this sequence a + b put one space between each set of numbers.\n For addition use : a + b \n For subtraction : a - b \n For multiplication : a x b \n For division : a / b')
p = True
while p:
    num1, operator, num2 = input('= ').split()
    if operator == '+':
        sum = int(num1)+int(num2)
        print(sum)
    elif operator == '-':
        subtract = int(num1)-int(num2)
        print(subtract)
    elif operator == 'x':
        multiply = int(num1)*int(num2)
        print(multiply)
    elif operator == '/':
        divide = int(num1)/int(num2)
        print(divide)
