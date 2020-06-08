
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    text2 = ''
    for i in range(0, len(something)):
        if text[i] != ' ':
            text2 += text[i]
    return text2 == reverse(text2)


something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
