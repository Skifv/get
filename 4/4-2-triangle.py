import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)


try:
    while(True):
        try:
            period = (input("Введите период (q для выхода): "))
            if period == 'q':
                break
            period = int(period)
        except ValueError:
            print('Ошибка ввода периода')
            continue

        flag = 1

        while(True):
            if flag == 1:
                binar = decimal2binary(0)
                GPIO.output(dac, binar)
                time.sleep(period/512)

            for i in range(1, 255, 1):
                U = i * (3.3/256)
                print("U =", U, "В")
                binar = decimal2binary(i)
                GPIO.output(dac, binar)
                time.sleep(period/512)

            for i in range(254, -1, -1):
                U = i * (3.3/256)
                print("U =", U, "В")
                binar = decimal2binary(i)
                GPIO.output(dac, binar)
                time.sleep(period/512)
except KeyboardInterrupt:
    print('\nПрограмма была остановлена с клавиатуры')
except ValueError:
    print('Ошибка ввода периода')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()