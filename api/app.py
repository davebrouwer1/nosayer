# app.py

import os
from flask import Flask, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- SETUP ---
app = Flask(__name__)
CORS(app) 

# Configure the Gemini AI client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- AI PROMPT ---
prompt = """Generate a single, short, creative, and subtly passive-aggressive phrase for saying "no". The tone should be witty and universally applicable, suitable for dodging social plans or workplace requests with equal finesse. The underlying message should be a firm rejection, humorously placing the blame on the absurdity of the request itself or a fictional, unbreakable prior commitment. Do not include any quotation marks or introductory text. Just the phrase itself."""
# --- API ROUTE ---
@app.route("/api/get-rejection", methods=['GET'])
def get_rejection():
    try:
        # --- THIS IS THE LINE WE'VE CHANGED ---
        model = genai.GenerativeModel('gemini-2.5-flash') # Use the new, correct model name
        
        response = model.generate_content(prompt)
        
        return jsonify({'rejection': response.text.strip()})
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({'error': "Oops, the AI is having a moment. Try again."}), 500

# --- START THE SERVER ---
if __name__ == '__main__':
    app.run(port=5000, debug=True)