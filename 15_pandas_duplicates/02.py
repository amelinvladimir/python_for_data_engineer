# Дубликаты

# Дубликаты могут возникнуть при повторной загрузке данных, ошибках интеграции или повторной отправке события.

import pandas as pd

sales = pd.DataFrame({
    "city": ["Москва", "Москва", "Тверь", "Тверь"],
    "month": ["Январь", "Январь", "Январь", "Январь"],
    "revenue": [100000, 100000, 40000, 50000]
})

print(sales.duplicated())
print(sales.duplicated().sum())
print(sales.drop_duplicates())

# Если уникальность определяется не всей строкой, а идентификатором события, нужно указать ключ:

print(sales.duplicated(subset=["city", "month"]))
print(sales.drop_duplicates(subset=["city", "month"]))

# Важно понять, какие записи нужно удалить, а какие нет, то есть по какому набору полей могут быть дубли, а по какому нет

# Можем явно указать, какую из дублирующих строк оставить при удалении дубликатов 
print(sales.drop_duplicates(subset=["city", "month"], keep="first"))