from sklearn.neural_network import MLPClassifier

# Temperature, Humidity
X=[
    [20,80],
    [25,70],
    [30,50],
    [35,40],
    [22,85],
    [28,60]
]

# 1 = Rain
# 0 = No Rain
Y=[1,1,0,0,1,0]

model=MLPClassifier(hidden_layer_sizes=(4,),
                    max_iter=5000,
                    random_state=1)

model.fit(X,Y)

weather=[[24,75]]

prediction=model.predict(weather)[0]

if prediction==1:
    print("Rain Expected")
else:
    print("No Rain")