def insert(arr, dim):
    alg_count = [0, 0]              # список из 2-ч элементов для хранения показателей эффективности
    
    for i in range(1, dim):         # Основной цикл со 2-го элемента право 
        temp = arr[i]               # Запомним элемент для сравнения 
        j = i - 1
        while j >= 0:               # Ищем влево ближайший меньший  
            alg_count[0] += 1       # Считаем операции сравнения 
            if arr[j] > temp:
                alg_count[1] += 1   # Считаем операции перестановки 
                arr[j+1] = arr[j]   # Сдвигаем элемент влево, а на его место ставим наименьший
                arr[j] = temp
            j -= 1       
    return alg_count                #a = [2,4,6,3,5,10,15,23,12,11]
                                    #b = 10
