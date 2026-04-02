solar1 = ["태양","수성","금성","지구","화성",'목성','토성','천왕성','해왕성']
solar2 = ['sun','mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
solardict = {}
for i,k in enumerate(solar1): #인덱스랑 값을 같이 저장
    val = solar2[i] #val에 solar2의 i인덱스값을 저장
    solardict[k] = val #빈 사전에 행성이름을 키값 행성인덱스를 값으로 저장

print(solardict) 
