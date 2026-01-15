import random

def main():
    password = input("Enter your password: ")
    print()

    if len(password) < 9:
        print("Password too short.")
        return

    # Assume success is True until proven False
    success = True

    for i in range(3):
        index = random.randint(0, len(password) - 1)
        
        user_char = input(f"Enter letter at position {index + 1}: ")
        
        if user_char != password[index]:
            print("Incorrect\n")
            success = False 
            break 
        else:
            print("Correct\n")

    if success:
        print("Security check passed.")
    else:
        print("Security check failed.")

if __name__ == "__main__":
    main()