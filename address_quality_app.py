from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('./model/address_quality_model_gradient_boosting.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the column names
with open('./model/X_columns_gradient_boosting.pkl', 'rb') as f:
    feature_columns = pickle.load(f)

def preprocess_input_data(address, city, state, pincode):
    # Creating a DataFrame from the input data
    df_new = pd.DataFrame([[address, city, state, pincode]], columns=['address', 'city', 'state', 'pincode'])
    
    # Apply the same preprocessing as done during training
    df_new = pd.get_dummies(df_new, drop_first=True)
    df_new = df_new.reindex(columns=feature_columns, fill_value=0)  # Align with the training data features
    
    return df_new

@app.route('/address_quality', methods=['POST'])
def predict():
    data = request.get_json()
    address_columns = ['address', 'city', 'state', 'pincode']
    
    # basic checks
    if not all(field in data for field in address_columns):
        return jsonify({'Error': 'Missing fields in request'}), 400

    
    # Extracting the necessary fields from the request data
    address = data.get('address')
    city = data.get('city')
    state = data.get('state')
    pincode = data.get('pincode')
    
    # checks for validation
    if not isinstance(address, str) or not address.strip():
        return jsonify({'Error': 'Invalid address'}), 400
    if not isinstance(city, str) or not city.strip():
        return jsonify({'Error': 'Invalid city'}), 400
    if not isinstance(state, str) or not state.strip():
        return jsonify({'Error': 'Invalid state'}), 400
    if not isinstance(pincode, str) or not pincode.strip() or len(pincode) != 6 or not pincode.isdigit():
        return jsonify({'Error': 'Invalid pincode'}), 400

    # Prepare the input data in the required format
    input_features = preprocess_input_data(address, city, state, pincode)
    
    # Making prediction
    prediction = model.predict(input_features)

    # Returning the prediction result
    return jsonify({'address_quality': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
