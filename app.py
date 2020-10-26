from flask import Flask, render_template, url_for, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    def predictor(array):
        df = pd.read_csv('dataset/data_features.csv')
        # Drop the animal names since this is not a good feature to split the data on
        dataset = df.drop("ESPECIE", axis=1)
        # Split the data into features and target
        features = dataset.drop('FAMILIA', axis=1)
        targets = dataset['FAMILIA']
        # Split the data into a training and a testing set
        train_features, test_features, train_targets, test_targets = train_test_split(features, targets, train_size=0.75)
        # Train the model
        tree= DecisionTreeClassifier(criterion="entropy")
        tree= tree.fit(train_features, train_targets)
        # Make prediction
        features = pd.DataFrame(data=None,columns=df.columns).drop(['ESPECIE','FAMILIA'], axis=1)
        features.loc[len(df)] = array
        prediction = tree.predict(features)[0]
        return prediction

    array= [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    predictor(array)
    if request.method == 'POST':
        clase = request.form['clase']
        subclase = request.form['subclase']
        infraclase = request.form['infraclase']
        orden = request.form['orden']
        superorden = request.form['superorden']
                                        
        result = predictor(array)
        return render_template('index.html', result = result)
    else:
        return render_template('index.html')
if __name__ == "__main__" :
    app.run(debug=True)