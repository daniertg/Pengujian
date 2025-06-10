import black

# Kode dengan format yang tidak rapi (spasi berlebih, indentasi tak konsisten, dll)
python_code = """
"""

# Format kode menggunakan Black
formatted = black.format_str(python_code, mode=black.Mode())

print("=== Kode Asli ===")
print(python_code)
print("\n=== Hasil Format Black ===")
print(formatted)
