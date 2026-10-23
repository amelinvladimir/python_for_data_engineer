# Преобразование строки в дату

# Даты из CSV, JSON и баз данных часто приходят в виде строк.
from datetime import datetime

value = "2026-10-22 14:30:00"

dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

print(dt.year)
print(dt.month)
print(dt.hour)


# Основные обозначения:
# - %Y — год из четырёх цифр;
# - %m — месяц;
# - %d — день;
# - %H — часы в 24-часовом формате;
# - %M — минуты;
# - %S — секунды.

# Для преобразования даты в строку используется strftime():

print(dt.strftime("%d.%m.%Y"))