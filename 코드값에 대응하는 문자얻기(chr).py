val = input("문자 코드값을 입력하쇼")
val = int(val) #입력한 코드값을 정수로 다시 저장
try: #실행해라
    ch = chr(val) #chr은 ord()의 반대 개념 코드값을 해당하는 문자로 리턴
    print(f"코드값:{val}[{hex(val)}, 문자{ch}]")
except ValueError: #오류 예외 처리 ValueError발생시 실행
    print(f"입력한 {val}에 대한 문자가 존재하지 않습니다.")
