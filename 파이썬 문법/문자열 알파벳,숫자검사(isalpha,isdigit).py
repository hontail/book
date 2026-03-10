txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcragt Three'
txt4 = '4po'
re1 = txt1.isalpha() #True출력 
ret2 = txt2.isalpha() #True출력 문자열로만 구성되어 있는지 확인하기 때문 
ret3 = txt3.isalpha() #False 띄어쓰기 있어서
ret4 = txt4.isalpha() #False 숫자 4

txt1 = '010-6443-3333'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit() #False출력 하이픈이 포함돼서
ret2 = txt2.isdigit() #알파벳이 포함돼서
ret3 = txt3.isdigit() #True출력

#알파벳 또는 숫자인지 확인 .isalnum() 쓰면됨
