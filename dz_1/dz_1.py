import csv


def get_hierarchy():
    """Открывает csv, получает и выводит словарь {Департамент: {отделы} } """
    with open('dz_1/Corp_Summary.csv', 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=';')

        line_count = 0
        hierarchy = dict()

        for row in csvreader:
            if line_count == 0:
                line_count += 1
                continue
            department, branch = row[1], row[2]
            if department not in hierarchy:
                hierarchy[department] = set()
            hierarchy[department].add(branch)

        for department in hierarchy:
            branches = ', '.join(str(br) for br in hierarchy[department])

            print(f'Департамент: {department}')
            print(f'Отделы: {branches}')
            print('')


def get_report():
    """Возвращает сводный отчёт по департаментам:"""
    with open('dz_1/Corp_Summary.csv', 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=';')

        line_count = 0
        report = dict()

        for row in csvreader:
            if line_count == 0:
                line_count += 1
                continue
            department, salary = row[1], int(row[5])
            if department not in report:
                report[department] = [department, 0, 1000 ** 10, 0, 0]
            report[department][1] += 1
            report[department][2] = min(report[department][2], salary)
            report[department][3] = max(report[department][3], salary)
            report[department][4] += salary

        return report


def print_report():
    """Выводит сводный отчёт по департаментам:"""
    report = get_report()

    for department in report:
        name = report[department][0]
        number = report[department][1]
        min_salary = report[department][2]
        max_salary = report[department][3]
        avg_salary = report[department][4] // number
        print(f'Департамент - {name}, количество сотрудников: {number} \n'
              f'Вилка: {min_salary} - {max_salary},'
              f' Средняя зарплата: {avg_salary} \n')


def save_report():
    """Сохраняет сводный отчет в csv файл"""
    report = get_report()

    with open('dz_1/report.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ['Департамент', 'Количество сотрудников',
                  'Минимальная Зарплата', 'Максимальная зарплата',
                  'Средняя зарплата']

        writer.writerow(header)
        for department in report:
            name = report[department][0]
            number = report[department][1]
            min_salary = report[department][2]
            max_salary = report[department][3]
            avg_salary = report[department][4] // number
            data = [name, number, min_salary, max_salary, avg_salary]
            writer.writerow(data)


print('Меню\n'
      '1. Вывести иерархию команд\n'
      '2. Вывести сводный отчёт по департаментам\n'
      '3. Сохранить сводный отчёт')

answer = input()
while answer not in ('1', '2', '3'):
    print('Введите 1, 2 или 3')
    answer = input()

if answer == '1':
    get_hierarchy()

if answer == '2':
    print_report()

if answer == '3':
    save_report()
