n = 10
sum_even = 0
sum_even_two = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
        sum_even_two += i

print(sum_even)
print(sum_even_two)