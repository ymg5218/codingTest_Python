# 1339

'''
가장 자리수가 큰 수에게 무조건 큰 값어치를 부여하려 했으나, 예외의 경우가 있었음
ABB, BB, BB, BB, BB, BB, BB, BB, BB, BB일 때, 가장 큰 자리수인 A에 9를 주는 것 보다, B에게 9를 주는게 더 큰 합이 됨.

내 예상 풀이
1. 각 알파벳의 현재 자리수에 값어치를 부여함.
ex) ABCDE, EFG, EHIJ
A : 10**4
B : 10**3
C : 10**2
D : 10**1
E : 10**0 + 10**2 * 10**3
F : 10**1
G : 10**0
H : 10**2
I : 10**1
J : 10**0
이렇게 정리하면, 각 자리수가 차지하는 가중치의 상대 값을 추정할 수 있음.
E와 B는 같은 자릿수에 위치하지만, E가 B보다 더 가중치가 높다는 사실을 해당 정리를 통해 알 수 있음.

이 방식으로 정리하면 위에서 예시로 든 예외도 다음과 같이 정리되어 B가 더 가중치가 높다는 사실을 알 수있음

A : 100, B : 110

2. 가중치가 높은 순서부터 ( 해당 가중치 * 부여할 수 있는 최대 수 )를 합산한다.
만약 C : 100, H : 100으로 가중치가 같아도, C 가중치에 n을 곱하고 H 가중치에 n-1을 곱하여 합산하나, 반대로 하나 결과는 같다.
    => 같은 가중치끼리의 우선순위는 중요하지 않다
가중치가 가장 높은 값은 max() 메소드로 가져오며, 가져왔던 값 위치엔 -1을 삽입하여 참조했음을 알린다.

3. 모든 유효한 알파벳에 대한 가중치를 참조했다면 리스트의 최종 값은 0 (유효하지 않은 알파벳. 삽입도 참조도 한 적 없음) 이거나 -1( 가중치를 참조함 ) 이다.
모든 요소의 값이 0 이하라면 반복문을 종료하고 합산한 값을 출력하면 끝
'''
N = int(input())

alpha = [0] * 26 # 어느 알파벳이 올 지 모른다. 

for _ in range(N):
    word = input()
    word_len = len(word)
    for idx in range(word_len):
        alpha[ord(word[idx]) - 65] += 10**(word_len-(idx+1)) # 아스키코드 값 -65로 각 알파벳 가중치를 담을 인덱스를 캐낸다.

max_value = 0 # 합을 담을 변수. 최댓값을 출력해야 함
num = 9 # 각 자리수가 가질 수 있는 최대 가치

while(max(alpha) > 0): # 모든 유효한 알파벳에 대한 가중치를 참조할 때까지 반복한다.
   max_value += max(alpha) * num
   alpha[alpha.index(max(alpha))] = -1 # 최대 값어치를 지니는 알파벳(인덱스)은 산정했으니 -1로 변경
   num -= 1 # 산정 이후, 각 자리수가 가질 수 있는 최대 가치 

print(max_value)
   