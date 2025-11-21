# COBOL to Python Converter

This project provides a simple framework and tools for **converting COBOL programs into Python**.  
The goal is not a 1:1 mechanical translation, but a **guided migration** that:

- Parses and analyzes COBOL source code
- Maps COBOL data structures and logic to Python
- Generates Python code templates
- Helps developers gradually modernize legacy systems

> ⚠️ Note: COBOL and Python are very different languages. Always review and test the generated Python code manually.

---

## 1. Features

- 🧩 **COBOL Parsing** – Basic parsing of COBOL divisions (IDENTIFICATION, DATA, PROCEDURE).
- 🔁 **Data Mapping** – Converts common `PIC` definitions into Python data types.
- 🧮 **Logic Translation** – Basic mapping of COBOL control structures (`IF`, `PERFORM`, simple `MOVE`, arithmetic) to Python.
- 📝 **Python Code Generation** – Produces Python modules as a starting point for refactoring.
- ✅ **Unit Test Scaffolding** – Optional generation of pytest-style test stubs.
- 📦 **Command-line Interface (CLI)** – Convert COBOL files via a simple command.

---

## 2. Project Structure

```text
cobol-to-python/
├─ README.md
├─ requirements.txt
├─ setup.py                    # Optional: if packaging as a library/CLI
├─ cobol_to_python/
│  ├─ __init__.py
│  ├─ cli.py                   # Entry point for command-line usage
│  ├─ Agent.py                 # COBOL parsing logic
│  ├─ mapper.py                # COBOL → Python type and structure mapping
│  └─ utils.py                 # Helper functions
└─ examples/
   ├─ sample.cob               # Example COBOL program
   └─ sample_converted.py      # Example generated Python program



##3. Prerequisites

Python: 3.9 or later

Optional: virtual environment (recommended)

Install dependencies:

pip install -r requirements.txt


Typical requirements.txt might include:

jinja2
click        # if using CLI
pytest       # for tests

4. How It Works (High Level)

Parse COBOL source

Reads .cob / .cbl file.

Extracts:

IDENTIFICATION DIVISION (program name, author, etc.)

DATA DIVISION (variables, PIC clauses)

PROCEDURE DIVISION (business logic / paragraphs)

Map COBOL concepts to Python

PIC 9(n) → int

PIC X(n) → str

WORKING-STORAGE variables → Python class attributes or local variables

IF / ELSE, PERFORM UNTIL, simple arithmetic → Python if, while, and operators.

Generate Python code

Builds Python classes/functions representing:

Program-level logic

Data structures

Optionally generates test stubs and comments describing original COBOL logic.

5. Usage
5.1 CLI Usage

After installing the project (editable install):

pip install -e .


Run the converter:

cobol2py convert \
  --input examples/sample.cob \
  --output examples/sample_converted.py


Example arguments:

--input : Path to COBOL source.

--output: Path for generated Python file.

--generate-tests : (optional) Also generate pytest stubs.


Recommended Migration Workflow

Choose candidate programs
Start with small, well-understood COBOL programs (utility scripts, small batch jobs).

Run converter
Generate Python code and store it in a parallel structure (e.g., legacy/ vs modern/).

Review & refactor

Clean up variable names.

Replace COBOL-style flow with idiomatic Python.

Add logging and error handling.

Write tests

Compare COBOL outputs vs Python outputs for the same inputs.

Use real production sample data when possible.

Gradual cutover

Run both implementations in parallel.

Switch consumers to the Python implementation once validated.