from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

def home(request):
    return render(request, "home.html")
def predict(request):
    return render(request, "predict.html")
def result(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'static', 'USA_Housing.csv')
    data = pd.read_csv(file_path)

    # Remove the non-numeric 'Address' column
    X = data.drop(['Price', 'Address'], axis=1)
    Y = data['Price']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET.get('n1'))
    var2 = float(request.GET.get('n2'))
    var3 = float(request.GET.get('n3'))
    var4 = float(request.GET.get('n4'))
    var5 = float(request.GET.get('n5'))

    input_data = np.array([[var1, var2, var3, var4, var5]])
    prediction = model.predict(input_data)
    prediction = round(prediction[0])

    price = "The predicted price is $" + str(prediction)
    return render(request, "predict.html", {"result2": price})
