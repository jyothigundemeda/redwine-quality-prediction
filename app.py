from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
with open('label_encoder.pkl', 'rb') as f:
    model = pickle.load(f)
# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
# Route to handle  form submission
# Route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Load the model and label encoder from pickle within the function
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    with open('label_encoder.pkl', 'rb') as f:
        loaded_label_encoder = pickle.load(f)

    if request.method == 'POST':
        ph = float(request.form['ph'])
        alcohol = float(request.form['alcohol'])
        
        # Use the loaded model to make predictions
        input_features = [[ph, alcohol]]
        predicted_label = loaded_model.predict(input_features)
        
        # Inverse transform the predicted label to get the quality label
        predicted_quality = loaded_label_encoder.inverse_transform(predicted_label)[0]
        
        return render_template('index.html', predicted_quality=predicted_quality)


if __name__ == '__main__':
    app.run(debug=True)
