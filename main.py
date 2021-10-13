def citire():
    '''
    functia citeste lista data
    :return:lista data
    '''
    n=int(input("n="))
    list=[]
    for i in range (n):
        list.append(float(input()))
    return list


def toate_numerele_sunt_ordonate_crescator(list):
    '''
    functia verfica daca lista este ordonata crescator
    :param lst:lista de numere intregi
    :return:true daca lista este ordonata crescator si fals in caz contrar
    '''
    for i in range(len(list) - 1):
        if list[i] >= list[i + 1]:
            return False
    return True


def get_longest_sorted_asc(list):
    '''
    functia determina cea mai lunga subsecventa de numere ordonate crescator din lista
    :param list:lista de numere intregi
    :return:cea mai lunga subsecventa care are numerele ordonate crescator
    '''
    subsecventa_max = []
    for i in range(len(list)-1):
        for j in range(i, len(list)):
            if toate_numerele_sunt_ordonate_crescator(list[i:j+1]) and len(list[i:j+1]) > len(subsecventa_max):
                subsecventa_max = list[i:j+1]
    return subsecventa_max


def test_get_longest_sorted_asc():
    '''
    testeaza daca functia este corecta
    :return:cea mai lunga subsecventa de numrere ordonate crescator
    '''
    assert get_longest_sorted_asc([2,5,6,7,4,5]) == [2,5,6,7]
    assert get_longest_sorted_asc([2,4,67,89]) == [2,4,67,89]
    assert get_longest_sorted_asc([]) == []
    assert get_longest_sorted_asc([2.1,7.4,4.5,5.3]) == [2.1,7.4]
    assert get_longest_sorted_asc([5,8,9]) == [5,8,9]


def toate_numerele_au_partea_intreaga_egala_cu_partea_fractionara(list):
    '''
    functia verifica daca toate numerele din lista au partea intreaga egala cu partea fractionara
    :param list:lista de numere reale
    :return:true daca numerele din lista au partea intreaga egala cu partea fractionara si fals in caz contrar
    '''
    for i in range(len(list)):
        x = str(list[i])
        pf = x.split(".")[1]
        pi = x.split(".")[0]
        if pf != pi:
            return False
    return True


def get_longest_equal_int_real(list):
    '''
    functia determina cea mai lunga subsecventa a carei numere au partea intreaga egala cu partea fractionara
    :param list:lista de numere reale
    :return:cea mai lunga subsecventa a carei numere au partea intreaga egala cu partea fractionara
    '''
    subsecventa_max = []
    for i in range(len(list)-1):
        for j in range(i, len(list)):
            if toate_numerele_au_partea_intreaga_egala_cu_partea_fractionara(list[i:j+1]) and len(list[i:j+1]) > len(subsecventa_max):
                subsecventa_max = list[i:j+1]
    return subsecventa_max


def test_get_longest_equal_int_real():
    '''
    testeaza daca functia este corecta
    :return:cea mai lunga subsecventa a carei numere au partea intreaga egala cu partea fractionara
    '''
    assert get_longest_equal_int_real([2, 3, 4]) == []
    assert get_longest_equal_int_real([3.3, 4.4, 51.51, 66.66]) == [3.3, 4.4, 51.51, 66.66]
    assert get_longest_equal_int_real([4.4, 5.5, 4.1, 41.55]) == [4.4, 5.5]
    assert get_longest_equal_int_real([3.1, 5.5, 4.1, 4.4]) == [5.5, 4.4]
    assert get_longest_equal_int_real([41.44, 31.31, 111.111]) == [31.31, 111.111]


def menu():
    print("Alegeti optiunea:")
    print("1.Citire")
    print("2.Cea mai lunga subsecventa de numere ordonate crescator")
    print("3.Cea mai lunga subsecventa a carei numerele au partea intreaga egala cu partea fractionara")
    print("0.Iesire")


def main():
    list = []
    menu()
    option = int(input("Option="))
    while option != 0:
        if option == 1:
            list=citire()
        elif option == 2:
            print(get_longest_sorted_asc(list))
        elif option == 3:
            print(get_longest_equal_int_real(list))
        elif option == 0:
            break
        menu()
        option = int(input("Option="))



if __name__ == '__main__':
    main()

main()