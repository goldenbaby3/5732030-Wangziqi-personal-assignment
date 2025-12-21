Task 2
1. Project Overview

This project implements a supermarket market basket analysis system using Python.
The system analyses customer transaction records to identify purchasing patterns and relationships between products.

The implementation focuses on software engineering quality, including modular design, test-driven development, and automated testing.

The system is designed to answer the following questions.

🔹Which products are most frequently purchased together

🔹What are the most common product combinations

🔹How to determine whether two products are frequently co-purchased

🔹How to generate product recommendations based on transaction history

2. System Functionality

🔹Construction of a co-purchase graph

·Each node represents a product

·Each edge represents a co-purchase relationship

·Edge weights represent co-occurrence frequency

🔹Analytical operations

·Query the most frequently co-purchased products for a given item

·Determine whether two products are frequently purchased together

·Identify frequent itemsets from transaction data

🔹Recommendation functionality

·Accept one or more target products

·Return products with the strongest co-purchase relationships

🔹Visualization

Graph-based visualization of product relationships

3. Project Structure
```bash
task2/
├─ run_system2.py
├─ README.md
├─ requirements.txt
├─ data/
│  └─ Supermarket_dataset_PAI.csv
├─ modules/
│  ├─ __init__.py
│  ├─ basket.py
│  ├─ graph_builder.py
│  ├─ co_purchase.py
│  ├─ frequent_items.py
│  ├─ recommender.py
│  └─ visualizer.py
└─ tests/
   ├─ __init__.py
   ├─ test_basket.py
   ├─ test_graph_builder.py
   ├─ test_co_purchase.py
   ├─ test_frequent_items.py
   └─ test_recommender.py
```

4. How to Run the Program
🔹Navigate to the project directory
```bash
cd Y:/WM9QF/task2
```
🔹Run the main program
```bash
python run_system2.py
```
🔹Follow the command-line instructions to input products, view analysis results, and generate visualizations.

5. Automated Testing and TDD

This project follows test-driven development principles.

·Each functional module is tested using automated unit tests

·Tests verify correctness and edge cases

·Test files are organised independently from implementation code
```bash
pytest
```

6. Test-Driven Development (TDD)
🔹This project strictly follows the test-driven development approach
🔹Test cases are written before implementing functional code
🔹Each functional module has one or more corresponding test files
🔹Tests cover:
 ·Functional correctness
 ·Edge cases such as empty inputs, missing values, and invalid data types
🔹The pytest framework is used for automated testing
```bash
pytest tests/ -v
```

7. Dataset Description

🔹Dataset file name is Supermarket_dataset_PAI.csv

🔹Each record represents a purchased product

🔹Transactions are grouped by member number and date

🔹Each group forms a shopping basket

8. Real-World Application

Market basket analysis is widely applied in retail scenarios.

·Product placement optimisation

·Promotion and bundling strategies

·Recommendation system development

·Customer behaviour analysis

9. References
🔹Han, J., Kamber, M., and Pei, J.
Data Mining: Concepts and Techniques

🔹NetworkX Documentation

🔹Pytest Documentation

AI tools were used only to assist with code structuring, debugging, and test generation, in accordance with coursework guidelines

10. Coursework Requirement Compliance

🔹Modular Python implementation

🔹Test-driven development with automated testing

🔹Edge case handling

🔹Clear separation of data processing, algorithms, and application logic

🔹Suitable for Git-based version control and review
