class Personalidad:

    def estadoAnimo(self):
        pass

class Feliz(Personalidad):

    def estadoAnimo(self):
        print("El Día de Hoy Estoy muy Alegre y Contento")


class Enojado(Personalidad):

    def estadoAnimo(self):
        print("El Día de Hoy Estoy muy Desanimado y Pesimista")


objeto1 = Feliz()
objeto2 = Enojado()

varPolimorfica=[]

varPolimorfica.append(objeto1)
varPolimorfica.append(objeto2)

print(varPolimorfica[0].estadoAnimo())
print(varPolimorfica[1].estadoAnimo())


"""

Programa Base de Polimorfismo con Estados de Animo.

"""
