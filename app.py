from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def diagnose_maize(symptoms):
    if "yellow spots" in symptoms and "leaf blight" in symptoms:
        return "Northern Leaf Blight - Apply fungicide treatment."
    elif "gray lesions" in symptoms:
        return "Gray Leaf Spot - Use resistant maize varieties."
    elif "wilting stalks" in symptoms:
        return "Stalk Rot - Improve soil drainage."
    else:
        return "No disease detected or insufficient data."

def diagnose_coffee(symptoms):
    if "orange spores" in symptoms:
        return "Coffee Leaf Rust - Apply copper-based fungicide."
    elif "dark lesions on berries" in symptoms:
        return "Coffee Berry Disease - Use resistant coffee plants."
    elif "wilting leaves" in symptoms:
        return "Fusarium Wilt - Use proper crop rotation."
    else:
        return "No disease detected or insufficient data."

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    crop = data.get('crop')
    symptoms = data.get('symptoms', [])

    if crop == "maize":
        result = diagnose_maize(symptoms)
    elif crop == "coffee":
        result = diagnose_coffee(symptoms)
    else:
        result = "Invalid crop selection."

    return jsonify({"diagnosis": result})

# Start Flask with ngrok to create a public URL
if __name__ == '__main__':
    public_url = ngrok.connect(5000)  # Expose Flask on port 5000
    print(f"Public URL: {public_url}")
    app.run(port=5000)
