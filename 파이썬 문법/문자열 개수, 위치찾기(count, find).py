txt = 'a lot of things occur each day, every day'
word_count = txt.count('l')
print(word_count) #l이 몇 개 있는지 카운트

word_find = txt.find('lot')
print(word_find) #lot이 몇번째 인덱스에 있는지 셈 l이 인덱스2에 있으니 인덱스 2 리턴

word_find = txt.find('day',30) #day가 2개 있는데 ,30은 인데스30 이후 day를 찾으라는 뜻 
print(word_find)
