####BLOQUE 2  
# path: Es una ruta para cargar un archivo Excel específico
# y luego renombrar columnas y realizar operaciones
# de limpieza de datos.  


import pandas as pd
import os

def process_autorregulacion_data(path):
    # Importar y renombrar columnas
    BD_ar = pd.read_excel(path)
    BD_ar = BD_ar.rename(columns={
        'Documento de identidad del niño o la niña (El mismo que se registró en la convocatoria o hizo la inscripción al programa)': 'documento',
        'Solución educativa a la que pertenece.': 'solucion_pc',
        'Por favor determine que formulario desea diligenciar': 'formulario',
        'Seleccione su vínculo con el niño o la niña': 'vinculo'
    })

    # Convertir los datos de la columna 'documento' en numéricos
    BD_ar['documento'] = pd.to_numeric(BD_ar['documento'], errors='coerce')

    # Crear marca temporal y columna de mes
    BD_ar['Marca temporal'] = pd.to_datetime(BD_ar['Marca temporal'])
    BD_ar['Mes'] = BD_ar['Marca temporal'].dt.month

    # Reemplazar valores faltantes en 'solucion_pc' por 'Otra'
    BD_ar['solucion_pc'] = BD_ar['solucion_pc'].fillna('Otra')

    # Eliminar duplicados
    BD_ar = BD_ar.sort_values(by='Marca temporal').drop_duplicates(subset=['documento', 'vinculo', 'solucion_pc', 'formulario'], keep='first')

    return BD_ar



def load_sample_data(path_2, path_3):
    sample = pd.read_excel(os.path.join(path_2, path_3))
    return sample



def merge_and_filter_data(df_dovim_1, BD_ar, sample):
    df_final = df_dovim_1.merge(BD_ar, how='left', on='documento', indicator='_merge_dovim')
    df_final = df_final[df_final['_merge_dovim'] == 'both']
    df_final = df_final[df_final['programa'] == 'Nube 9 Kiwi Levapan']
    df_final = df_final[df_final['formulario'] == 'Entrada']
    df_final.drop_duplicates(subset='documento', inplace=True)

    output_1df = sample.merge(df_final, on='documento', how='left', indicator='_merge_sample')
    output_1df = output_1df['_merge_sample'].groupby(output_1df['_merge_sample']).size().reset_index(name='Frecuencia')

    output_1df['Tipo de coincidencia'] = output_1df['_merge_sample'].replace({
        'left_only': 'Solo en muestra',
        'both': 'Coincidencia de muestra con instrumento+Dovim',
        'right_only': 'Solo en instrumento + Dovim'
    })

    total_count = output_1df['Frecuencia'].sum()
    output_1df['Porcentaje'] = (output_1df['Frecuencia'] / total_count) * 100

    # Seleccionar solo las columnas deseadas
    output_1df = output_1df[['Tipo de coincidencia', 'Frecuencia', 'Porcentaje']]

    # Verificar si el porcentaje de coincidencia es mayor al 80%
    if output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Porcentaje'].values[0] > 80:
        print("El porcentaje de coincidencia aprobó porque tiene una coincidencia mayor del 80% con una frecuencia de", output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Frecuencia'].values[0])

    else:
        print("Tocaría revisar los datos porque no existe una coincidencia mínima del 80% y su frecuencia es de", output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Frecuencia'].values[0])

    return output_1df



































































# ####BLOQUE 2  
# # path: Es una ruta para cargar un archivo Excel específico
# # y luego renombrar columnas y realizar operaciones
# # de limpieza de datos.  


# import pandas as pd
# import os

# def process_autorregulacion_data(path):
#     # Importar y renombrar columnas
#     BD_ar = pd.read_excel(path)
#     BD_ar = BD_ar.rename(columns={
#         'Documento de identidad del niño o la niña (El mismo que se registró en la convocatoria o hizo la inscripción al programa)': 'documento',
#         'Solución educativa a la que pertenece.': 'solucion_pc',
#         'Por favor determine que formulario desea diligenciar': 'formulario',
#         'Seleccione su vínculo con el niño o la niña': 'vinculo'
#     })

#     # Convertir los datos de la columna 'documento' en numéricos
#     BD_ar['documento'] = pd.to_numeric(BD_ar['documento'], errors='coerce')

#     # Crear marca temporal y columna de mes
#     BD_ar['Marca temporal'] = pd.to_datetime(BD_ar['Marca temporal'])
#     BD_ar['Mes'] = BD_ar['Marca temporal'].dt.month

#     # Reemplazar valores faltantes en 'solucion_pc' por 'Otra'
#     BD_ar['solucion_pc'] = BD_ar['solucion_pc'].fillna('Otra')

#     # Eliminar duplicados
#     BD_ar = BD_ar.sort_values(by='Marca temporal').drop_duplicates(subset=['documento', 'vinculo', 'solucion_pc', 'formulario'], keep='first')

#     return BD_ar



# def load_sample_data(path_2, path_3):
#     sample = pd.read_excel(os.path.join(path_2, path_3))
#     return sample



# def merge_and_filter_data(df_dovim_1, BD_ar, sample):
#     df_final = df_dovim_1.merge(BD_ar, how='left', on='documento', indicator='_merge_dovim')
#     df_final = df_final[df_final['_merge_dovim'] == 'both']
#     df_final = df_final[df_final['programa'] == 'Nube 9 Kiwi Levapan']
#     df_final = df_final[df_final['formulario'] == 'Entrada']
#     df_final.drop_duplicates(subset='documento', inplace=True)

#     output_1df = sample.merge(df_final, on='documento', how='left', indicator='_merge_sample')
#     output_1df = output_1df['_merge_sample'].groupby(output_1df['_merge_sample']).size().reset_index(name='Frecuencia')

#     output_1df['Tipo de coincidencia'] = output_1df['_merge_sample'].replace({
#         'left_only': 'Solo en muestra',
#         'both': 'Coincidencia de muestra con instrumento+Dovim',
#         'right_only': 'Solo en instrumento + Dovim'
#     })

#     total_count = output_1df['Frecuencia'].sum()
#     output_1df['Porcentaje'] = (output_1df['Frecuencia'] / total_count) * 100

#     # Seleccionar solo las columnas deseadas
#     output_1df = output_1df[['Tipo de coincidencia', 'Frecuencia', 'Porcentaje']]

#     # Verificar si el porcentaje de coincidencia es mayor al 80%
#     if output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Porcentaje'].values[0] > 80:
#         print("El porcentaje de coincidencia aprobó porque tiene una coincidencia mayor del 80% con una frecuencia de", output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Frecuencia'].values[0])

#     else:
#         print("Tocaría revisar los datos porque no existe una coincidencia mínima del 80% y su frecuencia es de", output_1df.loc[output_1df['Tipo de coincidencia'] == 'Coincidencia de muestra con instrumento+Dovim', 'Frecuencia'].values[0])

#     return output_1df














