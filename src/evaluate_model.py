import tensorflow as tf
from preprocess import load_and_preprocess_data

def evaluate_model():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    model = tf.keras.models.load_model("models/intrusion_detection_model.h5")

    # Reshape test data
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    evaluate_model()

