def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string or number: ")
    if is_palindrome(user_input):
        print(f"✅ '{user_input}' is a palindrome!")
    else:
        print(f"❌ '{user_input}' is not a palindrome.")
