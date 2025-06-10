from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
from prompts import get_java_to_python_prompt_beginner, get_java_to_python_prompt_expert
from java_syntax import check_java_syntax
from llama_client import call_ollama
from gemini_client import call_gemini
from llm_parser import extract_components_from_llm_output
from database import database_syntax
from similarity_checker import find_best_match, test_all_database_items, get_database_item_by_id, compare_with_database

load_dotenv()

app = Flask(__name__, template_folder='templates')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/database')
def get_database():
    return jsonify({"database": database_syntax})

@app.route('/test_similarity', methods=['POST'])
def test_similarity():
    try:
        data = request.get_json()
        if not data or 'generated_python' not in data:
            return jsonify({"error": "Generated Python code is required"}), 400
        
        generated_python = data['generated_python']
        test_type = data.get('test_type', 'all')
        item_id = data.get('item_id', None)
        
        if test_type == 'single' and item_id:
            database_item = get_database_item_by_id(item_id)
            if not database_item:
                return jsonify({"error": f"Database item with ID {item_id} not found"}), 404
            
            result = compare_with_database(generated_python, database_item)
            return jsonify({
                "test_type": "single",
                "item_id": item_id,
                "result": result
            })
        else:
            results = test_all_database_items(generated_python)
            return jsonify({
                "test_type": "all",
                "total_items": len(results),
                "results": results
            })
        
    except Exception as e:
        return jsonify({"error": f"Similarity test error: {str(e)}"}), 500

@app.route('/test_single/<int:item_id>', methods=['POST'])
def test_single_item(item_id):
    try:
        data = request.get_json()
        if not data or 'generated_python' not in data:
            return jsonify({"error": "Generated Python code is required"}), 400
        
        generated_python = data['generated_python']
        database_item = get_database_item_by_id(item_id)
        
        if not database_item:
            return jsonify({"error": f"Database item with ID {item_id} not found"}), 404
        
        result = compare_with_database(generated_python, database_item)
        return jsonify({
            "item_id": item_id,
            "database_item": database_item,
            "similarity_result": result
        })
        
    except Exception as e:
        return jsonify({"error": f"Single item test error: {str(e)}"}), 500

@app.route('/demo', methods=['GET', 'POST'])
def demo_code():
    messy_python = """
kata = ["katk", "mobil", "level", "rumah"]
for k in kata:
    if k == k[::-1]:
        print(f"{k} adalah palindrom.")
    else:
        print(f"{k} bukan palindrom.")
"""
    explanation = "Ini adalah contoh demo yang menampilkan kode Python dengan format yang berantak. Kode ini sengaja dibuat tidak rapi untuk menunjukkan kemampuan konverter dalam memberikan hasil yang lebih baik. Demo ini hanya untuk keperluan pengujian saja."
    return jsonify({
        "python_code": messy_python,
        "explanation": explanation
    })

@app.route('/convert_serve', methods=['POST'])
def convert_with_llama():
    try:
        data = request.get_json()
        if not data or 'java_code' not in data:
            return jsonify({"error": "Java code is required"}), 400

        java_code = data['java_code']
        level_cs = data.get('level_cs', 'beginner').lower()

        syntax_valid, syntax_error_msg = check_java_syntax(java_code)
        if not syntax_valid:
            return jsonify({
                "python_code": "java syntax is invalid",
                "explanation": syntax_error_msg
            })

        # Select the appropriate prompt based on level_cs
        if level_cs == "expert":
            prompt = get_java_to_python_prompt_expert(java_code)
        else:  # default to beginner
            prompt = get_java_to_python_prompt_beginner(java_code)
            
        try:
            result = call_ollama(prompt)
            generated_text = result.get('response', '')
        except Exception as e:
            return jsonify({"error": f"Ollama API error: {str(e)}"}), 500
            
        # Create response with raw text for debugging
        response_data = {
            "raw_response": generated_text
        }

        # Extract components using the llm_parser module
        extracted_data = extract_components_from_llm_output(generated_text, level_cs)
        response_data.update(extracted_data)

        return jsonify(response_data)

    except Exception as e:
        import traceback
        print(f"Error in convert_with_llama: {str(e)}")
        print(traceback.format_exc())
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/convert', methods=['POST'])
def convert_java_to_python():
    data = request.get_json()
    if not data or 'java_code' not in data:
        return jsonify({"error": "Harap kirim Java code di body request sebagai 'java_code'"}), 400

    java_code = data['java_code']
    level_cs = data.get('level_cs', 'beginner').lower()

    syntax_valid, syntax_error_msg = check_java_syntax(java_code)
    if not syntax_valid:
        return jsonify({
            "python_code": "java syntax is invalid",
            "explanation": syntax_error_msg
        })

    try:
        # Select the appropriate prompt based on level_cs
        if level_cs == "expert":
            prompt = get_java_to_python_prompt_expert(java_code)
        else:  # default to beginner
            prompt = get_java_to_python_prompt_beginner(java_code)

        content = call_gemini(prompt)
        
        # Create response with raw text for debugging, but without the java_code
        response_data = {
            "raw_response": content
        }
        
        # Extract components using the llm_parser module
        extracted_data = extract_components_from_llm_output(content, level_cs)
        response_data.update(extracted_data)
            
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)