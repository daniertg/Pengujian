import subprocess
import tempfile
import os
import time
from database import database_syntax
from levenshtein_manual import calculate_similarity_percentage

def calculate_similarity(str1, str2):
    """Calculate similarity between two strings using manual Levenshtein distance"""
    return calculate_similarity_percentage(str1, str2)

def execute_python_code(code):
    """Execute Python code and return the output"""
    temp_file = None
    try:
        # Check if code contains input() and modify accordingly
        if 'input()' in code:
            # Provide mock input for testing
            mock_input = "test_input"
            # Replace input() with mock input or use stdin
            modified_code = code.replace('input()', f'"{mock_input}"')
            code_to_execute = modified_code
            input_data = None
        else:
            code_to_execute = code
            input_data = None
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        temp_file.write(code_to_execute)
        temp_file.flush()
        temp_file.close()
        
        # Execute the Python file
        result = subprocess.run(
            ['python', temp_file.name],
            capture_output=True,
            text=True,
            timeout=5,
            input=input_data
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
            
    except subprocess.TimeoutExpired:
        return "Error: Code execution timeout"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Clean up temporary file
        if temp_file and os.path.exists(temp_file.name):
            try:
                time.sleep(0.1)  # Small delay to ensure file is released
                os.unlink(temp_file.name)
            except Exception:
                pass  # Ignore cleanup errors

def compare_with_database(generated_python, database_item):
    """Compare generated Python code with database item"""
    expected_python = database_item.get('expected_python', '')
    expected_output = database_item.get('expected_output', '')
    
    # Calculate syntax similarity
    syntax_similarity = calculate_similarity(generated_python, expected_python)
    
    # Execute generated code and compare output
    generated_output = execute_python_code(generated_python)
    output_similarity = calculate_similarity(generated_output, expected_output)
    
    # Calculate weighted score (50% syntax, 50% output)
    total_score = (syntax_similarity * 0.5) + (output_similarity * 0.5)
    
    return {
        'syntax_similarity': syntax_similarity,
        'output_similarity': output_similarity,
        'total_score': round(total_score, 2),
        'expected_python': expected_python,
        'generated_python': generated_python,
        'expected_output': expected_output,
        'generated_output': generated_output,
        'database_item': database_item
    }

def find_best_match(generated_python, database_list):
    """Find the best matching item from database"""
    best_match = None
    best_score = 0
    
    for item in database_list:
        comparison = compare_with_database(generated_python, item)
        if comparison['total_score'] > best_score:
            best_score = comparison['total_score']
            best_match = comparison
    
    return best_match

def test_all_database_items(generated_python):
    """Test similarity against all database items individually"""
    results = []
    
    for item in database_syntax:
        comparison = compare_with_database(generated_python, item)
        results.append({
            'id': item['id'],
            'category': item['category'],
            'level': item['level'],
            'java_code': item['java_code'],
            'syntax_similarity': comparison['syntax_similarity'],
            'output_similarity': comparison['output_similarity'],
            'total_score': comparison['total_score'],
            'expected_python': comparison['expected_python'],
            'expected_output': comparison['expected_output'],
            'generated_output': comparison['generated_output']
        })
    
    # Sort by total score descending
    results.sort(key=lambda x: x['total_score'], reverse=True)
    
    return results

def get_database_item_by_id(item_id):
    """Get specific database item by ID"""
    for item in database_syntax:
        if item['id'] == item_id:
            return item
    return None
