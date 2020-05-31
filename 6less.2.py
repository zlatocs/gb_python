class Road():
    length = int(input("Ведите длину дороги(м): "))
    width = int(input("Ведите ширину дороги(см): "))
    kg = 25
    sm = 5
    def raschet(self):
        tonna = Road.length*Road.width*Road.kg*Road.sm
        print(f'{tonna/1000:.0f} т')
rd = Road()
rd.raschet()





