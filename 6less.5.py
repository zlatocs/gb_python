class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем фломастером')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
stat = Stationery('отрисовка')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()