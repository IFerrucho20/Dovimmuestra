import os
from Dovim import load_and_process_data, process_data
from funciones_ar_merge import process_autorregulacion_data, load_sample_data, merge_and_filter_data
from checkfolder import check_folder_contents_and_select_file

def main():
    #Escoger la fecha que se pueda usar ejemplo dovim 12

    fecha = r'C:\Users\Hermanos Ferrucho\OneDrive - UWCOLOMBIA\Bases\Resultados instrumentos\Organizar Dovim\Dovim 12_2023'
    
    #Escoger la zona
    path_2 = r"C:\Users\Hermanos Ferrucho\OneDrive - UWCOLOMBIA\Bases\Muestras\2023\REGIONAL ANTIOQUIA"

    #Escoger la base de datos
    path_3 = r"C:\Users\Hermanos Ferrucho\OneDrive - UWCOLOMBIA\Bases\Muestras\2023\REGIONAL ANTIOQUIA\2. Nube9 Global-Kiwi\Kiwi Manizales\Muestreo_estratificado_personas_seleccionadas_2023-10-04.xlsx"


    # Usar la función para seleccionar un archivo basado en las palabras clave
    selected_file = check_folder_contents_and_select_file(fecha)
    if selected_file:

        path = os.path.join(fecha, selected_file)

        BD_ar = process_autorregulacion_data(path)
        print("BD_ar DataFrame:")
        print(BD_ar.head())  # Imprime las primeras filas de BD_ar para verificar

        df_dovim, _ = load_and_process_data(fecha)
        print("df_dovim DataFrame:")
        print(df_dovim.head())  # Imprime las primeras filas de df_dovim para verificar

        df_dovim_1 = process_data(fecha)
        print("df_dovim_1 DataFrame:")
        print(df_dovim_1.head())  # Imprime las primeras filas de df_dovim_1 para verificar

        sample = load_sample_data(path_2, path_3)
        print("sample DataFrame:")
        print(sample.head())  # Imprime las primeras filas de sample para verificar

        # Obtener los resultados fusionados y filtrados
        output_df = merge_and_filter_data(df_dovim_1, BD_ar, sample)
        print("output_df DataFrame:")
        print(output_df.head())  # Imprime las primeras filas de output_df para verificar


        # Imprimir los valores en una tabla
        print(output_df.to_markdown(index=False))

    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()











































































# import os
# from Dovim import load_and_process_data, process_data
# from funciones_ar_merge import process_autorregulacion_data, load_sample_data, merge_and_filter_data
# from checkfolder import check_folder_contents_and_select_file

# def main():
#     # Definir las rutas de los archivos
#     #Escoger la fecha que se pueda usar ejemplo dovim 12
#     fecha = r'C:\Users\Hermanos Ferrucho\OneDrive - UWCOLOMBIA\Bases\Resultados instrumentos\Organizar Dovim\Dovim 12_2023'
#     #Escoger la zona
#     path_2 = r"D:\United way colombia\Código de ejemplo DOVIM\REGIONAL SUROCCIDENTE"

#     #Escoger la base de datos
#     path_3 = r"D:\United way colombia\Código de ejemplo DOVIM\Levapan\Muestreo_estratificado_personas_seleccionadas_2023-08-08.xlsx"

#     # Usar la función para seleccionar un archivo basado en las palabras clave
#     selected_file = check_folder_contents_and_select_file(fecha)
#     if selected_file:
#         # Construir la ruta completa al archivo seleccionado
#         path = os.path.join(fecha, selected_file)

#         BD_ar = process_autorregulacion_data(path)
#         print("BD_ar DataFrame:")
#         print(BD_ar.head())  # Imprime las primeras filas de BD_ar para verificar

#         df_dovim, _ = load_and_process_data(fecha)
#         print("df_dovim DataFrame:")
#         print(df_dovim.head())  # Imprime las primeras filas de df_dovim para verificar

#         df_dovim_1 = process_data(fecha)
#         print("df_dovim_1 DataFrame:")
#         print(df_dovim_1.head())  # Imprime las primeras filas de df_dovim_1 para verificar

#         sample = load_sample_data(path_2, path_3)
#         print("sample DataFrame:")
#         print(sample.head())  # Imprime las primeras filas de sample para verificar

#         # Obtener los resultados fusionados y filtrados
#         output_df = merge_and_filter_data(df_dovim_1, BD_ar, sample)
#         print("output_df DataFrame:")
#         print(output_df.head())  # Imprime las primeras filas de output_df para verificar


#         # Imprimir los valores en una tabla
#         print(output_df.to_markdown(index=False))

#     else:
#         print("No se seleccionó ningún archivo.")

# if __name__ == "__main__":
#     main()


