# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

nums = [1, 2, 3, 2, 1, 4, 8, 1]

result = []

for i in nums:
    if nums.count(i) > 1 and i not in result:
        result.append(i)

print(result)
