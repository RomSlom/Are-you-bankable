from flask import Flask, jsonify
# from joblib import load
import pandas as pd
# import joblib
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#  pour les raisons et les modalités https://docs.python.org/fr/3/library/warnings.html


app = Flask(__name__)


# X_test=pd.read_csv(PATH+'X_test.csv')
# y_test=pd.read_csv('./Datas/y_test.csv')
dataframe=pd.read_csv('./Datas/dFreduced.csv')
# dataframePartial = dataframe.sample(frac=0.05, axis = None)

# Chargement de notre meilleur modèle
# rb means "Read Binary format"
model = pickle.load(open('./Datas/model.pkl','rb'))


@app.route("/")
def hello():
    """
    Default route to display "Hello World!" message just to test we are good with flask :).
    """
    return "Hello World"


# @app.route("/credit/<id_client>", methods=['POST'])
# # on créer une route qui va afficher la prédiction client (id_client étant utilisé dans la fonction ci-dessous)
# #  Le client (streamlit) allant sur cette adresse  fait cette requête pour obtenir quelque chose (le return de la fonction).

# def credit(id_client):

#     # récupération id client depuis argument url    
#     # calcul prédiction défaut et probabilité de défaut

#     #  Conversion en integer de l'Id client
#     ID = int(id_client)   
    
# # récupération des données clients
#     X = dataframe[dataframe['SK_ID_CURR'] == ID]
#     X = X.drop(['TARGET', 'SK_ID_CURR'], axis=1)
    
#     prediction = model.predict(X)
    
#     y_probabiliste = model.predict_proba(X)
    
#     dict_final = {
#         'prediction' : int(prediction),
#         'proba' : float(y_probabiliste[0][0])
#         }

#     print('Nouvelle Prédiction : \n', dict_final)

#     return jsonify(dict_final)
    
    
    
if __name__ == "__main__":
    app.run()
    

