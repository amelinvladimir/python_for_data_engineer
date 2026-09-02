# Мы хотим обработать строки последовательно.
def process(line):
    line_ls = line.rstrip("\n").split(sep=',')
    try:
        if int(line_ls[1]) > 10000:
            print(line_ls)
    except ValueError:
        pass

with open("orders_sample.csv") as file:
    for line in file:
        process(line)

# Файл можно читать построчно, а не загружать целиком в память.