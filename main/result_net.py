import sys


def test_list_IPv4(test_list):
    # Проверяем, что файл не пустой
    if len(test_list) == 0:
        raise ValueError("Файл пустой")
    # Запускаем цикл построчной проверки файла с получением номера строки
    for ind, line in enumerate(test_list):
        # Делим каждую строку с IP адресом на блоки
        temp = line.split(".")
        # Проверяем, что все IP состоят из 4 блоков
        if len(temp) == 4:
            # Проверяем, что все блоки IP адресов только из чисел
            if temp[0].isdigit() and temp[1].isdigit() and temp[2].isdigit() and temp[3].isdigit():
                # Проверяем, что числа блоков подходят по значению для IPv4
                if 0 <= int(temp[0]) < 256 and 0 <= int(temp[1]) < 256 and 0 <= int(temp[2]) < 256 and 0 <= int(
                        temp[3]) < 256:
                    pass
                else:
                    raise ValueError("Не все блоки IP адресов попадают в границы. На строке: {0}".format(ind + 1))
            else:
                raise ValueError("Не все адреса состоят из цифр. На строке: {0}".format(ind + 1))
        else:
            raise ValueError("Неправильное количество блоков в IP адресе. На строке: {0}".format(ind + 1))


def final_address_IPv4(final_list):
    temp = []
    # Запускаем цикл построчной проверки файла с получением номера строки
    for line in final_list:
        # Делим каждую строку с IP адресом на блоки и пишем в общий список
        temp += line.split(".")
    # Записываем каждый четвертый блок с первого элемента
    one_temp_items = temp[0::4]
    # Записываем каждый четвертый блок со второго элемента
    two_temp_items = temp[1::4]
    # Записываем каждый четвертый блок с третьего элемента
    three_temp_items = temp[2::4]
    # Записываем каждый четвертый блок с четвертого элемента
    fourth_temp_items = temp[3::4]
    # Перебираем списки, чтобы содержимое стало целочисленным и в дальнейшем у нас верно отрабатывали min max
    for i in range(len(one_temp_items)):
        one_temp_items[i] = int(one_temp_items[i])
        two_temp_items[i] = int(two_temp_items[i])
        three_temp_items[i] = int(three_temp_items[i])
        fourth_temp_items[i] = int(fourth_temp_items[i])
    # Запускаем цикл проверки разности значений в блоке
    for i in range(len(final_list)):
        # Проверяем разность в первом блоке
        if one_temp_items[i] != one_temp_items[0]:
            # Считаем количество адресов
            count_sub = (max(one_temp_items) - min(one_temp_items) + 1) * 256 * 256 * 256
            for j in range(33):
                if count_sub <= 2 ** j:
                    pref = 32 - j
                    break
            # Возвращаем подсеть с префиксом
            return 'Result net: 0.0.0.0/%s' % (pref)
    # Запускаем цикл проверки разности значений в блоке
    for i in range(len(final_list)):
        # Проверяем разность во втором блоке
        if two_temp_items[i] != two_temp_items[0]:
            # Считаем количество адресов
            count_sub = (max(two_temp_items) - min(two_temp_items) + 1) * 256 * 256
            for j in range(33):
                if count_sub <= 2 ** j:
                    pref = 32 - j
                    break
            # Возвращаем подсеть с префиксом
            return 'Result net: %s.0.0.0/%s' % (one_temp_items[0], pref)
    # Запускаем цикл проверки разности значений в блоке
    for i in range(len(final_list)):
        # Проверяем разность в третьем блоке
        if three_temp_items[i] != three_temp_items[0]:
            # Считаем количество адресов
            count_sub = (max(three_temp_items) - min(three_temp_items) + 1) * 256
            for j in range(33):
                if count_sub <= 2 ** j:
                    pref = 32 - j
                    break
            # Возвращаем подсеть с префиксом
            return 'Result net: %s.%s.0.0/%s' % (one_temp_items[0], two_temp_items[0], pref)
    # Запускаем цикл проверки разности значений в блоке
    for i in range(len(final_list)):
        # Проверяем разность в четвертом блоке
        if fourth_temp_items[i] != fourth_temp_items[0]:
            # Считаем количество адресов
            count_sub = (max(fourth_temp_items) - min(fourth_temp_items) + 3)
            for j in range(33):
                if count_sub <= 2 ** j:
                    pref = 32 - j
                    break
            # Возвращаем подсеть с префиксом
            return 'Result net: %s.%s.%s.0/%s' % (one_temp_items[0], two_temp_items[0], three_temp_items[0], pref)


