import os

# Función para verificar el contenido de la carpeta y seleccionar un archivo
def check_folder_contents_and_select_file(folder_path):
    # Obtener la lista de archivos en el directorio
    files = os.listdir(folder_path)

    # Palabras clave a buscar
    keywords = ['autorregulacion', 'socioemocional', 'obs1', 'obs2', 'obs3', 'obs4']

    # Diccionario para almacenar los archivos encontrados que coinciden con las palabras clave
    found_files = {}

    # Verificar si algún archivo contiene las palabras clave
    for file in files:
        file_lower = file.lower()  # Convertir el nombre del archivo a minúsculas para hacer coincidencia de casos
        for keyword in keywords:
            if keyword.lower() in file_lower:
                # Agregar el archivo al diccionario si contiene la palabra clave
                if keyword not in found_files:
                    found_files[keyword] = []
                found_files[keyword].append(file)

    # Si no se encuentran archivos, retornar None
    if not found_files:
        return None

    # Mostrar los archivos encontrados y permitir al usuario seleccionar uno
    print("Se encontraron los siguientes archivos:")
    file_options = []
    for keyword, files in found_files.items():
        for file in files:
            file_options.append(file)
            print(f"{len(file_options)}. {file} (Palabra clave: {keyword})")

    # Pedir al usuario que seleccione un archivo
    while True:
        try:
            selection = int(input("Seleccione el número del archivo que desea usar: "))
            if 1 <= selection <= len(file_options):
                selected_file = file_options[selection - 1]
                print(f"Ha seleccionado: {selected_file}")
                return selected_file
            else:
                print("Por favor, seleccione un número válido.")
        except ValueError:
            print("Por favor, ingrese un número.")

# Ejemplo de uso
if __name__ == "__main__":
    folder_path = input("Ingrese la ruta de la carpeta: ")
    selected_file = check_folder_contents_and_select_file(folder_path)
    if selected_file:
        # Aquí puedes usar 'selected_file' como el 'path' para las funciones en 'funciones_ar_merge.py'
        pass
    else:
        print("No se encontraron archivos con las palabras clave especificadas.")














































































# import os

# # Función para verificar el contenido de la carpeta y seleccionar un archivo
# def check_folder_contents_and_select_file(folder_path):
#     # Obtener la lista de archivos en el directorio
#     files = os.listdir(folder_path)

#     # Palabras clave a buscar
#     keywords = ['autorregulacion', 'socioemocional', 'obs1', 'obs2', 'obs3', 'obs4']

#     # Diccionario para almacenar los archivos encontrados que coinciden con las palabras clave
#     found_files = {}

#     # Verificar si algún archivo contiene las palabras clave
#     for file in files:
#         file_lower = file.lower()  # Convertir el nombre del archivo a minúsculas para hacer coincidencia de casos
#         for keyword in keywords:
#             if keyword.lower() in file_lower:
#                 # Agregar el archivo al diccionario si contiene la palabra clave
#                 if keyword not in found_files:
#                     found_files[keyword] = []
#                 found_files[keyword].append(file)

#     # Si no se encuentran archivos, retornar None
#     if not found_files:
#         return None

#     # Mostrar los archivos encontrados y permitir al usuario seleccionar uno
#     print("Se encontraron los siguientes archivos:")
#     file_options = []
#     for keyword, files in found_files.items():
#         for file in files:
#             file_options.append(file)
#             print(f"{len(file_options)}. {file} (Palabra clave: {keyword})")

#     # Pedir al usuario que seleccione un archivo
#     while True:
#         try:
#             selection = int(input("Seleccione el número del archivo que desea usar: "))
#             if 1 <= selection <= len(file_options):
#                 selected_file = file_options[selection - 1]
#                 print(f"Ha seleccionado: {selected_file}")
#                 return selected_file
#             else:
#                 print("Por favor, seleccione un número válido.")
#         except ValueError:
#             print("Por favor, ingrese un número.")

# # Ejemplo de uso
# if __name__ == "__main__":
#     folder_path = input("Ingrese la ruta de la carpeta: ")
#     selected_file = check_folder_contents_and_select_file(folder_path)
#     if selected_file:
#         # Aquí puedes usar 'selected_file' como el 'path' para las funciones en 'funciones_ar_merge.py'
#         pass
#     else:
#         print("No se encontraron archivos con las palabras clave especificadas.")
