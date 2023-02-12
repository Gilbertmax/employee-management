import matplotlib.pyplot as plt

#clase padre
class empleado():
    
    def __init__(self, num_emp, nombre, apellido, fecha_nacimiento, nss, sueldo_base, años_antiguedad):
        self.num_emp = num_emp
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nss = nss
        self.sueldo_base = sueldo_base
        self.años_antiguedad = años_antiguedad

    def info(self):
        print("Numero de empleado: " + self.num_emp + ".")
        print("Nombre completo: " + self.nombre, self.apellido + ".")
        print("Fecha de nacimiento: " + self.fecha_nacimiento + ".")
        print("El numero de seguro social es: " + self.nss + ".")
        print("Sueldo base: " + self.sueldo_base + ".")
        print("Años de antiguedad: " + self.años_antiguedad + ".")

#subclase administrativo
class administrativos(empleado):
    tipo_trabajador = "Administrativo"

#subclase empleados de ventas
class emp_ventas(empleado):
    tipo_trabajador = "Ventas"

#subclase empleados supervisores
class supervisores(empleado):
    tipo_trabajador = "Supervisor"

#subclase Gerentes
class gerente():
    tipo_trabajador = "Gerente"

    def __init__(self, num_emp, nombre, apellido):
        self.num_emp = num_emp
        self.nombre = nombre
        self.apellido = apellido
        

    def info(self):
        print("Numero de empleado: " + self.num_emp + ".")
        print("Nombre completo: " + self.nombre, self.apellido + ".")


#variable para ingresar a las if
a = int(input("Inserte:\n1 - Para visualizar a los empleados administrativos:\n2 - Para visualizar a los empleados de ventas:\n3 - Para visualizar a los supervisores:\n4 - Para visualizar a los Gerentes:\n-------->" ))

#if de administrativos
if a == 1:
    empleado_admin = administrativos("152367", "Ernesto", "Rosas", "26-05-1992","63257415", "$13,000.00", "3 años")
    print(empleado_admin.tipo_trabajador)
    empleado_admin.info()

#elif de ventass
elif a == 2:
    empleado_ventas = emp_ventas("110355", "Maria", "Garcia", "15-07-1995", "65137945", "$11,000.00", "1 años")
    print(empleado_ventas.tipo_trabajador)
    empleado_ventas.info()
    b = int(input("Inserte:\n1 - Para imprimir el reporte del los ultimos 6 meses de ventas:\n2 - Para salir de la aplicación:\n-------->"))
    if b == 1:
        #fechas con registros actuales
        eje_x = ["Enero", "Febero", "Marzo", "Abril", "Mayo", "Junio"]
        #ventas registradas en cada periodo
        eje_y = [220050.15, 356480.80, 153500.10, 250020.50, 402030.75, 305236.10]
        #grafica
        plt.bar(eje_x, eje_y)
        #Montos de ventas
        plt.ylabel("Monto de ventas")
        #Meses
        plt.xlabel("Ventas Mensuales")
        #Titulo de las graficas
        plt.title("Reporte de ventas Enero-Junio")
        #Muestra de grafica
        plt.show()

    elif b == 2:
        print("---ADIOS---")

#elif de supervisores
elif a == 3:
    empleado_super = supervisores("102490", "Ruperta", "Cerda", "05-01-1993", "64535879", "$12,000.00", "2 años")
    print(empleado_super.tipo_trabajador)
    empleado_super.info()

#elif de gerentes
elif a == 4:
    empleado_gerente = gerente ("10001", "Armando", "Casas")
    print(empleado_gerente.tipo_trabajador)
    empleado_gerente.info()
    print("---ESTA INFORMACION SOLO CUENTA COMO CREDENCIAL DEL PERSONAL---\nPARA SABER MAS SOBRE ESTA INFORMACION DIRIGIRSE AL AREA DE RECURSOS HUMANSO.")




