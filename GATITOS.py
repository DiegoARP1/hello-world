class Gato:
    def __init__(self,nombre,tipo,edad,color,calidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.color = color
        self.calidad = calidad

        #para sus acciones indiquemos su gustos
        if self.edad >= 1:
            self.cari = 12
        else:self.cari=5
    #accion de acariciar
    def acariciar(self,carinos):
        cari = self.cari
        if cari>int(carinos):
            print(f'MIAU!!\n{self.nombre} se ha enfurecido porque le has dado menos cariños de los que se merece un lindo gatito de {self.edad} años.')
        elif cari<=carinos:
            print(f'MIAU!<3\n {self.nombre} recibio cariñitos y esta mas alegre que la chucha! #')
            self.calidad += int(carinos)//2

peluso = Gato('peluso','choro',12,'blanquinegro',5)
marykripi = Gato('MaryKripi','Maricona',1,'negricafe',6)

marykripi.acariciar(15)






