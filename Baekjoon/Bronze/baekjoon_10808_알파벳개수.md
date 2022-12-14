# [알파벳 개수](https://www.acmicpc.net/problem/10808)

```python
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = input()
B = [0] * 26

for idx, a in enumerate(A):
    B[idx] = S.count(a)

print(*B)
```

- 별다른 규칙이 없는 짧은 리스트 만들때는 그냥 만드는 게 나을 것 같아서 알파벳 리스트를 만들었다
- count 함수 쓸 생각을 못해서 반복문 한 번 더 쓸 뻔 했다


# 아스키 코드 활용한 다른 풀이

## 아스키 코드

- 영문 알파벳을 사용하는 대표적인 문자 인코딩
- 알파벳 a의 아스키 코드 값이 97인 점을 이용해 인덱스 값으로 재활용
- `ord()` 와 `chr()` 두 가지 함수를 통해 알파벳과 숫자 값 서로 변환 가능

```python
S = input()
A = [0] * 26

for s in S:
    A[ord(s) - 97] += 1

print(*A)
```
- 문자열 각 문자의 아스키코드 값에서 97을 빼면 알파벳 순서대로 나열되고 자동으로 인덱스 값으로 배치
- 카운트가 필요 없다, 앞의 a와 뒤의 a가 각자 자기 아스키코드 -> 인덱스 값을 통해 +1 해주는 방식
- 대신 값을 담을 리스트를 생성해줘야 했고 값을 더해줘야 했기때문에 정수형의 26칸짜리 리스트를 먼저 생성
  

## 배운 점
- 리스트를 대괄호 없이 출력할 때는 `print(*list)` 방식 이용
- 리스트 내에서 같은 문자열 찾을 때는 `count()` 사용
- 알파벳 문제가 나올 때는 아스키 코드를 먼저 떠올릴 것