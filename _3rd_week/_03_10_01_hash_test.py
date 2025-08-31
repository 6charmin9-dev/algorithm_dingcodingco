print(hash("fast")) # 4123940003881077006 ... 변경 됨 # 파이썬은 보안상의 이유로 **기본 문자열/바이트/기타 객체의 해시값을 프로세스마다 무작위 시드(seed)**로 초기화 
print(hash("slow")) # 3984015825197101194 ... 변경 됨 
print(hash("fast")) # 1라인과 값이 같음 
'''
Hash DoS 공격 방어
악의적인 사용자가 해시 충돌을 많이 일으켜 딕셔너리 성능을 떨어뜨리는 공격을 막기 위해
'''
items = [None] * 10
items[hash("fast") % len(items)] = "빠른"
print(items[hash("fast") % len(items)])