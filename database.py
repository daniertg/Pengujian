database_syntax = [
  # Input/Output (4 items)
  {
    "id": 1,
    "level": "beginner",
    "category": "print",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World\");\n    }\n}",
    "expected_python": "print(\"Hello World\")",
    "expected_output": "Hello World"
  },
  {
    "id": 2,
    "level": "beginner", 
    "category": "input",
    "java_code": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner s = new Scanner(System.in);\n        String x = s.nextLine();\n        System.out.println(x);\n    }\n}",
    "expected_python": "x = input()\nprint(x)",
    "expected_output": "test_input"
  },
  {
    "id": 3,
    "level": "beginner",
    "category": "print multiple",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Line 1\");\n        System.out.println(\"Line 2\");\n    }\n}",
    "expected_python": "print(\"Line 1\")\nprint(\"Line 2\")",
    "expected_output": "Line 1\nLine 2"
  },
  {
    "id": 4,
    "level": "beginner",
    "category": "print with variable",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String name = \"Java\";\n        System.out.println(\"Hello \" + name);\n    }\n}",
    "expected_python": "name = \"Java\"\nprint(\"Hello \" + name)",
    "expected_output": "Hello Java"
  },

  # Variables (4 items)
  {
    "id": 5,
    "level": "beginner",
    "category": "integer variable",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int x = 10;\n        System.out.println(x);\n    }\n}",
    "expected_python": "x = 10\nprint(x)",
    "expected_output": "10"
  },
  {
    "id": 6,
    "level": "beginner",
    "category": "string variable",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String text = \"Hello\";\n        System.out.println(text);\n    }\n}",
    "expected_python": "text = \"Hello\"\nprint(text)",
    "expected_output": "Hello"
  },
  {
    "id": 7,
    "level": "beginner",
    "category": "double variable",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        double pi = 3.14;\n        System.out.println(pi);\n    }\n}",
    "expected_python": "pi = 3.14\nprint(pi)",
    "expected_output": "3.14"
  },
  {
    "id": 8,
    "level": "beginner",
    "category": "boolean variable",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        boolean flag = true;\n        System.out.println(flag);\n    }\n}",
    "expected_python": "flag = True\nprint(flag)",
    "expected_output": "True"
  },

  # Conditionals (4 items)
  {
    "id": 9,
    "level": "beginner",
    "category": "if-else",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int x = 5;\n        if (x > 3)\n            System.out.println(\"Greater\");\n        else\n            System.out.println(\"Smaller\");\n    }\n}",
    "expected_python": "x = 5\nif x > 3:\n    print(\"Greater\")\nelse:\n    print(\"Smaller\")",
    "expected_output": "Greater"
  },
  {
    "id": 10,
    "level": "beginner",
    "category": "if-else-if",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int score = 85;\n        if (score >= 90)\n            System.out.println(\"A\");\n        else if (score >= 80)\n            System.out.println(\"B\");\n        else\n            System.out.println(\"C\");\n    }\n}",
    "expected_python": "score = 85\nif score >= 90:\n    print(\"A\")\nelif score >= 80:\n    print(\"B\")\nelse:\n    print(\"C\")",
    "expected_output": "B"
  },
  {
    "id": 11,
    "level": "beginner",
    "category": "nested if",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int a = 5, b = 3;\n        if (a > 0) {\n            if (b > 0)\n                System.out.println(\"Both positive\");\n        }\n    }\n}",
    "expected_python": "a = 5\nb = 3\nif a > 0:\n    if b > 0:\n        print(\"Both positive\")",
    "expected_output": "Both positive"
  },
  {
    "id": 12,
    "level": "beginner",
    "category": "switch-case",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int day = 2;\n        switch(day) {\n            case 1:\n                System.out.println(\"Monday\");\n                break;\n            case 2:\n                System.out.println(\"Tuesday\");\n                break;\n            default:\n                System.out.println(\"Other\");\n        }\n    }\n}",
    "expected_python": "day = 2\nif day == 1:\n    print(\"Monday\")\nelif day == 2:\n    print(\"Tuesday\")\nelse:\n    print(\"Other\")",
    "expected_output": "Tuesday"
  },

  # Loops (4 items)
  {
    "id": 13,
    "level": "beginner",
    "category": "for loop",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        for (int i = 0; i < 3; i++)\n            System.out.println(i);\n    }\n}",
    "expected_python": "for i in range(3):\n    print(i)",
    "expected_output": "0\n1\n2"
  },
  {
    "id": 14,
    "level": "beginner",
    "category": "while loop",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int i = 0;\n        while (i < 3) {\n            System.out.println(i);\n            i++;\n        }\n    }\n}",
    "expected_python": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1",
    "expected_output": "0\n1\n2"
  },
  {
    "id": 15,
    "level": "beginner",
    "category": "do-while loop",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int i = 0;\n        do {\n            System.out.println(i);\n            i++;\n        } while (i < 2);\n    }\n}",
    "expected_python": "i = 0\nwhile True:\n    print(i)\n    i += 1\n    if not (i < 2):\n        break",
    "expected_output": "0\n1"
  },
  {
    "id": 16,
    "level": "beginner",
    "category": "for-each loop",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int[] numbers = {1, 2, 3};\n        for (int num : numbers)\n            System.out.println(num);\n    }\n}",
    "expected_python": "numbers = [1, 2, 3]\nfor num in numbers:\n    print(num)",
    "expected_output": "1\n2\n3"
  },

  # Operators (4 items)
  {
    "id": 17,
    "level": "beginner",
    "category": "arithmetic operators",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int a = 10, b = 3;\n        System.out.println(a + b);\n        System.out.println(a - b);\n        System.out.println(a * b);\n    }\n}",
    "expected_python": "a = 10\nb = 3\nprint(a + b)\nprint(a - b)\nprint(a * b)",
    "expected_output": "13\n7\n30"
  },
  {
    "id": 18,
    "level": "beginner",
    "category": "logical operators",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        boolean a = true, b = false;\n        System.out.println(a && b);\n        System.out.println(a || b);\n        System.out.println(!a);\n    }\n}",
    "expected_python": "a = True\nb = False\nprint(a and b)\nprint(a or b)\nprint(not a)",
    "expected_output": "False\nTrue\nFalse"
  },
  {
    "id": 19,
    "level": "beginner",
    "category": "comparison operators",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int x = 5, y = 10;\n        System.out.println(x == y);\n        System.out.println(x != y);\n        System.out.println(x < y);\n    }\n}",
    "expected_python": "x = 5\ny = 10\nprint(x == y)\nprint(x != y)\nprint(x < y)",
    "expected_output": "False\nTrue\nTrue"
  },
  {
    "id": 20,
    "level": "beginner",
    "category": "increment/decrement",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int x = 5;\n        x++;\n        System.out.println(x);\n        x--;\n        System.out.println(x);\n    }\n}",
    "expected_python": "x = 5\nx += 1\nprint(x)\nx -= 1\nprint(x)",
    "expected_output": "6\n5"
  },

  # Data Types (4 items)
  {
    "id": 21,
    "level": "beginner",
    "category": "primitive types",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int i = 10;\n        double d = 3.14;\n        char c = 'A';\n        boolean b = true;\n        System.out.println(i + \" \" + d + \" \" + c + \" \" + b);\n    }\n}",
    "expected_python": "i = 10\nd = 3.14\nc = 'A'\nb = True\nprint(str(i) + \" \" + str(d) + \" \" + c + \" \" + str(b))",
    "expected_output": "10 3.14 A True"
  },
  {
    "id": 22,
    "level": "beginner",
    "category": "type casting",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int i = 10;\n        double d = (double) i;\n        System.out.println(d);\n    }\n}",
    "expected_python": "i = 10\nd = float(i)\nprint(d)",
    "expected_output": "10.0"
  },
  {
    "id": 23,
    "level": "beginner",
    "category": "constants",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        final int MAX = 100;\n        System.out.println(MAX);\n    }\n}",
    "expected_python": "MAX = 100\nprint(MAX)",
    "expected_output": "100"
  },
  {
    "id": 24,
    "level": "beginner",
    "category": "multiple variables",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int a = 1, b = 2, c = 3;\n        System.out.println(a + b + c);\n    }\n}",
    "expected_python": "a = 1\nb = 2\nc = 3\nprint(a + b + c)",
    "expected_output": "6"
  },

  # String Manipulation (3 items)
  {
    "id": 25,
    "level": "beginner",
    "category": "string length",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String text = \"Hello\";\n        System.out.println(text.length());\n    }\n}",
    "expected_python": "text = \"Hello\"\nprint(len(text))",
    "expected_output": "5"
  },
  {
    "id": 26,
    "level": "beginner",
    "category": "string concatenation",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String first = \"Hello\";\n        String second = \"World\";\n        System.out.println(first + \" \" + second);\n    }\n}",
    "expected_python": "first = \"Hello\"\nsecond = \"World\"\nprint(first + \" \" + second)",
    "expected_output": "Hello World"
  },
  {
    "id": 27,
    "level": "beginner",
    "category": "string methods",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String text = \"Hello\";\n        System.out.println(text.toUpperCase());\n        System.out.println(text.toLowerCase());\n    }\n}",
    "expected_python": "text = \"Hello\"\nprint(text.upper())\nprint(text.lower())",
    "expected_output": "HELLO\nhello"
  },

  # Arrays/Lists (3 items)
  {
    "id": 28,
    "level": "beginner",
    "category": "array declaration",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int[] numbers = {1, 2, 3, 4, 5};\n        System.out.println(numbers[2]);\n    }\n}",
    "expected_python": "numbers = [1, 2, 3, 4, 5]\nprint(numbers[2])",
    "expected_output": "3"
  },
  {
    "id": 29,
    "level": "beginner",
    "category": "array length",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        int[] arr = {10, 20, 30};\n        System.out.println(arr.length);\n    }\n}",
    "expected_python": "arr = [10, 20, 30]\nprint(len(arr))",
    "expected_output": "3"
  },
  {
    "id": 30,
    "level": "beginner",
    "category": "array iteration",
    "java_code": "public class Main {\n    public static void main(String[] args) {\n        String[] fruits = {\"apple\", \"banana\", \"orange\"};\n        for (int i = 0; i < fruits.length; i++)\n            System.out.println(fruits[i]);\n    }\n}",
    "expected_python": "fruits = [\"apple\", \"banana\", \"orange\"]\nfor i in range(len(fruits)):\n    print(fruits[i])",
    "expected_output": "apple\nbanana\norange"
  }
]
