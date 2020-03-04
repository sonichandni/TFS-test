# import load_model
# print("hi")
from tensorflow.keras.models import load_model
# print("d")
# give the path to model directory to load the model
loaded_model = load_model('my_model/1/')

# predict function to predict the probabilities for each class 0-9
loaded_model.predict(test_images[0:1])

# predict_classes to get the class with highest probability 
loaded_model.predict_classes(test_images[0:1])