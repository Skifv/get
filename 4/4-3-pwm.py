import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)

p.start(0)

try:
    while True:
        try:
            dc = (input("Введите коэффициент заполнения (q для выхода): "))
            if dc == 'q':
                break
            dc = int(dc)
        except ValueError:
            print('Ошибка ввода периода')
            continue
    
        p.ChangeDutyCycle(dc)

        U = 3.3 * (dc/100)

        print("U = ", U, "В")
except KeyboardInterrupt:
    print('\nПрограмма была остановлена с клавиатуры')
except ValueError:
    print('Ошибка ввода коэффициента заполнения')
finally:
    GPIO.cleanup()
    p.stop()