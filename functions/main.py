
# from firebase_admin import firestore
# from flask import Flask, request

# app = Flask(__name__)


# @app.route('/salva-risposta-test', methods=['POST'])
# def salva_risposta_test():
    
#     dati_risposta = request.get_json()  # I dati delle risposte inviate dall'utente

#     try:
#         db = firestore.client()
#         risultato = db.collection('results').add(dati_risposta)
#         print('Risposta del test salvata con ID:', risultato[1].id)
#         return 'Risposta del test salvata correttamente', 200
#     except Exception as e:
#         print('Errore nel salvataggio della risposta del test:', e)
#         return 'Errore nel salvataggio della risposta del test', 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import jsonify
from google.cloud import firestore

def create_results_collection():
    db = firestore.Client()
    collection_ref = db.collection('results')

    # Verifica se la collezione "results" esiste già
    if not collection_ref.get():
        # Crea la collezione "results"
        collection_ref.create()

def salva_risposta_test(request):
    create_results_collection()  # Crea la collezione "results" se non esiste

    db = firestore.Client()
    collection_ref = db.collection('results')

    try:
        dati_risposta = request.get_json()  # I dati delle risposte inviate dall'utente

        # Salva i dati delle risposte nella collezione "results"
        risultato = collection_ref.add(dati_risposta)
        print('Risposta del test salvata con ID:', risultato[1].id)
        return 'Risposta del test salvata correttamente', 200
    except Exception as e:
        print('Errore nel salvataggio della risposta del test:', e)
        return 'Errore nel salvataggio della risposta del test', 500
