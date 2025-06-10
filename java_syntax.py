import re
import tempfile
import subprocess

def check_java_syntax(java_code: str):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            match = re.search(r'public\s+class\s+(\w+)', java_code)
            class_name = match.group(1) if match else "Main"
            java_file = f"{temp_dir}/{class_name}.java"
            with open(java_file, "w", encoding="utf-8") as f:
                f.write(java_code)
            proc = subprocess.run(
                ["javac", java_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if proc.returncode != 0:
                return False, proc.stderr.strip()
            return True, ""
    except Exception as e:
        return False, f"Java syntax check error: {str(e)}"
