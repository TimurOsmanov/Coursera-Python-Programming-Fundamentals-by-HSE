import sys
# Во входном файле (вы можете читать данные из sys.stdin,
# подключив библиотеку sys) записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
data_in = open('input.txt', 'r', encoding='utf8')
sys.stdin, set1, sum_str = data_in, set(), str()
for line in sys.stdin:
    a = line.strip().split()
    for now in a:
        set1.add(now)
print(len(set1))
