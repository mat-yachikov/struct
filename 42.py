# Список для чисел
nums = []
# Пока количество чисел не достигло ста
while(len(nums) < 100):
    # Вводим число
    n = int(input())
    # Добавляем в список
    nums.append(n)
    # Если это число -42, то выводим все числа в обратном порядке
    if (nums[-1] == -42):
        nums.reverse()
        for i in range(len(nums)):
            print(nums[i], end=' ')
        # Реверсим еще раз, т.к. продолжаем записывать новые числа
        nums.reverse()
