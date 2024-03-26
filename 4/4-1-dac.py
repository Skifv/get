import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        user_input = (input("Введите целое число от 0 до 255 (или q для завершения): "))

        if user_input == 'q':
            break
        
        try:
            number = int(user_input)

            if number < 0 or number > 255:
                print("Ошибка: выход за границы допустимого диапазона чисел")
                continue
        except ValueError:
            print("Ошибка: было введено не целое число")
            continue
        
        binary = decimal2binary(number)
       
        for i in range(8):
            GPIO.output(dac[i], binary[i])

        U = number * (3.3/256)

        print("U =", U, "В")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()