# Developer 1 - Parte 1
'''
Importamos librerías
'''
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Developer 1 - Parte 2
'''
Importamos librerías
'''
import pandas
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
st.set_option('deprecation.showPyplotGlobalUse', False)

# Developer 1 - Parte 3
'''
Cargamos los datos
'''
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

# Developer 2 - Parte 1
''' Hacemos Featuring Engineering '''
train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})
test_df['Sex'] = test_df['Sex'].map({'male': 0, 'female': 1})
train_df['Sex'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Sex'].fillna(test_df['Age'].mean(), inplace=True)

# Developer 2 - Parte 2
''' Hacemos Featuring Engineering '''
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Embarked'].fillna(test_df['Embarked'].mode()[0], inplace=True)

# Developer 2 - Parte 3
''' Hacemos Featuring Engineering '''
train_df['CabinBool'] = (train_df['Cabin'].notnull().astype('int'))
test_df['CabinBool'] = (test_df['Cabin'].notnull().astype('int')) train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'], prefix='Embarked')], axis=0)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')], axis=0)

# Developer 2 - Parte 4
''' Hacemos Featuring Engineering '''
train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'], prefix='Embarked')], axis=1)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')], axis=1)
test_df['Fare'].fillna(test_df['Fare'].dropna().mean(), inplace=True)

# Developer 3 - Parte 1
'''
Generamos Variables dependientes e independientes
'''
variables=['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'CabinBool', 'Embarked_C', 
'Embarked_S', 'Embarked_Q']
X = train_df[variables]
y = train_df['Survived']
# Developer 3 - Parte 2
'''
Creamos el modelo
'''
X = train_df[['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'CabinBool', 'Embarked_C', 
'Embarked_S', 'Embarked_Q]]
y = train_df[[Survived']]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=0)
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)
# Developer 3 - Parte 3
'''Hacemos predicciones'''
model.fit(X_train, y_val)
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
importances = 
pd.DataFrame({'feature':X_train.columns,'importance':np.round(model.feature_importan
ces_,3)})
importances = 
importances.sort_values('importance',ascending=False).set_index('feature')
# Developer 3 - Parte 4
'''
Visualizamos la variable Age
'''
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
train_df['AgeGroup'] = pd.cut(train_df['Age'], bins)
survived_age = train_df[train_df['Survived']==1]['AgeGroup'].value_counts(sort=False)
dead_age = train_df[train_df['Survived']==0]['AgeGroup'].value_counts(sort=False)
age_df = pd.DataFrame([survived_age,dead_age],index=['Survived','Dead'])
age_df.plot(kind='bar', stacked=True)
plt.xlabel('Age Group')
plt.ylabel('Number of passengers')
plt.title('Distribution of passengers by age and survival')
st.pyplot()

