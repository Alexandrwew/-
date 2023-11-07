print('вас приетствует бот по сборке ПК')
print('сейчс не лучшее время для сборки ПК из-зи больших цен в РФ, вы уверены ,что хотите начать сборку(да / нет) ')
a = True
summ = 0
videocart = ''
processor = ''
plata = ''
c = ''
v = ''
potok = ''
kol = ''
ssd = ''
gb = ''
while a:
    c = input()
    if c == 'да' or c == 'нет':
        a = False
    else:
        print(f'некоррестный ввод {c}')
a = True
if c == 'да':
    print('занете ли вы какие комплекущие будут в вашем ПК? (да / нет) ')
    while a:
        v = input()
        if v == 'да' or v == 'нет':
            a = False
        else:
            print(f'некоррестный ввод  {v}')
    a = True
    if v == 'да':
        print('''введите видеокарту которую хотите видеть ПК наш сервис только развивается, поэтрму вы можете выбрать только из 9 самых популярных видеокарт:
    ( GeForce GTX 1060 / GeForce GTX 1650 / GeForce GTX 1050 Ti / GeForce RTX 2060 / GeForce GTX 1050 / GeForce GTX 1660 Ti / GeForce GTX 1660 SUPER / GeForce GTX 1070 / GeForce RTX 3060) ''')
        while a:
            videocart = input()
            if videocart == 'GeForce GTX 1060' or videocart == 'GeForce GTX 1650' or videocart == 'GeForce GTX 1050 Ti' or videocart == 'GeForce RTX 2060' or videocart == 'GeForce GTX 1050' or videocart == 'GeForce GTX 1660 Ti' or videocart == 'GeForce GTX 1660 SUPER' or videocart == 'GeForce GTX 1070' or videocart == 'GeForce RTX 3060':
                a = False
            else:
                print(f'некорресиный ввод {videocart}')
        if videocart == 'GeForce GTX 1060':
            print('её стоимость составляет 20 000 руб')
            summ += 20000
        elif videocart == 'GeForce GTX 1650':
            print('её стоиимость составляет 25 000 рублей.')
            summ += 25000
        elif videocart == 'GeForce GTX 1050 Ti':
            print('её стоимсоть составляет 15 000 рублей')
            summ += 15000
        elif videocart == 'GeForce RTX 2060':
            print('её стоимость составляет 30 000 рублей')
            summ += 30000
        elif videocart == 'GeForce GTX 1050':
            print('её стоимость составляет 15 000 рублей')
            summ += 15000
        elif videocart == 'GeForce GTX 1660 Ti':
            print('её стоимость составляет 23 000 рублей')
            summ += 23000
        elif videocart == 'GeForce GTX 1660 SUPER':
            print('её стоиммость составляет 28 000 рублей')
            summ += 28000
        elif videocart == 'GeForce GTX 1070':
            print('её стоимость составялет 27 000 рублей')
            summ += 27000
        elif videocart == 'GeForce RTX 3060':
            print('её стоимость составляет 32000 рублей')
            summ += 32000
        a = True
        print('какой будет процессор?(AMD Ryzen 5 5600X OEM / Intel Core i5-12400F OEM / Intel Core i7-12700KF OEM / Intel Core i3-10100 OEM / Intel Core i9-12900K OEM) ')
        while a:
            processor = input()
            if processor == 'AMD Ryzen 5 5600X OEM' or processor == 'Intel Core i5-12400F OEM' or processor == 'Intel Core i7-12700KF OEM' or processor == 'Intel Core i3-10100 OEM' or processor == 'Intel Core i9-12900K OEM':
                a = False
            else:
                print(f'некорректный ввод {processor}')
        a = True
        if processor == 'AMD Ryzen 5 5600X OEM':
            print('его стоимость составляет 17 000 рублей')
            summ += 17000
        elif processor == 'Intel Core i5-12400F OEM':
            print('его стоимость составляет 13 799 рублей')
            summ += 13799
        elif processor == 'Intel Core i7-12700KF OEM':
            print('его стоимость составляет 33 999 рублей')
            summ += 33999
        elif processor == 'Intel Core i3-10100 OEM':
            print('его стоимость составит 8 000 рублей')
            summ += 8000
        elif processor == 'Intel Core i9-12900K OEM':
            print('его стоимость составит 43 999 рублей')
            summ += 43999
        print('какая будет материнская плата? у нас есть три самых популярных(ASUS ROG MAXIMUS XIII HERO / ASRock H310CM-DVS / GIGABYTE Z690 AORUS XTREME) ')
        while a:
            plata = input()
            if plata == 'ASUS ROG MAXIMUS XIII HERO' or plata == 'ASRock H310CM-DVS' or plata == 'GIGABYTE Z690 AORUS XTREME':
                a = False
            else:
                print(f'некорректный ввод {plata}')
        if plata == 'ASUS ROG MAXIMUS XIII HERO':
            print('её стоимость составит 12 999 рублей')
            summ += 12999
        elif plata == 'ASRock H310CM-DVS':
            print('её стоимость составит 2 999 рублей')
            summ += 2999
        elif plata == 'GIGABYTE Z690 AORUS XTREME':
            print('её стоисоть составит 70 000 рублей')
            summ += 70000
        a = True
        print('в нашем магазине есть только один тип пямяти ddr4 сколько гб вам надо? (2 плашки по 8) / (1 плашка по 8) / (1 плашка по 16) / (2 плашки по 16)')
        while a:
            potok = input('введите кол-во плашек опретивной памяти ')
            if potok == '1' or potok == '2':
                a = False
                potok = int(potok)
            else:
                print(f'некорректный ввод {potok}')
        a = True
        while a:
            kol = input('введите количество оперативной памяти в каждой плашке ')
            if kol == '8' or kol == '16':
                a = False
                kol = int(kol)
            else:
                print(f'некорректный ввод {kol}')
        a = True
        if potok == 1 and kol == 8:
            print(f'стоимость 1000 рублей')
            summ += 2000
        elif potok == 2 and kol == 8:
            print(f'стоимость 4000 рублей')
            summ += 4000
        elif potok == 1 and kol == 16:
            print(f'стоимость 3000 рублей')
            summ += 3000
        elif potok == 2 and kol == 16:
            print(f'стоимость 6000 рублей')
            summ += 6000
        a = True
        print('введите кол-во ssd гб (240 / 500 / 1000 / 1920)')
        while a:
            ssd = input()
            if ssd == '240' or ssd == '500' or ssd == '1000' or ssd == '1920':
                a = False
            else:
                print(f'некорректный ввод {ssd}')
        if ssd == '240':
            print(f'стоимость 1000')
            summ += 1000
        elif ssd == '500':
            print(f'стоимость 1500')
            summ += 1500
        elif ssd == '1000':
            print(f'стоимость 2500')
            summ += 2500
        elif ssd == '1920':
            print(f'стоимость 3500')
            summ += 3500
        a = True
        print('введите кол-во обычной паямти hdd (медленной)(1тб / 2тб / 3тб / 4тб)')
        while a:
            gb = input()
            if '1' in gb or '2' in gb or '3' in gb or '4' in gb:
                a = False
            else:
                print(f'некорректный ввод {gb}')
        if '1' in gb:
            print(f'стоимость 4199')
            summ += 4199
        elif '2' in gb:
            print(f'стоимость 5699')
            summ += 5699
        elif '3' in gb:
            print(f'стоимость 8290')
            summ += 8290
        elif '4' in gb:
            print(f'стоимость 10000')
            summ += 10000
        print(f'видеокарта - {videocart}; материнская плата - {plata}; процессор - {processor}; плашек - {potok}; количество в каждой плашке - {kol}гб; ssd - {ssd}гб; hdd - {gb}тб;')
        print(f'ваша цена: {summ} рублей ')
        a = True
    elif v == 'нет':
            print('для каких задач вы хотите ПК?(для несложных(например для работы с текстовыми документами) / для средних(например для нетяжёлых игр или для начальных приложениях для монтажа) / для тяжёлых ( например для работы со сложными программами ро монтажу / для очень тяжёлых игр) ')
            print('в ответе укажите для каких задач(несложных / средних / тяжёлых )? ')
            while a:
                c = input('ваш ответ: ')
                if c == 'тяжёлых' or c == 'средних' or c == 'несложных':
                    a = False
                else:
                    print(f'некоррестный ввод {c}')
            if c == 'тяжёлых':
                plata = 'GIGABYTE Z690 AORUS XTREME'
                processor = 'Intel Core i9-12900K OEM'
                videocart = 'GeForce RTX 3060'
                potok = 2
                kol = 16
                ssd = 1920
                gb = 4
                print(f'видеокарта - {videocart}; материнская плата - {plata}; процессор - {processor}; плашек - {potok}; количество в каждой плашке - {kol}гб; ssd - {ssd}гб; hdd - {gb}тб')
                print('ваша цена: 169499 рублей ')
            elif c == 'средних':
                plata = 'ASUS ROG MAXIMUS XIII HERO'
                processor = 'Intel Core i5-12400F OEM'
                videocart = 'GeForce GTX 1660 SUPER'
                potok = 2
                kol = 8
                ssd = 1000
                gb = 2
                print(f'видеокарта - {videocart}; материнская плата - {plata}; процессор - {processor}; плашек - {potok}; количество в каждой плашке - {kol}гб; ssd - {ssd}гб; hdd - {gb}тб')
                print('ваша цена: 68997 рублей ')
            elif c == 'несложных':
                plata = 'ASRock H310CM-DVS'
                processor = 'Intel Core i3-10100 OEM'
                videocart = 'GeForce GTX 1050'
                potok = 1
                kol = 8
                ssd = 240
                gb = 1
                print(f'видеокарта - {videocart}; материнская плата - {plata}; процессор - {processor}; плашек - {potok}; количество в каждой плшке - {kol}гб; ssd - {ssd}гб; hdd - {gb}тб')
                print('ваша цена: 33198 рублей')
else:
    print('как собирететесь с мыслями заходите')