# Функция пересчета в двоичную систему
def hex_to_bin(tuple_temp):
    # Цикл для приведения блоков адресов в четырехзначный вид
    for i in range(len(tuple_temp)):
        if len(str(tuple_temp[i])) == 1:
            re_temp_item = "000" + str(tuple_temp[i])
            tuple_temp[i] = re_temp_item
        elif len(str(tuple_temp[i])) == 2:
            re_temp_item = "00" + str(tuple_temp[i])
            tuple_temp[i] = re_temp_item
        elif len(str(tuple_temp[i])) == 3:
            re_temp_item = "0" + str(tuple_temp[i])
            tuple_temp[i] = re_temp_item
    # Цикл для приведения блоков адресов из четырехзначного вида в шестнадцатизначный
    for i in range(len(tuple_temp)):
        rej_temp_item = ""
        for j in range(4):
            if tuple_temp[i][j] == "0":
                rej_temp_item += "0000"
            elif tuple_temp[i][j] == "1":
                rej_temp_item += "0001"
            elif tuple_temp[i][j] == "2":
                rej_temp_item += "0010"
            elif tuple_temp[i][j] == "3":
                rej_temp_item += "0011"
            elif tuple_temp[i][j] == "4":
                rej_temp_item += "0100"
            elif tuple_temp[i][j] == "5":
                rej_temp_item += "0101"
            elif tuple_temp[i][j] == "6":
                rej_temp_item += "0110"
            elif tuple_temp[i][j] == "7":
                rej_temp_item += "0111"
            elif tuple_temp[i][j] == "8":
                rej_temp_item += "1000"
            elif tuple_temp[i][j] == "9":
                rej_temp_item += "1001"
            elif tuple_temp[i][j] == "a":
                rej_temp_item += "1010"
            elif tuple_temp[i][j] == "b":
                rej_temp_item += "1011"
            elif tuple_temp[i][j] == "c":
                rej_temp_item += "1100"
            elif tuple_temp[i][j] == "d":
                rej_temp_item += "1101"
            elif tuple_temp[i][j] == "e":
                rej_temp_item += "1110"
            elif tuple_temp[i][j] == "f":
                rej_temp_item += "1111"
        tuple_temp[i] = rej_temp_item
    return tuple_temp


def norm_len_temp_ipv6(norm_len_temp):
    while len(norm_len_temp) != 8:
        norm_len_temp = norm_len_temp + [""]
        for i in range(len(norm_len_temp) - 1, 1, -1):
            norm_len_temp[i] = norm_len_temp[i - 1]
    for i in range(len(norm_len_temp)):
        if norm_len_temp[i] == "":
            norm_len_temp[i] = 0
    return norm_len_temp


