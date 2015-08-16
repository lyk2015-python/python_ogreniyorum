from str_util import utils

print(utils.is_palindrome("ece"))  # True
print(utils.is_palindrome("ecem"))  # False

print(utils.gen_word(["a", "b", "c"], 5))  # abaca
print(utils.gen_word(["a", "b", "c"], 5))  # ccbaa

print(utils.is_url("http://www.google.com/"))  # True "http://" "www." "/"
print(utils.is_url("ftp://google.com"))  # False

print(utils.title_make("bak bunu dedim"))  # Bak Bunu Dedim

try:
    print(utils.zip_str("baba akü yok", "akü hiç yok"))  # Error
except utils.UtilException as e:
    print(e)

print(utils.zip_str("baba akü yo", "akü hiç yok"))  # baakbüa  haikçü  yyook
