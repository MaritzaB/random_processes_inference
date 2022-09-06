import datetime

birthdate = input(
    "Introduce la fecha en formato dd-mm-yyyy: "
)
date = datetime.datetime.strptime(birthdate, "%d-%m-%Y")

day = int(date.day)
monthh = int(date.month)
year = int(date.year)

a = (14 - monthh) // 12
y = year - a
m = monthh + 12 * a - 2

d = (
    day
    + y
    + (y // 4)
    - (y // 100)
    + (y // 400)
    + (31 * m) // 12
) % 7

weekday = {
    0: "domingo",
    1: "lunes",
    2: "martes",
    3: "miercoles",
    4: "jueves",
    5: "viernes",
    6: "s'abado",
}

value = weekday[d]

print(f"El d'ia {date} cae en ", value)
