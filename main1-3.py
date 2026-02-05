import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        user_pick = int(input("1부터 100까지의 숫자를 입력하시오."))
        if user_pick < random_number:
            print("업")
        elif user_pick > random_number:
            print("다운")
        elif user_pick == random_number:
            print(f"정답입니다. 컴퓨터의 숫자는{random_number}")
    
    except:
        print("정수를 입력하세요")
    
    game_count = game_count + 1