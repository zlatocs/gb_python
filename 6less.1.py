import time
class Traffic:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def run(self):
        while True:
            print(Traffic.__color[0])
            time.sleep(7)
            print(Traffic.__color[1])
            time.sleep(2)
            print(Traffic.__color[2])
            time.sleep(5)
            print(Traffic.__color[3])
            time.sleep(2)

tl = Traffic()
tl.run()
