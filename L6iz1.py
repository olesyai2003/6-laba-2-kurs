# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Название магазина (фильтр 2х)
# Название товара
# Стоимость
spisok_new = []


def table():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 6,
        '-' * 20,
        '-' * 30,
        '-' * 20
    )
    return line


def table_name():
    post = '| {:^6} | {:^20} | {:^30} | {:^20} | '.format(
        "№",
        "Название магазина",
        "Название товара",
        "Стоимость, руб."
    )
    return post


def table_name_fil(names):
    post = []
    for idx_new, spisok_new_new in enumerate(names, 1):
        post.append(
            '| {:>6} | {:<20} | {:<30} | {:<20} | '.format(
                idx_new,
                spisok_new_new.get('name_shop', ''),
                spisok_new_new.get('name_product', ''),
                spisok_new_new.get('prise', '')
            )
        )
    return post


def save_list_shop(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_list_shop(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    list_shop = []

    while True:
        command = input('>>> ').lower()

        if command == 'exit':
            break

        elif command == 'add':
            name_shop = input('Название магазина: ')
            name_product = input('Название товара: ')
            prise = input('Стоимость товара: ')

            list_shop_new = {
                'name_shop': name_shop,
                'name_product': name_product,
                'prise': prise
            }

            list_shop.append(list_shop_new)

            if len(list_shop) > 1:
                list_shop.sort(key=lambda item: item.get('name_shop', ''))

        elif command == 'list':
            print(table())
            print(table_name())
            print(table())
            for item_n in table_name_fil(list_shop):
                print(item_n)
            print(table())

        elif command == 'product':
            shop_sear = input('Введите название товара: ')
            search_shop = []
            for shop_sear_itme in list_shop:
                if shop_sear == shop_sear_itme['name_product']:
                    search_shop.append(shop_sear_itme)

            if len(search_shop) > 0:
                print(table())
                print(table_name())
                print(table())
                for item_f in table_name_fil(search_shop):
                    print(item_f)
                print(table())
            else:
                print('Такого товара не найдено', file=sys.stderr)

        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_list_shop(file_name, list_shop)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            list_shop = load_list_shop(file_name)

        elif command == 'help':
            print('Список команд:\n')
            print('add - добавить магазин.')
            print('list - вывести список магазинов.')
            print('product <Название> - запросить информацию о товаре.')
            print('help - Справочник.')
            print("load <Название файла без скобок> - загрузить данные из файла;")
            print("save <Название файла без скобок> - сохранить данные в файл;")
            print('exit - Завершить пработу программы.')
        else:
            print(f'Команда <{command}> не существует.', file=sys.stderr)
            print('Введите <help> для просмотра доступных команд')


if __name__ == '__main__':
    main()
