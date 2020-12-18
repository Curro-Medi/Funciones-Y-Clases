from Ejercicio7.Aula import Aula, aula2
aula = Aula("3 metros", "4 metros", "3 metros", False)


print(aula.descripcion())
print(aula.completo())
print(aula.estado())
print(aula.descripcion())


miaula = Aula("3 metros", "5 metros", "4 metros", True)
print()
print(miaula.miauladatos())


aulaa2 = aula2("3 metros", "5 metros", "4 metros", True, "")
print()
print(aulaa2.estado())
print(aulaa2.descripcionaula2())
