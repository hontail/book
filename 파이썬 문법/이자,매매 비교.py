Victory = 50000000
bank = 0

while True:
    for i in range (1,29):
        bank = Victory * ((1.12) ** i)

    if bank > 1100000000:
        bank = bank - 1100000000
        print(f"{int(bank)}원 차이로 동일 아저씨 말씀이 맞습니다.")
        break
    else:
        bank = 1100000000 - bank
        print(f"{int(bank)}원 차이로 미란 아주머니 말씀이 맞습니다.")
        break
#처음 돈 5천만원을 1년간 1.12%이자 붙는게 이득인지 매매로 존버하는게 이득인지 비교
