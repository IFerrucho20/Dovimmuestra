####BLOQUE 1  
# fecha: Es una ruta que define el directorio donde se
# encuentran los archivos de datos para la función
# load_and_process_data. Se utiliza para cargar y procesar 
# los datos de los archivos Excel especificados en el
# diccionario base_files. 


import pandas as pd
# Function for missing values summary
def missing_summary(data):
    missing_counts = data.isnull().sum()
    missing_percents = round(missing_counts / len(data) * 100, 2)
    missing_data = pd.DataFrame({
        'Variable': data.columns,
        'Missing': missing_counts,
        'Percent': missing_percents
    })
    return missing_data

def load_and_process_data(fecha):
    base_files = {
        "Beneficiarios": "registros_unicos.xlsx",
        "Formacion": "registros_formacion.xlsx",
        "Asistencias": "registros_asistencias.xlsx",
        "Comunicaciones": "registros_comunicacion.xlsx",
        "Satisfaccion": "registros_satisfaccion.xlsx",
        "Programas": "registros_programas.xlsx"
    }

    # Load dataframes
    dfs = {key: pd.read_excel(fecha + '/' + file) for key, file in base_files.items()}

    # Remove unwanted column from Programas dataframe
    Programas = dfs["Programas"].drop(columns=[14], errors='ignore')

    # Merge dataframes
    df_dovim = pd.merge(dfs["Formacion"], dfs["Asistencias"], on='idmatricula', how='outer', indicator='merge_for_asis')
    df_ben_com = dfs['Beneficiarios'].merge(dfs['Comunicaciones'], on='documento', how='outer', indicator='ben_com')
    df_dovim = df_dovim.merge(df_ben_com, on='documento', how='outer', indicator='dov_intrm')
    df_dovim = df_dovim.merge(Programas, on='programa', how='outer', indicator='merge_final')

    # Generate missing summary
    missing_complete = missing_summary(df_dovim)

    df_dovim.dropna(subset=['documento', 'programa'], inplace=True)

    return df_dovim, missing_complete  # Return both the processed dataframe and the missing summary

# Asegúrate de que los nombres de las columnas en relevant_columns sean exactamente los mismos
# que los nombres de las columnas en el DataFrame df_dovim

def filter_data(df):
    # relevant_columns = [
    #     'documento', 'programa', 'solucion', 'regional', 'nombres', 'apellidos',
    #     'convocatoria', 'grupo', 'departamento', 'ciudad', 'ubicacioninstitucion',
    #     'tipoinstitucion', 'institucion', 'cargo', 'edades', 'formacion', 'sexoinscrito'
    # ]
    ##SE CAMBIO PO RQUE PARECE QUE NO ENCONTRABA TODAS LAS COLUMNAS  COMO TIPOINSTIUTCION, , EDADES, FORMACIÓN
    #pase de tipoinstitucion a idinstitucion
    relevant_columns = [
    'documento', 'programa', 'solucion', 'regional', 'nombres', 'apellidos',
    'convocatoria', 'grupo', 'departamento', 'ciudad', 'ubicacioninstitucion',
    'institucion', 'cargo', 'sexoinscrito', 'edades', 'idinstitucion', 'formacion'
]


    # Asegúrate de que todas las columnas listadas existan en el DataFrame
    assert all(column in df.columns for column in relevant_columns), "Una o más columnas relevantes no se encuentran en el DataFrame."

    # Filtrar por vigencia 2023 y excluir 'Eventos UWC'
    df_filtered = df[(df['vigencia'] == 2023) & (df['ruta'] != 'Eventos UWC')]

    # Seleccionar columnas relevantes
    df_filtered = df_filtered[relevant_columns]

    # Eliminar duplicados
    df_filtered = df_filtered.drop_duplicates(subset=['documento'], keep='first')

    # Modificar valores en la columna 'sexoinscrito'
    df_filtered['sexoinscrito'] = df_filtered['sexoinscrito'].replace({'Mujer': 'mujer', 'Hombre': 'hombre', '1': 'hombre'})

    return df_filtered

def process_data(fecha):
    df_dovim, _ = load_and_process_data(fecha)
    print("Columnas en df_dovim:", df_dovim.columns.tolist())
    df_dovim_filtered = filter_data(df_dovim)
    return df_dovim_filtered




























































































