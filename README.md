# Password Generator CLI Application

This is a fully functional Password Generator CLI Application built using python, during my python programming internship at CodSoft. This Password Generator CLI Application allows users to generate strong and random passwords based on their desired length and complexity. Users can specify whether they want a simple, medium, or strong password, and the program will generate one accordingly.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Example Usage](#example-usage)

## Features

- Custom Length: Users can specify the length of the password they wish to generate.
- Complexity Levels:
  1. Simple: Passwords containing only letters (uppercase and lowercase).
  2. Medium: Passwords containing letters and digits.
  3. Strong: Passwords containing letters, digits, and punctuation marks.
- Randomness: Each password is randomly generated based on the specified complexity level.
- Error Handling: Handles invalid inputs for password length and complexity.

## Technologies Used

- Python

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/rabumaabraham/CODSOFT-TASK3/tree/main
    ```

2. **Navigate into the project directory**:

    ```bash
    cd password-generator
    ```

3. **Run the application**:

    python password.py


## Example Usage

Enter the desired length of the password: 12

Enter the desired complexity (simple, medium, strong): strong

Generated Password: qF@zH9!p7LzR

Do you want to generate another password? (Y/N): Y

Enter the desired length of the password: 8

Enter the desired complexity (simple, medium, strong): medium

Generated Password: A9bVf2Xz

Do you want to generate another password? (Y/N): N
Goodbye!
