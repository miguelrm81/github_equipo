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