import pandas as pd
import streamlit as st
import pickle
from urllib.request import urlopen
import json

# load our best model
PATH = "C:/Users/DELL/Formation OC/Are you bankable/Datas/"

#Load Dataframe

X_test=pd.read_csv(PATH+'X_test.csv')
y_test=pd.read_csv(PATH+'y_test.csv')
dataframe=pd.read_csv(PATH+'df_test.csv')

# Main sections
header = st.container()
dataset= st.container()
features = st.container()
model_training = st.container()


with header:
    st.title("Make sure a client is a sure client!") 
    

    
with dataset:
    st.header("The train dataset is made of a selection of relevant features chosen after EDA")
    credit_data = dataframe
    st.write (credit_data.head())

with model_training:
   
       
    model_selection_column, display_column = st.columns(2)
    test_clients = pd.read_csv(PATH+'df_test.csv')
    liste_id = test_clients['SK_ID_CURR'].tolist()

     # Choose a client

    # chosen_client = str(model_selection_column.selectbox("Please chose your client ID", test_clients['SK_ID_CURR']))
    chosen_client = st.text_input('Veuillez saisir l\'identifiant d\'un client:', )

    st.success("client chosen")
    
    if chosen_client == '':
        st.write('Veuillez recommencer')
        
    elif (int(chosen_client) in liste_id) :
          
        # On peut appeler l'API
          
        API_url = "http://127.0.0.1:5000/credit/" + chosen_client
          
        with st.spinner('Attente du score du client choisi ...'):
            
          json_url = urlopen(API_url)
          
          API_data = json.loads(json_url.read())
          classe_predite = API_data["prediction"]
          if classe_predite == 1:
              resultat = "client dangereux"
          else:
              resultat = "client peu risqué"
          
          proba = 1- API_data["proba"]
          
          #affichage de la prédiction
          prediction = API_data['proba']
          # classe_reelle = dataframe[dataframe['SK_ID_CURR']==int(chosen_client)]['LABELS'].values[0]
          # classe_reelle = str(classe_reelle).replace('0', 'sans défaut').replace('1', 'avec défaut')
          chaine = 'Prédiction : **' + resultat +  '** avec **' + str(round(proba*100)) + '%** de risque d''erreur '

        st.markdown(chaine)