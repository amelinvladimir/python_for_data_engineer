import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Создаём исходные данные
data = {
    'customer_id': [
        1, 1, 1, 2, 2, 2, 3, 3, 3,
        4, 4, 4, 5, 5, 5, 6, 6, 6,
        7, 7, 7, 8, 8, 8, 9, 9, 9
    ],
    'customer_category': [
        'Мелкий', 'Мелкий', 'Мелкий',
        'Мелкий', 'Мелкий', 'Мелкий',
        'Мелкий', 'Мелкий', 'Мелкий',
        'Средний', 'Средний', 'Средний',
        'Средний', 'Средний', 'Средний',
        'Средний', 'Средний', 'Средний',
        'Крупный', 'Крупный', 'Крупный',
        'Крупный', 'Крупный', 'Крупный',
        'Крупный', 'Крупный', 'Крупный'
    ],
    'product_category': [
        'Электроника', 'Одежда', 'Продукты',
        'Одежда', 'Продукты', 'Продукты',
        'Электроника', 'Одежда', 'Продукты',
        'Электроника', 'Одежда', 'Мебель',
        'Одежда', 'Продукты', 'Продукты',
        'Электроника', 'Одежда', 'Мебель',
        'Электроника', 'Мебель', 'Мебель',
        'Электроника', 'Одежда', 'Мебель',
        'Электроника', 'Электроника', 'Мебель'
    ],
    'quantity': [
        1, 3, 5,
        2, 4, 6,
        1, 2, 8,
        5, 3, 2,
        4, 6, 5,
        7, 3, 4,
        10, 8, 6,
        12, 2, 9,
        15, 10, 11
    ]
}

df = pd.DataFrame(data)

print('Исходные данные:')
print(df.head(10))


# 2. Формируем сводную таблицу
# Считаем общее количество купленных товаров
pivot = pd.crosstab(
    index=df['customer_category'],
    columns=df['product_category'],
    values=df['quantity'],
    aggfunc='sum'
)

# Задаём правильный порядок категорий клиентов
pivot = pivot.reindex(['Мелкий', 'Средний', 'Крупный'])

print('\nКоличество купленных товаров:')
print(pivot)


# 3. Строим heatmap по абсолютным значениям
plt.figure(figsize=(9, 5))

sns.heatmap(
    pivot,
    annot=True,
    fmt='.0f',
    cmap='YlGnBu',
    linewidths=0.5
)

plt.title('Количество покупок по категориям клиентов')
plt.xlabel('Категория товара')
plt.ylabel('Категория клиента')
plt.tight_layout()
plt.show()


# 4. Рассчитываем долю каждой категории товаров
pivot_percent = pivot.div(
    pivot.sum(axis=1),
    axis=0
) * 100

print('\nСтруктура покупок в процентах:')
print(pivot_percent.round(1))


# 5. Строим heatmap по процентам
plt.figure(figsize=(9, 5))

sns.heatmap(
    pivot_percent,
    annot=True,
    fmt='.1f',
    cmap='YlGnBu',
    linewidths=0.5,
    vmin=0,
    vmax=100
)

plt.title('Структура покупок по категориям клиентов (%)')
plt.xlabel('Категория товара')
plt.ylabel('Категория клиента')
plt.tight_layout()
plt.show()



pivot_percent.plot(
    kind='bar',
    figsize=(12, 6),
    width=0.8
)

plt.title('Предпочтения клиентов по категориям товаров')
plt.xlabel('Категория клиента')
plt.ylabel('Доля покупок, %')
plt.xticks(rotation=0)
plt.legend(title='Категория товара')
plt.tight_layout()
plt.show()