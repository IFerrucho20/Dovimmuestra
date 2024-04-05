import os

# Función para listar directorios excluyendo los que contengan ciertas palabras clave
def listar_directorios(path, exclusiones):
    try:
        # Listar todos los directorios en la ruta dada
        todos_los_directorios = next(os.walk(path))[1]
        # Filtrar los directorios que no contengan las palabras clave de exclusión
        directorios_filtrados = [d for d in todos_los_directorios if not any(excluido in d for excluido in exclusiones)]
        return directorios_filtrados
    except Exception as e:
        print(f"Error al listar directorios: {e}")
        return []

# Función para navegar entre directorios
def navegar_directorios(path_inicial, exclusiones):
    path_actual = path_inicial
    while True:
        print(f"Directorio actual: {path_actual}")
        directorios = listar_directorios(path_actual, exclusiones)
        # Imprimir los directorios disponibles para la selección del usuario
        for i, directorio in enumerate(directorios, start=1):
            print(f"{i}. {directorio}")
        # Pedir al usuario que seleccione un directorio o salir
        seleccion = input("Seleccione un número para entrar al directorio o 'salir' para finalizar: ")
        if seleccion.lower() == 'salir':
            break
        else:
            try:
                # Cambiar al directorio seleccionado
                indice = int(seleccion) - 1
                if 0 <= indice < len(directorios):
                    path_actual = os.path.join(path_actual, directorios[indice])
                else:
                    print("Selección inválida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

# Función para filtrar archivos por un patrón específico
def filtrar_archivos_por_patron(path, patron):
    try:
        # Listar todos los archivos en la ruta dada
        todos_los_archivos = next(os.walk(path))[2]
        # Filtrar los archivos que contengan el patrón especificado
        archivos_filtrados = [f for f in todos_los_archivos if patron in f]
        return archivos_filtrados
    except Exception as e:
        print(f"Error al filtrar archivos: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    path_inicial = "C:\\Users\\Hermanos Ferrucho\\OneDrive - UWCOLOMBIA\\Bases\\Muestras\\2023\\REGIONAL SUROCCIDENTE"
    exclusiones = ["Fortalecimiento", "La vuelta al mundo"]
    patron_archivo = "_estratificado_personas_seleccionadas_"

    # Navegar entre directorios
    navegar_directorios(path_inicial, exclusiones)

    # Filtrar archivos en el último directorio alcanzado
    archivos = filtrar_archivos_por_patron(path_inicial, patron_archivo)
    print("Archivos filtrados:")
    for archivo in archivos:
        print(archivo)

