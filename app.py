from flask import Flask, render_template, url_for, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("menu.html")

@app.route("/predictor",methods=["POST","GET"])
def predictor():
    def predictor(array, clase):
        df = pd.read_csv('dataset/data_features.csv')
        df1 = pd.read_csv('dataset/data_'+str(clase)+'.csv')
        # Drop the animal names since this is not a good feature to split the data on
        dataset = df.drop("ESPECIE", axis=1)
        # Split the data into features and target
        features = dataset.drop('FAMILIA', axis=1)
        targets = dataset['FAMILIA']
        # Split the data into a training and a testing set
        train_features, test_features, train_targets, test_targets = train_test_split(features, targets, train_size=0.80)
        # Train the model
        tree= DecisionTreeClassifier(criterion="entropy")
        tree= tree.fit(train_features, train_targets)
        # Make prediction
        features = pd.DataFrame(data=None,columns=df.columns ).drop(['ESPECIE','FAMILIA'], axis=1)
        features.loc[len(df)] = array
        prediction = tree.predict(features)[0]
        # Obtain species
        species = df1.loc[df1['FAMILIA'].apply(lambda x: x.lower()) == prediction]
        return species

    if request.method == 'POST':
        
        clase = request.form['clase']
        theria = int(request.form['theria']) if request.form['theria'] != "" else 0 
        eutheria = int(request.form['eutheria']) if request.form['eutheria'] != "" else 0 
        metatheria = int(request.form['metatheria']) if request.form['metatheria'] != "" else 0 
        neognathae = int(request.form['neognathae']) if request.form['neognathae'] != "" else 0 
        paleognathae = int(request.form['paleognathae']) if request.form['paleognathae'] != "" else 0 
        carnivora = int(request.form['carnivora']) if request.form['carnivora'] != "" else 0 
        artiodactyla = int(request.form['artiodactyla']) if request.form['artiodactyla'] != "" else 0 
        rodentia = int(request.form['rodentia']) if request.form['rodentia'] != "" else 0 
        chiroptera = int(request.form['chiroptera']) if request.form['chiroptera'] != "" else 0 
        cingulata = int(request.form['cingulata']) if request.form['cingulata'] != "" else 0 
        primates = int(request.form['primates']) if request.form['primates'] != "" else 0 
        perissodactyla = int(request.form['perissodactyla']) if request.form['perissodactyla'] != "" else 0 
        didelphimorphia = int(request.form['didelphimorphia']) if request.form['didelphimorphia'] != "" else 0 
        lagomorpha = int(request.form['lagomorpha']) if request.form['lagomorpha'] != "" else 0 
        paucituberculata = int(request.form['paucituberculata']) if request.form['paucituberculata'] != "" else 0 
        pilosa = int(request.form['pilosa']) if request.form['pilosa'] != "" else 0 
        apodiformes = int(request.form['apodiformes']) if request.form['apodiformes'] != "" else 0 
        tinamiformes = int(request.form['tinamiformes']) if request.form['tinamiformes'] != "" else 0 
        anseriformes = int(request.form['anseriformes']) if request.form['anseriformes'] != "" else 0 
        galliformes = int(request.form['galliformes']) if request.form['galliformes'] != "" else 0 
        phoenicopteriformes = int(request.form['phoenicopteriformes']) if request.form['phoenicopteriformes'] != "" else 0 
        podicipediformes = int(request.form['podicipediformes']) if request.form['podicipediformes'] != "" else 0 
        columbiformes = int(request.form['columbiformes']) if request.form['columbiformes'] != "" else 0 
        cuculiformes = int(request.form['cuculiformes']) if request.form['cuculiformes'] != "" else 0 
        caprimulgiformes = int(request.form['caprimulgiformes']) if request.form['caprimulgiformes'] != "" else 0 
        opisthocomiformes = int(request.form['opisthocomiformes']) if request.form['opisthocomiformes'] != "" else 0 
        gruiformes = int(request.form['gruiformes']) if request.form['gruiformes'] != "" else 0 
        charadriiformes = int(request.form['charadriiformes']) if request.form['charadriiformes'] != "" else 0 
        sphenisciformes = int(request.form['sphenisciformes']) if request.form['sphenisciformes'] != "" else 0 
        procellariiformes = int(request.form['procellariiformes']) if request.form['procellariiformes'] != "" else 0 
        ciconiiformes = int(request.form['ciconiiformes']) if request.form['ciconiiformes'] != "" else 0 
        strigiformes = int(request.form['strigiformes']) if request.form['strigiformes'] != "" else 0 
        trogoniformes = int(request.form['trogoniformes']) if request.form['trogoniformes'] != "" else 0 
        coraciiformes = int(request.form['coraciiformes']) if request.form['coraciiformes'] != "" else 0 
        galbuliformes = int(request.form['galbuliformes']) if request.form['galbuliformes'] != "" else 0 
        falconiformes = int(request.form['falconiformes']) if request.form['falconiformes'] != "" else 0 
        psittaciformes = int(request.form['psittaciformes']) if request.form['psittaciformes'] != "" else 0 

        array = []
        array.append(theria)
        array.append(eutheria)
        array.append(metatheria)
        array.append(neognathae)
        array.append(paleognathae)
        array.append(carnivora)
        array.append(artiodactyla)
        array.append(rodentia)
        array.append(chiroptera)
        array.append(cingulata)
        array.append(primates)
        array.append(perissodactyla)
        array.append(didelphimorphia)
        array.append(lagomorpha)
        array.append(paucituberculata)
        array.append(pilosa)
        array.append(apodiformes)
        array.append(tinamiformes)
        array.append(anseriformes)
        array.append(galliformes)
        array.append(phoenicopteriformes)
        array.append(podicipediformes)
        array.append(columbiformes)
        array.append(cuculiformes)
        array.append(caprimulgiformes)
        array.append(opisthocomiformes)
        array.append(gruiformes)
        array.append(charadriiformes)
        array.append(sphenisciformes)
        array.append(procellariiformes)
        array.append(ciconiiformes)
        array.append(strigiformes)
        array.append(trogoniformes)
        array.append(coraciiformes)
        array.append(galbuliformes)
        array.append(falconiformes)
        array.append(psittaciformes)

        df = predictor(array, clase)
        return render_template("predictor.html", tables=[df.to_html(classes="table table-dark", header="true")])
    else:
        return render_template("predictor.html")
    

@app.route("/clasificador",methods=["POST"])
def clasificador():
    return render_template("clasificador.html")


if __name__ == "__main__" :
    app.run(debug=True)