# ####BLOQUE 1  
# # fecha: Es una ruta que define el directorio donde se
# # encuentran los archivos de datos para la función
# # load_and_process_data. Se utiliza para cargar y procesar 
# # los datos de los archivos Excel especificados en el
# # diccionario base_files. 


# import pandas as pd
# # Function for missing values summary
# def missing_summary(data):
#     missing_counts = data.isnull().sum()
#     missing_percents = round(missing_counts / len(data) * 100, 2)
#     missing_data = pd.DataFrame({
#         'Variable': data.columns,
#         'Missing': missing_counts,
#         'Percent': missing_percents
#     })
#     return missing_data

# def load_and_process_data(fecha):
#     base_files = {
#         "Beneficiarios": "registros_unicos.xlsx",
#         "Formacion": "registros_formacion.xlsx",
#         "Asistencias": "registros_asistencias.xlsx",
#         "Comunicaciones": "registros_comunicacion.xlsx",
#         "Satisfaccion": "registros_satisfaccion.xlsx",
#         "Programas": "registros_programas.xlsx"
#     }

#     # Load dataframes
#     dfs = {key: pd.read_excel(fecha + '/' + file) for key, file in base_files.items()}

#     # Remove unwanted column from Programas dataframe
#     Programas = dfs["Programas"].drop(columns=[14], errors='ignore')

#     # Merge dataframes
#     df_dovim = pd.merge(dfs["Formacion"], dfs["Asistencias"], on='idmatricula', how='outer', indicator='merge_for_asis')
#     df_ben_com = dfs['Beneficiarios'].merge(dfs['Comunicaciones'], on='documento', how='outer', indicator='ben_com')
#     df_dovim = df_dovim.merge(df_ben_com, on='documento', how='outer', indicator='dov_intrm')
#     df_dovim = df_dovim.merge(Programas, on='programa', how='outer', indicator='merge_final')

#     # Generate missing summary
#     missing_complete = missing_summary(df_dovim)

#     df_dovim.dropna(subset=['documento', 'programa'], inplace=True)

#     return df_dovim, missing_complete  # Return both the processed dataframe and the missing summary

# # Asegúrate de que los nombres de las columnas en relevant_columns sean exactamente los mismos
# # que los nombres de las columnas en el DataFrame df_dovim

# def filter_data(df):
#     # relevant_columns = [
#     #     'documento', 'programa', 'solucion', 'regional', 'nombres', 'apellidos',
#     #     'convocatoria', 'grupo', 'departamento', 'ciudad', 'ubicacioninstitucion',
#     #     'tipoinstitucion', 'institucion', 'cargo', 'edades', 'formacion', 'sexoinscrito'
#     # ]
#     ##SE CAMBIO PO RQUE PARECE QUE NO ENCONTRABA TODAS LAS COLUMNAS  COMO TIPOINSTIUTCION, , EDADES, FORMACIÓN
#     #pase de tipoinstitucion a idinstitucion
#     relevant_columns = [
#     'documento', 'programa', 'solucion', 'regional', 'nombres', 'apellidos',
#     'convocatoria', 'grupo', 'departamento', 'ciudad', 'ubicacioninstitucion',
#     'institucion', 'cargo', 'sexoinscrito', 'edades', 'idinstitucion', 'formacion'
# ]


#     # Asegúrate de que todas las columnas listadas existan en el DataFrame
#     assert all(column in df.columns for column in relevant_columns), "Una o más columnas relevantes no se encuentran en el DataFrame."

#     # Filtrar por vigencia 2023 y excluir 'Eventos UWC'
#     df_filtered = df[(df['vigencia'] == 2023) & (df['ruta'] != 'Eventos UWC')]

#     # Seleccionar columnas relevantes
#     df_filtered = df_filtered[relevant_columns]

#     # Eliminar duplicados
#     df_filtered = df_filtered.drop_duplicates(subset=['documento'], keep='first')

#     # Modificar valores en la columna 'sexoinscrito'
#     df_filtered['sexoinscrito'] = df_filtered['sexoinscrito'].replace({'Mujer': 'mujer', 'Hombre': 'hombre', '1': 'hombre'})

#     return df_filtered

# def process_data(fecha):
#     df_dovim, _ = load_and_process_data(fecha)
#     print("Columnas en df_dovim:", df_dovim.columns.tolist())
#     df_dovim_filtered = filter_data(df_dovim)
#     return df_dovim_filtered












