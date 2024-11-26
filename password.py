import random
import string

class PasswordGenerator:

    def __init__(self, length, complexity):
        self.length = length
        self.complexity = complexity
        self.password = ""

    def generate_password(self):
        if self.complexity == 'simple':
            # Simple password: only letters
            characters = string.ascii_letters
        elif self.complexity == 'medium':
            # Medium password: letters and digits
            characters = string.ascii_letters + string.digits
        elif self.complexity == 'strong':
            # Strong password: letters, digits, and punctuation
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            return "Invalid complexity choice. Choose 'simple', 'medium', or 'strong'."
        
        # Randomly select characters to generate password
        self.password = ''.join(random.choice(characters) for _ in range(self.length))
        return self.password


if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            complexity = input("Enter the desired complexity (simple, medium, strong): ").strip().lower()

            password_generator = PasswordGenerator(length, complexity)
            password = password_generator.generate_password()

            if password:
                print(f"Generated Password: {password}")
            
        except ValueError:
            print("Please enter a valid number for the password length.")
        
        continue_generation = input("Do you want to generate another password? (Y/N): ").strip().lower()
        if continue_generation != 'y':
            break
