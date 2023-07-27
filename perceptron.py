import numpy as np


class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def predict(self, inputs):
        net_input = np.dot(inputs, self.weights) + self.bias
        return 1 if net_input >= 0 else 0

    def train(self, inputs, targets, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for input_data, target in zip(inputs, targets):
                prediction = self.predict(input_data)
                error = target - prediction
                self.weights += learning_rate * error * input_data
                self.bias += learning_rate * error


# Example usage:
if __name__ == "__main__":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([0, 0, 0, 1])

    perceptron = Perceptron(input_size=2)
    perceptron.train(inputs, targets)

    # Test the trained perceptron
    for input_data in inputs:
        prediction = perceptron.predict(input_data)
        print(f"Input: {input_data}, Prediction: {prediction}")