from src.train_model import build_model, X_train, X_test, y_train, y_test

def main():
    model = build_model()
    X_train_reshaped = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    model.fit(X_train_reshaped, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))
    model.save("models/intrusion_detection_model.h5")
    print("Training completed and model saved.")

if __name__ == "__main__":
    main()

