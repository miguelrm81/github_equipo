'''
Visualizamos la variable Clase
'''
survived_class = train_df[train_df['Survived']==1]['Pclass'].value_counts(sort=False) dead_class = train_df[train_df['Survived']==0]['Pclass'].value_counts(sort=False) class_df = pd.DataFrame([survived_class,dead_class],index=['Survived','Dead']) class_df.plot(kind='bar', stacked=True)
plt.xlabel('Class')
plt.ylabel('Number of passengers')
plt.title('Survival rate by class')
st.pyplot()


'''
Visualizamos la variable Sexo '''
survived_sex = train_df[train_df['Survived']==1]['Sex'].value_counts(sort=False) dead_sex = train_df[train_df['Survived']==0]['Sex'].value_counts(sort=False) sex_df = pd.DataFrame([survived_sex,dead_sex],index=['Survived','Dead']) sex_df.plot(kind='bar', stacked=True)
plt.xlabel('Sex')
plt.ylabel('Number of passengers') plt.title('Survival rate by sex') st.pyplot()


'''
Visualizamos la variable Embarked '''
survived_embark = train_df[train_df['Survived']==1]['Embarked'].value_counts(sort=False)
dead_embark = train_df[train_df['Survived']==0]['Embarked'].value_counts(sort=False) embark_df = pd.DataFrame([survived_embark,dead_embark],index=['Survived','Dead']) embark_df.plot(kind='bar', stacked=True)
plt.xlabel('Embarked')
plt.ylabel('Number of passengers')
plt.title('Survival rate by port of embarkation')
st.pyplot()


'''
Visualizamos la importancia de las variables
'''
survived_embark = train_df[train_df['Survived']==1]['Embarked'].value_counts(sort=True)
dead_embark = train_df[train_df['Survived']==0]['Embarked'].value_counts(sort=False) st.write('Visualización del modelo y datos')
st.write('Importancia de características en el modelo')
st.bar_chart(importances)