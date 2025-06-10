def get_java_to_python_prompt_beginner(java_code: str) -> str:   
    return f"""
Task: Convert basic Java code to Python compatible with Skulpt (Python-in-the-browser).

CONVERSION RULES:

1. ONLY convert basic Java syntax:
   - Input/Output: Scanner, System.out
   - Variables: declaration, assignment
   - Branching: if, else if, else, switch-case
   - Loops: for, while, do-while
   - Operators: mathematical, logical, comparison
   - Primitive data types
   - Basic String manipulation
   - array / list

2. REJECT and output "404" if encountering:
   - OOP concepts (object, inheritance, polymorphism)
     - Example: when there are 2 or more classes interacting
     - Example: extends, implements, super
   - Exception handling (try-catch)
   - Lambda expressions
   - Interface/abstract class

3. Output requirements:
   - Output MUST follow exact format as in examples
   - Only use built-in Python (no external libraries)
   - Don't add comments in Python code
   - Don't include original Java code in output

ACCEPTABLE OUTPUT FORMATS (MUST BE EXACT):

If advanced syntax is encountered:
1. Python Code:
```python
404
```

2. Explanation:
404

3. Tips:
404

If ONLY basic syntax:
1. Python Code:
python
# Converted Python code

2. Explanation:
Line-by-line syntax differences explanation in BAHASA INDONESIA with format:
a. Java = <Java code>
   Python = <equivalent Python code if not exists answer "Tidak ada padanan">
   Explanation = <syntax difference explanation in BAHASA INDONESIA>
b. Java = <next code>
   Python = <its equivalent>
   Explanation = <explanation>
...

3. Tips:
One brief tip about Python related to syntax python output in BAHASA INDONESIA.

ACCEPTED SYNTAX EXAMPLES:
- int x = 10;
- System.out.println("Hello");
- if (x > 5) {{...}}
- for (int i=0; i<10; i++) {{...}}
- int[] arr = {1, 2, 3};

REJECTED SYNTAX EXAMPLES:
- Two or more interacting classes:
  class A {{..}}
  class B extends A {{..}}  # will be rejected
- Object creation:
  Scanner sc = new Scanner(System.in);  # will be rejected
- Exception handling:
  try {{...}} catch {{...}}  # will be rejected

Java code to convert:
{java_code}

Remember: ONLY respond with 3 numbered sections as in format above, without any additions.
"""


def get_java_to_python_prompt_expert(java_code: str) -> str:    
    return f"""
After checking the rules and output format, convert the following Java code to Python that is fully compatible with Skulpt (Python-in-the-browser):
RULES:

1. Convert all Java syntax to Python based on the reference database above.
   - This includes both basic syntax and object-oriented elements

2. Make sure the behavior and output of the converted Python code is the same as the original Java code.

3. Do NOT use any external libraries.
   - Only use Python built-in syntax and functions (standard library only).

4. Only return the following two numbered sections in your output exactly as shown below:
   - 1. Python Code
   - 2. Explanation
   
5. Do NOT add any other text, headers, or content beyond these two numbered sections.

EXPECTED OUTPUT FORMAT (EXACTLY AS SHOWN BELOW):

1. Python Code:
```python
# Your converted Python code here
```

2. Explanation:
Brief explanation in Bahasa Indonesia (maximum 40 words) that summarizes the syntax differences.

Java Code:
{java_code}

Remember to respond ONLY with the two numbered sections exactly as shown in the expected output format.
"""