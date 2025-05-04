def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом, игнорируя пробелы и знаки пунктуации.

    Args:
        text: Строка для проверки.

    Returns:
        True, если строка является палиндромом, иначе False.
    """
    processed_string = ''.join(filter(str.isalnum, text)).lower()
    return processed_string == processed_string[::-1]

# Тесты
assert is_palindrome("Лёша на полке клопа нашёл") == True  # Пример из задания
assert is_palindrome("казак") == True  # Простое слово-палиндром
assert is_palindrome("A man, a plan, a canal: Panama") == True  # Фраза с пунктуацией и пробелами
assert is_palindrome("Madam, I'm Adam") == True # Фраза со знаками препинания и разным регистром
assert is_palindrome("12321") == True # Цифровой палиндром
assert is_palindrome("hello") == False # Не палиндром
assert is_palindrome("World") == False # Не палиндром
assert is_palindrome("") == True  # Пустая строка - палиндром
assert is_palindrome("w") == True # одна буква - палиндром
assert is_palindrome("Racecar") == True

