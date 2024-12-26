import subprocess
import os
import tempfile
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to execute code based on language
def execute_code(language, code):
    try:
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=f'.{language}') as temp_file:
            temp_file.write(code)
            temp_file.close()
            file_path = temp_file.name

            # Define commands for different languages
            if language == 'python':
                result = subprocess.run(['python', file_path], capture_output=True, text=True)
            elif language == 'c':
                result = subprocess.run(['gcc', file_path, '-o', file_path[:-2]], capture_output=True, text=True)
                if result.returncode == 0:
                    result = subprocess.run([file_path[:-2]], capture_output=True, text=True)
                else:
                    return result.stderr
            elif language == 'cpp':
                result = subprocess.run(['g++', file_path, '-o', file_path[:-4]], capture_output=True, text=True)
                if result.returncode == 0:
                    result = subprocess.run([file_path[:-4]], capture_output=True, text=True)
                else:
                    return result.stderr
            elif language == 'java':
                result = subprocess.run(['javac', file_path], capture_output=True, text=True)
                if result.returncode == 0:
                    result = subprocess.run(['java', file_path[:-5]], capture_output=True, text=True)
                else:
                    return result.stderr
            else:
                return "Unsupported language."

            # Return the output or error
            return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
    finally:
        # Clean up the temporary file
        os.remove(file_path)

# Route to render the HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle code execution
@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    language = data['language']
    code = data['code']
    output = execute_code(language, code)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
