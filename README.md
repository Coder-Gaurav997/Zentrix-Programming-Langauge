# 🚀 ZENTRIX

ZENTRIX is a custom interpreted programming language built using Python.  
It is designed to demonstrate how programming languages work internally, including tokenization, parsing, and execution.

---

## ✨ Features

- `let` for variable declaration
- Dynamic typing
- Data types: Number, String, Boolean (`true/false`), Null (`null`)
- Operators:
  - Arithmetic: `+ - * / %`
  - Comparison: `== != < > <= >=`
  - Logical: `&& ||`
- Control flow:
  - `if / else`
  - `while`
  - `for (i in a to b)`
- I/O:
  - `echo()` for output
  - `input()` for user input

---

## 🧠 Example

```zentrix
let x = 5;
let y = 10;

if (x < y) {
    echo("x is smaller");
}

for (i in 0 to 3) {
    echo(i);
}
```

---

## 📁 Structure

zentrix/
│── lexer.py
│── parser.py
│── ast_nodes.py
│── interpreter.py
│── main.py
|── test.zx 

---

## ▶️ Run

```bash
python main.py
```

---

## 🎯 Purpose

- Learn how interpreters work
- Understand language design
- Build a custom programming language from scratch

---

## ⚠️ Limitations

- No functions yet
- No scope system
- Basic error handling

---

## 👨‍💻 Author

'Gaurav Pandey' (Mr. Def@ult)

---

> Clean, readable, and doesn’t try to impress recruiters with buzzwords it can’t back up. Perfect.
