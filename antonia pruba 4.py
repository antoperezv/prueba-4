pacientes = [] 

def validar_nombre(nombre): 
    return nombre.strip() != "" 

def validar_edad(edad): 
    return edad > 0 

def validar_temperatura(temperatura): 
    return 35.0 <= temperatura <= 42.0 

def mostrar_menu(): 
    print("\n========== MENU PRINCIPAL ============") 
    print("1. Agregar paciente") 
    print("2. Buscar paciente") 
    print("3. Eliminar paciente") 
    print("4. Actualizar estado") 
    print("5. Mostrar pacientes") 
    print("6. Salir") 

def leer_opcion(): 
    while True: 
        try: 
            opcion = int(input("seleccione una opcion (1-6): ")) 
            if 1 <= opcion <= 6: 
                return opcion 
            else: 
                print("debe ingresar una opcion valida.") 
        except ValueError: 
            print("Error: debe ingresar un numero valido") 
def agregar_paciente(lista): 
    nombre = input("ingrese nombre del paciente: ") 
    if not validar_nombre(nombre): 
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.") 
        return 
    
    try: 
        edad = int(input("ingrese edad: ")) 
        if not validar_edad(edad): 
            print("Error: La edad debe ser un número entero mayor que cero") 
            return 
    except ValueError: 
        print("Error: la edad debe ser un numero entero") 
        return 
    
    try: 
        temperatura = float(input("ingrese temperatura (35.0-42.0): ")) 
        if not validar_temperatura(temperatura): 
            print("Error: La temperatura debe ser un número decimal entre 35.0 y 42.0") 
            return 
    except ValueError: 
        print("Error: la temperatura debe ser un numero decimal.") 
        return 
    paciente = { 
        "nombre": nombre, 
        "edad": edad, 
        "temperatura": temperatura, 
        "atendido": False 
    } 
    lista.append(paciente) 
    print("Paciente registrado correctamente") 

def buscar_paciente(lista, nombre): 
    for i in range(len(lista)): 
        if lista[i]["nombre"] == nombre:
            return i 
    return -1 

def actualizar_estado(lista): 
    for paciente in lista: 
        if paciente["temperatura"] <= 37.0: 
            paciente["atendido"] = True 
        else: 
            paciente["atendido"] = False 
def mostrar_pacientes(lista): 
    actualizar_estado(lista) 
    if len(lista) == 0: 
        print("no existen pacientes registrados.") 
        return 
    print("\n===== LISTA DE PACIENTES ======") 
    for paciente in lista: 
        print(f"nombre: {paciente['nombre']}") 
        print(f"edad: {paciente['edad']}") 
        print(f"temperatura: {paciente['temperatura']}") 
        if paciente["atendido"]: 
            print("estado: atendido") 
        else: 
            print("estado: requiere atencion") 
        print("*" * 45) 
while True: 
    mostrar_menu() 
    opcion = leer_opcion() 
    if opcion == 1: 
        agregar_paciente(pacientes) 
    elif opcion == 2: 
        nombre = input("ingrese nombre a buscar: ") 
        posicion = buscar_paciente(pacientes, nombre) 
        if posicion != -1: 
            print("\npaciente encontrado") 
            print("posicion:", posicion) 
            print(pacientes[posicion]) 
        else: 
            print("el paciente no existe.") 
    elif opcion == 3: 
        nombre = input("ingrese nombre a eliminar: ")
        posicion = buscar_paciente(pacientes, nombre)
        if posicion != -1: 
            pacientes.pop(posicion) 
            print("paciente eliminado correctamente.") 
        else: 
            print(f"el paciente '{nombre}' no se encuentra registrado.")
    elif opcion == 4: 
        actualizar_estado(pacientes) 
        print("estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_pacientes(pacientes) 
    elif opcion == 6:
        print("gracias por usar el sistema. vuelva pronto") 
        break