def test_list_IPv6(list):
    # Проверяем, что файл не пустой
    if len(list) == 0:
        raise ValueError("Файл пустой")
    # Запускаем цикл построчной проверки файла с получением номера строки
    for ind, line in enumerate(list):
        # Делим каждую строку с IP адресом на блоки
        temp = line.split(":")
        # Проверяем, что все IP состоят из верного количества блоков
        if 2 <= len(temp) <= 8:
            # Дополним количество блоков, если оно было сокращено через ::
            temp = norm_len_temp_ipv6(temp)
            # Проверяем, что все блоки IP адресов из верных знаков
            spec_char = (".,:;!_*-+()/#¤%&)")
            if (set(spec_char).isdisjoint(str(temp[0])) and set(spec_char).isdisjoint(str(temp[1]))
                    and set(spec_char).isdisjoint(str(temp[2])) and set(spec_char).isdisjoint(str(temp[3]))
                    and set(spec_char).isdisjoint(str(temp[4])) and set(spec_char).isdisjoint(str(temp[5]))
                    and set(spec_char).isdisjoint(str(temp[6])) and set(spec_char).isdisjoint(str(temp[7]))):
                # Вызываем функцию для пересчета в двоичную систему
                temp = hex_to_bin(temp)
                # Проверяем, что числа блоков подходят по значению для IPv6
                if (((0 <= int(temp[0]) < int("1111111111111111") and 0 <= int(temp[1]) < int("1111111111111111")
                      and 0 <= int(temp[2]) < int("1111111111111111")) and 0 <= int(temp[3]) < int("1111111111111111")
                     and 0 <= int(temp[4]) < int("1111111111111111")) and 0 <= int(temp[5]) < int("1111111111111111")
                    and 0 <= int(temp[6]) < int("1111111111111111")) and 0 <= int(temp[7]) < int("1111111111111111"):
                    pass
                else:
                    raise ValueError("Не все блоки IP адресов попадают в границы. На строке: {0}".format(ind + 1))
            else:
                raise ValueError("Не все адреса состоят из верных знаков. На строке: {0}".format(ind + 1))
        else:
            raise ValueError("Неправильное количество блоков в IP адресе. На строке: {0}".format(ind + 1))


def final_address_IPv6(final_list_ipv6):
    # Объявим список по размеру на весь следующий цикл
    adr = [None] * len(final_list_ipv6)
    # Обьявим переменную для последующего рассчета префикса
    adr_bit = 48
    # Запускаем цикл построчной проверки файла с получением номера строки
    for ind, line in enumerate(final_list_ipv6):
        # Делим каждую строку с IP адресом на блоки и пишем в общий список
        # После обработаем наши адреса в функциях, для удобного бинароного вида
        # И запишем лишь интересующий нас блок и 1 адерс, чтоб знать как формировать префикс и подсеть
        adr[ind] = hex_to_bin(norm_len_temp_ipv6(line.split(":")))[4]
        temp = hex_to_bin(norm_len_temp_ipv6(line.split(":")))
        # А так же оставим вариант в исходном виде из файла с уже сокращенными нулями
        adr_subnet = line.split(":")
    # Первые 3 блока мы не будем брать, т.к. они по умолчанию неприкасаемые
    # И уже являются неотъемлемой частью подсети
    # Ибо в ирл они выданы провайдером и при нашей задаче они 100% будут идентичны
    # Далее можно уже и посмотреть меняется ли что-то и на основании этого определять подсеть и префикс
    # Т.к. эти пересчеты сложные и нудные и в нашем случае не особо практичны, перейдем сразу к блоку где
    # Есть разность адресов и посчитаем на нем, упростим жизнь для решения конкретной задачи
    # Запишем самый большой адрес в в нужный блок будущей подсети
    temp[4] = max(adr)
    # Сотрем содержимое списка для его последующего использования
    adr = ""
    # Запустим цикл посимвольной перекладки нашего адреса в переменную
    for i in range(len(temp)):
        adr += temp[i]
    # Запустим цикл посимвольного перебора нашего адреса будущей подсети,
    # Пропустив первые 48 бит, чтобы получить префикс
    for i in range(48, len(adr)):
        if int(adr[i]) != 1:
            adr_bit += 1
        else:
            break
    # Возвращаем подсеть с префиксом
    return 'Result net: %s::/%s' % (adr_subnet[0], adr_bit)


def file_processing(name_file, version):
    try:
        if version == "4":
            with open(name_file) as IPv4:
                myListIPv4 = [line.rstrip() for line in IPv4]
            if test_list_IPv4(myListIPv4) == None:
                print(final_address_IPv4(myListIPv4))
                # Для тестов
                return final_address_IPv4(myListIPv4)
        elif version == "6":
            with open(name_file) as IPv6:
                myListIPv6 = [line.rstrip() for line in IPv6]
            if test_list_IPv6(myListIPv6) == None:
                print(final_address_IPv6(myListIPv6))
        else:
            print(("Файл " + name_file + " не найден"))
    except OSError:
        raise ValueError("Файл " + name_file + " не найден")


if __name__ == "__main__":
    file_processing(sys.argv[1], sys.argv[2])
