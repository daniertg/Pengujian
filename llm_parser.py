import re

def extract_components_from_llm_output(text, level="beginner"):
    result = {}
    python_code_match = re.search(r'```python\s*(.*?)\s*```', text, re.DOTALL)
    if python_code_match:
        result["python_code"] = python_code_match.group(1).strip()
    else:
        # Fallback method if code block format is inconsistent
        code_section_match = re.search(r'1\.\s*Python\s*Code:?(?:\s*```python)?\s*(.*?)(?:```|\n2\.)', text, re.DOTALL)
        if code_section_match:
            code = code_section_match.group(1).strip()
            # Remove possible markdown code fence if it wasn't captured in the regex
            result["python_code"] = re.sub(r'^```python|```$', '', code).strip()
        else:
            result["python_code"] = "Error: Could not extract Python code from response"
            
    # Extract explanation
    explanation_match = re.search(r'2\.\s*Explanation:?\s*(.*?)(?:\n3\.|\Z)', text, re.DOTALL)
    if explanation_match:
        result["explanation"] = explanation_match.group(1).strip()
    else:
        result["explanation"] = "Error: Could not extract explanation from response"
    
    # Extract tips if level is beginner
    if level == "beginner":
        tips_match = re.search(r'3\.\s*Tips:?\s*(.*?)(?:\Z)', text, re.DOTALL)
        if tips_match:
            result["tips"] = tips_match.group(1).strip()
        else:
            result["tips"] = "Error: Could not extract tips from response"
    
    return result
