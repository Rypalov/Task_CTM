import sys


# Переведем ip
def ip_to_int(a: int, b: int, c: int, d: int):
    return (a << 24) + (b << 16) + (c << 8) + d


# Произведем XOR над нашими адресами, чтобы посчитать маску
def masked(ip1: list, ip2: list):
    m = 0xFFFFFFFF ^ ip_to_int(*ip1) ^ ip_to_int(*ip2)
    block_one = (m & (0xFF << 24)) >> 24
    if block_one == 255:
        block_two = (m & (0xFF << 16)) >> 16
        if block_two == 255:
            block_three = (m & (0xFF << 8)) >> 8
            if block_three == 255:
                block_four = (m & (0xFF << 0)) >> 0
            else:
                block_four = 0
        else:
            block_three = 0
            block_four = 0
    else:
        block_two = 0
        block_three = 0
        block_four = 0
    return block_one, block_two, block_three, block_four


# Соберем минимальную подсеть
def sub_net(ip_list: list, mask: tuple):
    block: list = ["", "", "", ""]
    for i in range(1, 4):
        if mask[i] == 255:
            block[i] = ip_list[0][i]
        else:
            block[i] = 0
    if mask[0] == 0:
        block[0] = mask[0]
    elif mask[0] == 255:
        block[0] = ip_list[0][0]
    elif mask[0] < 128:
        block[0] = 0
    else:
        block[00] = mask[0] // 8 * 8
    return f"{block[0]}.{block[1]}.{block[2]}.{block[3]}"


# Посчитаем префикс по маске
def get_prefix(mask: tuple):
    prefix: int = 0
    for x in mask:
        x = bin(x)[2:]
        for xx in x:
            if xx == "1":
                prefix += 1
            else:
                break
    return prefix


def test_list_ipv4(test_list: list):
    status: bool = True
    try:
        # Проверяем, что файл не пустой
        if len(test_list) == 0:
            raise ValueError
        # Запускаем цикл построчной проверки файла с получением номера строки
        for ind, line in enumerate(test_list):
            # Делим каждую строку с IP адресом на блоки
            temp = line.split(".")
            try:
                # Проверяем, что все IP состоят из 4 блоков
                if len(temp) != 4:
                    raise ValueError
                try:
                    # Проверяем, что все блоки IP адресов только из чисел
                    if not (temp[0].isdigit() and temp[1].isdigit() and temp[2].isdigit() and temp[3].isdigit()):
                        raise ValueError
                    try:
                        # Проверяем, что числа блоков подходят по значению для IPv4
                        if not (0 <= int(temp[0]) < 256 and 0 <= int(temp[1]) < 256 and 0 <= int(temp[2]) < 256 and 0 <= int(temp[3]) < 256):
                            raise ValueError
                        else:
                            if status:
                                status = True
                    except ValueError:
                        print(f"Не все блоки IP адресов попадают в границы. На строке: {ind + 1}. IP: {line}")
                        status = False
                except ValueError:
                    print(f"Не все адреса состоят из цифр. На строке: {ind + 1}. IP: {line}")
                    status = False
            except ValueError:
                print(f"Неправильное количество блоков в IP адресе. На строке: {ind + 1}. IP: {line}")
                status = False
    except ValueError:
        print("Файл пустой")
        status = False
    return status


def final_address_ipv4(final_list: list):
    # Создадим список, который будет хранить наши IP в блоках побитово
    list_block: list = [[0 for x in range(4)] for y in range(len(final_list))]
    # Заполним оба списка
    for k, line in enumerate(final_list):
        for kk, block in enumerate(line.split(".")):
            list_block[k][kk] = int(block)
    mask = masked(max(list_block), min(list_block))
    return f"Result net: {sub_net(list_block, mask)}/{get_prefix(mask)}"


# Функция пересчета в двоичную систему
def hex_to_bin(tuple_temp: list):
    # Цикл для приведения блоков адресов в четырехзначный вид
    for i in range(len(tuple_temp)):
        if len(str(tuple_temp[i])) == 1:
            re_temp_item = f"000{str(tuple_temp[i])}"
            tuple_temp[i] = re_temp_item
        elif len(str(tuple_temp[i])) == 2:
            re_temp_item = f"00{str(tuple_temp[i])}"
            tuple_temp[i] = re_temp_item
        elif len(str(tuple_temp[i])) == 3:
            re_temp_item = f"0{str(tuple_temp[i])}"
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


def norm_len_temp_ipv6(norm_len_temp: list):
    while len(norm_len_temp) != 8:
        norm_len_temp = norm_len_temp + [""]
        for i in range(len(norm_len_temp) - 1, 1, -1):
            norm_len_temp[i] = norm_len_temp[i - 1]
    for i in range(len(norm_len_temp)):
        if norm_len_temp[i] == "":
            norm_len_temp[i] = 0
    return norm_len_temp


def test_list_ipv6(listed: list):
    # Проверяем, что файл не пустой
    if len(listed) == 0:
        raise ValueError("Файл пустой")
    # Запускаем цикл построчной проверки файла с получением номера строки
    for ind, line in enumerate(listed):
        # Делим каждую строку с IP адресом на блоки
        temp = line.split(":")
        # Проверяем, что все IP состоят из верного количества блоков
        if 2 <= len(temp) <= 8:
            # Дополним количество блоков, если оно было сокращено через ::
            temp = norm_len_temp_ipv6(temp)
            # Проверяем, что все блоки IP адресов из верных знаков
            spec_char = ".,:;!_*-+()/#¤%&)"
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
                    raise ValueError(f"Не все блоки IP адресов попадают в границы. На строке: {ind + 1}. IP: {line}")
            else:
                raise ValueError(f"Не все адреса состоят из верных знаков. На строке: {ind + 1}. IP: {line}")
        else:
            raise ValueError(f"Неправильное количество блоков в IP адресе. На строке: {ind + 1}. IP: {line}")


def final_address_ipv6(final_list_ipv6: list):
    # Объявим список по размеру на весь следующий цикл
    adr: list = [None] * len(final_list_ipv6)
    # Обьявим переменную для последующего рассчета префикса
    adr_bit: int = 48
    temp: list
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
    adr: str = ""
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
    return f'Result net: {adr_subnet[0]}::/{adr_bit}'


def file_processing(name_file: str, version: str):
    try:
        if version == "4":
            with open(name_file) as IPv4:
                myListIPv4 = [line.rstrip() for line in IPv4]
            if test_list_ipv4(myListIPv4):
                print(final_address_ipv4(myListIPv4))
                return final_address_ipv4(myListIPv4)
        elif version == "6":
            with open(name_file) as IPv6:
                myListIPv6 = [line.rstrip() for line in IPv6]
            if test_list_ipv6(myListIPv6) == None:
                print(final_address_ipv6(myListIPv6))
    except OSError:
        print(f"Файл {name_file} не найден")
    except ValueError:
        return test_list_ipv4(myListIPv4)


if __name__ == "__main__":
    file_processing(sys.argv[1], sys.argv[2])
