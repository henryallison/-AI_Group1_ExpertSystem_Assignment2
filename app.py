from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Crop Disease Diagnosis Logic
def diagnose_crop(crop, symptoms):
    diagnosis = "No disease detected."
    treatment = "Maintain good farming practices."

    if crop == 'maize':
        if 'grayish lesions' in symptoms:
            diagnosis = "Northern Leaf Blight"
            treatment = "Apply fungicides containing chlorothalonil or mancozeb."
        elif 'small, oval spots' in symptoms:
            diagnosis = "Gray Leaf Spot"
            treatment = "Use resistant maize varieties and apply fungicides."
        elif 'internal discoloration and rot' in symptoms:
            diagnosis = "Stalk Rot"
            treatment = "Improve field drainage and avoid over-fertilization."
    
    elif crop == 'coffee':
        if 'orange rust spots' in symptoms:
            diagnosis = "Coffee Leaf Rust"
            treatment = "Apply copper-based fungicides and prune infected leaves."
        elif 'dark, sunken lesions' in symptoms:
            diagnosis = "Coffee Berry Disease"
            treatment = "Use fungicides like carbendazim and practice good field hygiene."
        elif 'yellowing and wilting' in symptoms:
            diagnosis = "Fusarium Wilt"
            treatment = "Remove and destroy infected plants, and use resistant varieties."

    return diagnosis, treatment

# Route to serve the Diagnosis Page
@app.route('/')
def home():
    return render_template('diagnosis.html')

# Diagnosis API Route
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    crop = data.get('crop')
    symptoms = data.get('symptoms', [])

    diagnosis, treatment = diagnose_crop(crop, symptoms)
    return jsonify({"diagnosis": diagnosis, "treatment": treatment})

if __name__ == '__main__':
    app.run(debug=True)
