base_empleados = [
    [101, 21],
    [102, 14],
    [103, 7],
    [104, 0]
]

def verificar_ID(ID_ingresado):
    for empleado in base_empleados:
        if empleado[0] == ID_ingresado:
            return empleado[1]
    return None

def simular_Bot():
    print("SISTEMA DE GESTION DE VACACIONES")
    print("Autora: Lara Bellingi")
    print("[Usuario]: Envia comando /start")
    print("[Usuario]: Selecciona la opcion 'Solicitar Vacaciones'")
    estado_usuario = "ESPERANDO_ID"
    
    try:
        ID = int(input("[Usuario]: Por favor ingrese su ID: "))
    except ValueError:
        print("[Error]: El legajo debe ser un valor numérico entero.")
        print("FIN DEL PROCESO CON ERRORES")
        return
        
    saldo_disponible = verificar_ID(ID)
    
    if saldo_disponible == None:
        print("[Error]: ID no encontrado en la base de datos.")
        print("FIN DEL PROCESO CON ERRORES")
        return
        
    print("[Sistema]: ID encontrado en la base de datos.")
    print(f"[Sistema]: Legajo autenticado. Saldo actual del empleado: {saldo_disponible} días.")
    estado_usuario = "ESPERANDO_FECHA_INICIO"
    
    try:
        fecha_inicio = int(input("[Usuario]: Por favor ingrese la cantidad de días de vacaciones: "))
    except ValueError:
        print("[Error]: La fecha debe ser un valor numérico entero.")
        print("FIN DEL PROCESO CON ERRORES")
        return
        
    if 0 < fecha_inicio <= saldo_disponible:
        solicitud_aprobada = True
        for empleado in base_empleados:
            if empleado[0] == ID:
                empleado[1] -= fecha_inicio
                print("[Sistema]: Tiene saldo suficiente")
                print("[Sistema]: Mensaje: 'Actualizando base de datos y confirmando registro...'")
                print("[Sistema]: ¡SOLICITUD PROCESADA EXITOSAMENTE!")
                print(f"[Sistema]: Comprobante: ID {ID} aprobó {fecha_inicio} días. Nuevo Saldo: {empleado[1]} días.")
                print("FIN DEL PROCESO, SOLICITUD APROBADA")
    else:
        solicitud_aprobada = False
        print("[Sistema]: Saldo insuficiente")
        print("[Sistema]: Mensaje: 'Error: Solicitud rechazada debido a saldo insuficiente'")
        print("FIN DEL PROCESO, SOLICITUD RECHAZADA")

if __name__ == "__main__":
    simular_Bot()