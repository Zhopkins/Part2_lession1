'''
1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
'''
import re
from collections import Counter

# 1. Получите текст из файла
f = open('sometext.txt', 'r', encoding='utf-8')
readtext = f.read()

# 2. Разбейте текст на предложения.
# Отдельные предложения можно сплитануть через символ точки

readtext = re.split('\.\s', readtext) # разделяем текст по последовательности точки и пробельного символа за ним
print(readtext)

# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
list = []
my_pattern = re.compile('[А-Яа-я]{4,}') # создаем объект, в котором хранится шаблон. Он ищет русские слова из 4 букв и более
for words in readtext:
    list += my_pattern.findall(words)
list = [x.lower() for x in list] #нижний регистр
print(list)
wordsset = set(list)
popularwords = {}
for word in wordsset:
    popularwords[word] = list.count(word)
popularwords = sorted(popularwords.items(), reverse=True, key=lambda x: x[1] )
print(popularwords)


# 4. Отберите все ссылки.
links = []
links_pattern = re.compile('[A-Za-z0-9\.\/]+[a-z]')
for link in readtext:
    links += links_pattern.findall(link)

links = [x.lower() for x in links]
print(links)

# 5. Ссылки на страницы какого домена встречаются чаще всего?
domains = []
for link in links:
    domains.append(link.split('/')[0])
popular_domain = max(domains, key=domains.count)
print('Чаще всего встречается:', popular_domain)

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
onlyreg = []
reg_pattern = re.compile('[A-Za-z0-9\.\/]+[a-z0-9]')
for link in readtext:
    onlyreg.append(reg_pattern.sub('«Ссылка отобразится после регистрации»', link))
print(onlyreg)
