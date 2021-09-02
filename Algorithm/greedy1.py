##첫 번째 방법
#배열의 크기 , 숫자가 더해지는 횟수 , 연속가능횟수
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# result = 0

# while True:
#   for i in range(k):
#     if(m==0):
#       break
#     result += first
#     m -=1

#   if (m==0):
#     break
#   result += second
#   m -=1

# print(result)

##두 번째 방법
# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)
