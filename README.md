```markdown
# 📊 Student Grade Calculator

A precise, terminal-based Python application developed for **Week 2: Making Decisions & Repeating Tasks** of **The Developers Arena** Internship Program. This project builds a production-grade automated academic grading system executing algorithmic evaluation scales, functional isolation of logical tasks, runtime user error prevention loops, and input sanitization practices.

---

## 🎯 1. Project Overview
The **Student Grade Calculator** addresses the problem of human data-entry mistakes during academic marking evaluations. By building a software system around recursive exception trapping boundaries and modular programming structures, the program guarantees clean operational flows.

### 📋 Quality Standards & Objectives
* **Encapsulated Logic:** Decoupled data parsing mechanics from core assessment functions.
* **Fault-Tolerant Loops:** Rejection loops guarding input routines from invalid non-numeric variables or out-of-bounds parameters.
* **Intuitive Feedback UI:** Clear output visualizations returning capitalized user tags alongside tailored motivational insights based on grade performance tiers.

---

## ⚙️ 2. Setup & Installation Instructions

Follow these instructions sequentially to provision a local staging environment and deploy the script on your workstation:

### Prerequisite System Requirements
* **Python Engine:** Runtime environment `v3.8` through `v3.12+` installed securely on the host platform.
* **Terminal Interface:** Native command console (PowerShell, Command Prompt, or bash).

### Deployment Walkthrough
1. **Repository Serialization:** Clone or download this project workspace into your directory structures:
   ```bash
   git clone [https://github.com/MansiYadav17/TheDevelopersArena_Task2.git](https://github.com/MansiYadav17/TheDevelopersArena_Task2.git)

```

2. **Directory Execution:** Change context to the precise project working root:
```bash
cd TheDevelopersArena_Task2

```


3. **Program Execution:** Trigger the python execution engine against the source file entry point directly:
```bash
python grade_calculator.py

```



---

## 🏗️ 3. Technical Architecture & Code Structure

The source architecture isolates the business logic layer completely from external hardware input/output processing elements.

```
📁 TheDevelopersArena_Task2/
├── 📄 README.md              # Global project blueprint, technical details & run-guide
├── 📄 grade_calculator.py    # Main program source executing input validation loops & logic
├── 📄 test_cases.txt         # Comprehensive matrix containing QA edge validation tests
└── 📁 screenshots/           # Directory holding verified program terminal capture logs
    └── functional_output.png # Live script trace rendering pristine output loops

```

### Modular Blueprint Definitions

* `get_grade_info(marks)`: A pure logical function mapping scalar floats to explicit evaluation parameters. It operates with a zero-side-effect profile, returning a tuple containing the static single-character alpha `Grade` string alongside a tailored `Message` token.
* `main()`: The global sequence coordinator orchestrating sequential programmatic setup. It handles terminal prompt rendering, blocks terminal operations via sanitization constraints, manages exception frames, and flushes output strings to standard outputs.

---

## 📐 4. Algorithm & Grading Logic

The underlying logic tracks specific categorical scale limits, converting numeric parameters strictly into localized performance tiers:

| Marks Ceiling Bound | Marks Floor Bound | Letter Grade Designation | Evaluator Motivational Insight Tone |
| --- | --- | --- | --- |
| **100** | **90** | **A** | *Excellent work! You're a superstar!* |
| **89.9** | **80** | **B** | *Very Good! Keep it up!* |
| **79.9** | **70** | **C** | *Good job! You're doing well.* |
| **69.9** | **60** | **D** | *You passed, but there is room for improvement.* |
| **59.9** | **0** | **F** | *Don't give up! Study harder and you will improve.* |

### Exception Mitigation and Sanitization Routine

To ensure the integrity of the tracking system, input parameters are processed through an interactive multi-stage validation check:

1. **String Sanitization:** Leading or trailing whitespace from names are trimmed away cleanly using explicit `.strip()` array extensions.
2. **Type Coercion Boundaries:** Raw terminal keyboard entries are dynamically mapped to double-precision `float` objects via explicit mathematical type casting.
3. **Type Exception Capture:** The input collection is enclosed in an active `try-except ValueError` tracking frame. Any entry containing character maps, arrays, symbols, or empty commands triggers a prompt loop reset without terminal system collapse.
4. **Range Restriction Checks:** Logical relational expressions (`0 <= marks <= 100`) isolate scores outside real bounds, forcing immediate correction and maintaining runtime continuity.

---

## 🖼️ 5. Visual Documentation

The application operates as an interactive CLI application. Below is an illustrative trace log showing functional operations matching terminal performance constraints:

```text
--- Student Grade Calculator ---
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA:
Marks: 85.0/100
Grade: B
Message: Very Good! Keep it up! 👍

```

*(Verify your deployment matches this signature by matching terminal windows with files saved directly inside the `screenshots/` directory structure).*

---

## 🧪 6. Testing Evidence Portfolio

Comprehensive quality assurance validation is managed using automated diagnostic simulation paths to test the robustness of all validation loops:

```text
====================================================================
TEST MATRIX - VALIDATION SUITE RECORD
====================================================================
[TEST ID 01] TARGET: Standard Pathway Execution
- Input Name: "Priya" | Input Marks: "85"
- Expected: Grade B, Message: "Very Good! Keep it up! 👍"
- Result: STATUS_PASS (Application resolves exactly as predicted)

[TEST ID 02] TARGET: High Boundary-Value Evaluation
- Input Name: "Alex"  | Input Marks: "100"
- Expected: Grade A, Message: "Excellent work! You're a superstar! 👍"
- Result: STATUS_PASS (Boundary threshold calculations compute correctly)

[TEST ID 03] TARGET: Out-of-Bounds Negative Bounds Mitigation
- Input Name: "John"  | Input Marks: "-5"
- Expected: Output "Error: Please enter a value between 0 and 100." -> Refresh Input.
- Result: STATUS_PASS (Out-of-range bounds trapped cleanly)

[TEST ID 04] TARGET: Out-of-Bounds Maximum Bounds Mitigation
- Input Name: "Sam"   | Input Marks: "105"
- Expected: Output "Error: Please enter a value between 0 and 100." -> Refresh Input.
- Result: STATUS_PASS (Over-maximum boundaries handled perfectly)

[TEST ID 05] TARGET: Non-Numeric Literal Character Interception
- Input Name: "Lily"  | Input Marks: "ninety"
- Expected: Output "Invalid input! Please enter a numerical value for marks." -> Refresh Input.
- Result: STATUS_PASS (ValueError trapped cleanly without program termination)
====================================================================

```

```

```
