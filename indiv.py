#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Использовать словарь, содержащий следующие ключи:
# название пункта назначения; номер
# поезда; время отправления. Написать программу,
# выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны
# быть упорядочены по номерам маршрутов;
# вывод на экран информации о маршруте, номер которого
# введен с клавиатуры времени; если
# таких поездов нет, выдать на дисплей
# соответствующее сообщение

import sys

routes = []


def get_route():
    destination = input("Пункт назначения: ")
    number = input("Номер поезда: ")
    time = input("Время отправления: ")

    return {
        'destination': destination,
        'number': number,
        'time': time
    }


def display_routes(road):
    if road:
        line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 4,
                '-' * 20
        )
        print(line)
        print(
                '| {:^30} | {:^4} | {:^20} |'.format(
                    "Пункт назначения",
                    "№",
                    "Время"
                                            )
        )
        print(line)

        for route in road:
            print(
                '| {:<30} | {:>4} | {:<20} |'.format(
                    route.get('destination', ''),
                    route.get('number', ''),
                    route.get('time', '')
                )
            )
        print(line)

    else:
        print("Поезда не найдены")


def main():

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            route = get_route()

            routes.append(route)
            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            display_routes(routes)

        elif command == 'select':
            number2 = input("Выберите номер маршрута: ")
            number3 = int(number2.replace(':', ''))
            count = 0

            for route in routes:
                number1 = route.get('number')
                number1 = int(number1.replace(':', ''))
                if number1 == number3:
                    count += 1
                    print(
                        '{:>4} {} {}'.format("№" + route.get('number'),
                                             route.get('destination', ''),
                                             route.get('time'))
                        )

            if count == 0:
                print("Такие маршруты не найдены")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select - найти маршруты по времени")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
