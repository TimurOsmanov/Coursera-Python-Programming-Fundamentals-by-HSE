# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
data_in = open('input.txt', 'r', encoding='utf8')
my_dict = dict()
for line in data_in:
    a = line.strip().split()
    for now in a:
        if now not in my_dict:
            my_dict[now] = 0
        else:
            my_dict[now] += 1
        print(my_dict[now], end=' ')
