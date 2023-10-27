import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Downloads\\reviews.csv')

# Para verificar o numero total de avaliações e as primeiras avaliações que foram carregadas

print('The Number of reviews: ', len(df))
print(df[['title', 'rating']].head(10))

#Limpando os dados


#Dividindo e transformando os dados
#Precisamos transformar textos em vetores com a tecnica bag of words (BoW)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
reviews = df['title'].values
ratings = df['rating'].values
reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, ratings, test_size=0.2, random_state=1000)
vectorizer = CountVectorizer()
vectorizer.fit(reviews_train)
x_train = vectorizer.transform(reviews_train)
x_test= vectorizer.transform(reviews_test)

print(len(x_train.toarray()))

print(len(x_test.toarray()))

print(len(x_train.toarray()[0]))

print(x_train.toarray())

#Treinando o modelo usando o classificador LogisticRegression da scikit-learn

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

#Avaliando o modelo com o metodo predict()

import numpy as np
predicted = classifier.predict(x_test)
accuracy = np.mean(predicted == y_test)
print("Sccuracy:", round(accuracy,2))

#Criando uma matriz de confusão

from sklearn import metrics
print(metrics.confusion_matrix(y_test, predicted, labels = [1,2,3,4,5]))

#Contando as linhas de cada grupo de classificação

print(df.groupby('rating').size())

#Analisar as principais metricas de classificação com a função classification_report() encontrada no modulo metrics da scikit-learn

print(metrics.classification_report(y_test, predicted, labels = [1,2,3,4,5]))

