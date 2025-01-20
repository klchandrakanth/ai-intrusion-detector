import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from preprocess import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data()

def build_model():
    model = Sequential([
        LSTM(64, input_shape=(X_train.shape[1], 1), activation='relu', return_sequences=True),
        Dropout(0.2),
        LSTM(32, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = build_model()

# Reshape the data
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

# Save the trained model
model.save("models/intrusion_detection_model.h5")
print("Model training completed and saved to models/intrusion_detection_model.h5")

