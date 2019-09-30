import random

MONTH = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')


def generate_month(month):
    return MONTH[month], random.randrange(0, 46, 2)


def generate_year(year):
    months = {}
    for month in range(0, 12):
        name, avg = generate_month(month)
        months.update({name: avg})
    return {year: months}


def min_max_temperature(temperatures):
    return min(temperatures), max(temperatures)


def get_user_input_year():
    return int(input('Type a year from the registry: '))


def main():
    registry = {}

    registry.update(generate_year(2000))
    registry.update(generate_year(2001))
    registry.update(generate_year(2002))
    print(registry)

    input_year = get_user_input_year()
    if registry.get(input_year) is None:
        print(f'This year {input_year} does not exist in our system.')
    else:
        min_max_year = min_max_temperature(registry.get(input_year).values())
        print(f'Minimum temperature: {min_max_year[0]}', f'Maximum temperature: {min_max_year[1]}', sep='\n')


if __name__ == "__main__":
    main()
