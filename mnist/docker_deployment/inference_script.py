from flask import Flask, request, jsonify
import torch
import torch.nn as nn

# Define the model architecture (same as in training)
class MNISTNN(nn.Module):
    def __init__(self):
        super(MNISTNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(28 * 28, 128),  # 28*28 input features (flattened image)
            nn.ReLU(),
            nn.Linear(128, 64),       # Hidden layer with 64 neurons
            nn.ReLU(),
            nn.Linear(64, 10),        # 10 output classes (digits 0-9)
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        x = x.view(-1, 28 * 28)     # Flatten the image
        return self.fc(x)

# Load the model and set it to evaluation mode
model = MNISTNN()
model.load_state_dict(torch.load("model_weights.pth"))
model.eval()

# Create a Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the request
    data = request.get_json()
    input_data = torch.FloatTensor(data["input"])

    # Run inference
    with torch.no_grad():
        output = model(input_data)
        _, predicted_class = torch.max(output, 1)
    
    # Return the results as JSON
    return jsonify({"predicted_class": predicted_class.item()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
