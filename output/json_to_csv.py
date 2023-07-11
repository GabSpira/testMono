import pandas as pd
import json
import os
import dataframe_image as dfi


# # Carica il file JSON
with open('./output/exportedData3.json', 'r') as file:
    data = json.load(file)


# user_data = data[0]['userData']

# # Estrai i dati da userRatings
# user_ratings = data[0]['userRatings']


results_data = []

# Itera attraverso i risultati nel file JSON
for result in data:
    user_data = result['userData']
    user_ratings = result['userRatings']

    # Crea un dizionario per i dati del risultato corrente
    result_data = user_data.copy()

    # Aggiungi i dati di userRatings al dizionario del risultato
    for rating in user_ratings:
        rhythm = rating['rhythm']
        score = rating['score']
        result_data[rhythm] = score

    # Aggiungi il dizionario del risultato alla lista dei risultati
    results_data.append(result_data)

# Crea il DataFrame dai dati dei risultati
df = pd.DataFrame.from_records(results_data)
df = df.transpose()

print(df)


df_styled = df.head(200).style.set_properties(**{'background-color': '#fee68f',
                                                            'color': '#830340',
                                                            'border-color': 'blue',
                                                            'align': 'center'})
                                            #                 \
                                            # .format({"Loudness": "{:20,.0f} dB"})
df_styled = df_styled.set_caption("Features of the selected song")

#export dataframe
# os.makedirs('./output/Images', exist_ok=False)
dfi.export(df_styled, './output/Images/test3_DataFrame.png', max_cols=-1)