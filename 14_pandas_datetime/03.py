# Наивная дата и дата с временной зоной

# Объект datetime может быть двух видов:
# - naive — не содержит информацию о временной зоне;
# - aware — содержит информацию о временной зоне.

from datetime import datetime, timezone

naive = datetime(2026, 10, 22, 14, 30)
aware = datetime(2026, 10, 22, 14, 30, tzinfo=timezone.utc)

print(naive.tzinfo)  # None
print(aware.tzinfo)  # UTC

# Время 14:30 без временной зоны нельзя однозначно интерпретировать как конкретный момент времени.