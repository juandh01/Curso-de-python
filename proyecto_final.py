class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"👤 Nombre: {self.nombre} | Edad: {self.edad}")


class Ciudadano(Persona):
    def __init__(self, nombre, edad, deposito):
        super().__init__(nombre, edad)
        self.deposito = deposito

    def mostrar(self):
        super().mostrar()
        print(f" Depósito: ${self.deposito:.2f}")

    def paga_impuestos(self):
        return self.deposito > 4000


agenda = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    if nombre in agenda:
        print(" Ya existe este contacto.")
    else:
        edad = int(input("Edad: "))
        deposito = float(input("Depósito en USD: "))
        agenda[nombre] = Ciudadano(nombre, edad, deposito)
        print(" Contacto agregado.")


def consultar_contacto():
    nombre = input("Nombre a consultar: ")
    if nombre in agenda:
        agenda[nombre].mostrar()
        print(" ¿Paga impuestos?:", "Sí" if agenda[nombre].paga_impuestos() else "No")
    else:
        print(" No se encontró el contacto.")


def modificar_contacto():
    nombre = input("Nombre a modificar: ")
    if nombre in agenda:
        edad = int(input("Nueva edad: "))
        deposito = float(input("Nuevo depósito: "))
        agenda[nombre] = Ciudadano(nombre, edad, deposito)
        print(" Contacto actualizado.")
    else:
        print(" Contacto no encontrado.")


def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(" Contacto eliminado.")
    else:
        print(" No se encontró el contacto.")


def mostrar_reporte():
    if not agenda:
        print(" No hay contactos.")
        return
    total = len(agenda)
    paga = sum(1 for c in agenda.values() if c.paga_impuestos())
    no_paga = total - paga
    print("\n Reporte de Contactos:")
    for c in agenda.values():
        c.mostrar()
        print(" Paga impuestos:", "Sí" if c.paga_impuestos() else "No", "\n")
    print(f" Total: {total} | Pagan impuestos: {paga} | No pagan: {no_paga}")
    print(f" Porcentaje que paga: {paga / total * 100:.1f}%\n")


def menu():
    while True:
        print("\n GESTOR DE CONTACTOS BANCARIOS")
        print("1. Agregar contacto")
        print("2. Consultar contacto")
        print("3. Modificar contacto")
        print("4. Eliminar contacto")
        print("5. Ver reporte general")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            consultar_contacto()
        elif opcion == "3":
            modificar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            mostrar_reporte()
        elif opcion == "6":
            print(" Hasta luego.")
            break
        else:
            print(" Opción inválida.")


menu()
