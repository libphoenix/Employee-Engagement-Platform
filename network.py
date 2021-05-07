from tensorflow import keras 
import numpy as np


# model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])


# model.compile(optimizer = "sgd" , loss = "mean_squared_error")

# ip = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
# label = np.array ([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

# model.fit(ip, label, epochs = 500)

# model.save("simple.pb")

saved_model = keras.models.load_model("simple.pb")
print(saved_model.predict([10]))
