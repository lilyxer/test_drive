lexicon_ru: dict[str, str] = {
    '/start': 'я попробую подсказывать тебе '
              'информацию и тх по автомобилям на тесте\n'
              'пожалуйста пользуйся встроенной клавиатурой\n\n'
              'Версия бота 1.0 ... цены актуальны на январь \'24года\n'
              'о неточностях или ошибках просьба сообщить мне: @MikhBorisov',
    '/help': 'Создан для удобства работы на проектах.'
             'Ниже представлены основные ТТХ автомобилей'
             '/start для выбора бренда',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'choice': 'Выбери модель из клавиатуры',
    'menu': 'Вы в главном меню, выберите машины или маршрут',
    'map': 'Мы в <b> Казани </b>\n'
           'Ссылка на маршрут: внизу сообщения\n'
           '\nТочки на карте:\n'
           '0. Точка старта - Аэропорт -- 0 смена\n\n'
           '6 км ~10мин\n'
           '1. Халяль, напротив озон\n\n'
           '7 км ~8мин\n'
           '2. Сокуры, напротив мусорки к гаражам\n\n'
           '10 км ~10мин\n'
           '3. Парковка у Пятёрочки -- 1 смена\n\n'
           '7 км ~8мин\n'
           '4. Широкая обочина перед знаком\n\n'
           '4 км ~6мин\n'
           '5. Магазин хозтоваров, пяточок в 2 ряда\n\n'
           '3 км ~7мин\n'
           '6. Широкая обочина на проходной -- 2 смена\n\n'
           '3 км ~8мин\n'
           '7. Большая парковка на перекрестке\n\n'
           '2.1 км ~6мин\n'
           '8. Парковка за АЗС\n\n'
           '6 км ~8мин\n'
           '9. Парковка у школы -- 3 смена\n\n'
           '9 км ~10мин\n'
           '10. Въезд в лес !!Быстрая!!\n\n'
           '1.43 км ~4мин\n'
           '11. Смена в лесу !!Быстрая!!\n\n'
           '3.6 км ~6мин\n'
           '12. Большая автобусная остановка -- 4 смена\n\n'
           '8.2 км ~9мин\n'
           '13. Съезд на дублёр к озону\n\n'
           '3.4 км ~5мин\n'
           '14. Мечеть, не отбита\n\n'
           '5.9 км ~12мин\n'
           '15. Газовая заправка -- 5 смена\n\n'
           '6.2 км ~10мин\n'
           '16. Карманы после разворота под эстакадой\n\n'
           '8.5 км ~9мин\n'
           '17. Пятёрочка\n\n'
           '6 км ~9мин\n'
           '18. Финиш в гостиннице\n'
           'https://yandex.ru/maps/43/kazan/?ll=49.282360%2C55.651853&mode=routes&rtext=55.609541%2C49.302704~55.648695%2C49.301569~55.622243%2C49.393059~55.649643%2C49.288235~55.633027%2C49.259355~55.643818%2C49.213857~55.658804%2C49.216998~55.654489%2C49.195577~55.635717%2C49.214125~55.633270%2C49.215350~55.622736%2C49.229028~55.622578%2C49.151982~55.639773%2C49.030118~55.647427%2C49.024740~55.636302%2C49.063806~55.676623%2C49.125767~55.701176%2C49.143441~55.705735%2C49.183359~55.684887%2C49.206109~55.654726%2C49.283771&rtt=auto&ruri=~~~~~~~~~~~~~~~~~~~&z=15.37',
}

interest: dict[str, list[str]] = {
    'chery_int': ['В дополнении к обычной гарантии в 3 года '
                  'добавляется диллерская гарантия еще на несколько лет и 100км',
                  'chery в переводе как не старанно - вишня'],

}
def get_specification(engine: str = '', power: str = '', torque: str = '', acceleration: str = '',
                      transmission: str = '', size: str = '', mass: str = '', fuel: str = '',
                      clearance: str = '', drive: str = '', susp: str = '', equip: str = '',
                      price = '', page: str='') -> str:
    return (f'<b>Двигатель:</b>\n{engine}\n<b>Мощность:</b>\n{power} л.с.\n'
            f'<b>Момент:</b>\n{torque} Нм\n<b>Разгон:</b>\n{acceleration} сек\n\n'
            f'<b>Трансмиссия:</b>\n{transmission}\n\n'
            f'<b>Габариты:</b>\n{size}\n<b>Масса:</b>\n{mass}кг\n<b>Объём бака:</b>\n{fuel} л\n'
            f'<b>Дорожный просвет:</b>\n{clearance} мм\n\n'
            f'<b>Привод:</b>\n{drive}\n<b>Подвеска:</b>\n{susp}\n\n'
            f'<b>Комплектации:</b>\n{equip}\n'
            f'<b>Цена</b>\n{price} руб\n\n'
            f'<b>Ссылка:</b>\n{page}')

cars = {
    'Chery': {
        'new_tiggo_8_pro_max': get_specification('2.0T', '197', '375', '8.4', 'DCT7',
                                                 '4720 х 1860 х 1705', '1829', '57', '190',
                                                 'интеллектуальный полный', 'независимая McPherson, независимая многорычажная',
                                                 'Dreamline, Ultimate',
                                                 '4 160 000 - 4 651 000', 'https://www.chery.ru/models/newtiggo8promax/'),
        'tiggo_7_pro_max': get_specification('1.5T - 1.6T', '147 - 150', '210 - 275', '9.8', 'CVT9 - DCT7',
                                             '4500 x 1842 x 1705', '1540 - 1643', '51', '190',
                                             'передний - интеллектуальный полный', 'независимая McPherson, независимая многорычажная',
                                             'Elite (FWD), Prestige, Ultimate',
                                             '2 820 000 - 3 570 000', 'https://www.chery.ru/models/tiggo7promax/'),
        'tigo_4_pro': get_specification('1.5 - 1.5T', '113 - 147', '138 - 210', '13.9 - 9.7', 'MT5, CVT7, CVT9',
                                        '4318 x 1831 x 1662', '1350 - 1439', '51', '190',
                                        'передний привод', 'независимая McPherson, полузависимая со стабилизатором поперечной устойчивости',
                                        'Action, Family, Travel, Style, Ultimate',
                                        '2 120 000 - 2 620 000', 'https://www.chery.ru/models/tiggo4pro/'),
        'arrizo_8': get_specification('1.6T', '186', '275', '8.9', 'DCT7',
                                      '4757 x 1832 x 1469', '1489 - 1538', '55', '144',
                                      'передний привод', 'независимая McPherson, независимая многорычажная',
                                      'Prestige, Ultimate, Ultimate SE',
                                      '3 410 000 - 3 560 000', 'https://www.chery.ru/models/arrizo8/')
    },
    'Jetour': {
        'X90_PLUS': get_specification('1.6T - 2.0T', '190 - 245', '275 - 375', '11.0 - 8.5', 'DCT7',
                                      '4858 x 1925 x 1780', '1709 -1790', '57', '210',
                                      'передний привод', 'независимая McPherson, независимая многорычажная',
                                      'Comfort, Elite, Luxury',
                                      '3 399 900 - 3 889 900', 'https://jetour-ru.com/models/x90Plus'),
        'X70_PLUS': get_specification('1.6T', '190', '275', '11.7', 'DCT7',
                                      '4724 x 1900 x 1720', '1662 - 1694', '57', '204',
                                      'передний привод', 'независимая McPherson, независимая многорычажная',
                                      'Comfort, Luxury',
                                      '2 999 900 - 3 299 900', 'https://jetour-ru.com/models/x70Plus'),
        'DASHING': get_specification('1.5T - 1.6T', '147 - 190', '210 - 271', '13.2 - 10.5', 'MT6 - DCT6 - DCT7',
                                     '4590 x1900 x 1685', '1570 - 1655', '57', '160',
                                     'передний привод', 'независимая McPherson, независимая многорычажная',
                                     'Comfort, Comfort plus, Elite, Luxury',
                                     '2 489 900 - 3 189 900', 'https://jetour-ru.com/models/dashing'),
    },
    'Omoda': {
        'C5': get_specification('1.5T - 1.6T', '147 - 150', '210 - 275', '9.9 - 8.6', 'CVT25 - DCT7',
                                '4400 x 1830 x 1588', '1456 - 1610', '52 - 57', '190 - 180',
                                'передний - интеллектуальный полный', 'независимая McPherson, полузависимая / независимая многорычажная',
                                'Joy, Lifestyle, Ultimate, Active, Supreme',
                                '2 679 900 - 3 309 900', 'https://omoda.ru/models/modelc5/'),
        'S5_GT': get_specification('1.6T', '150', '275', '7.5', 'DCT7',
                                   '4691 x 1814 x 1493', '1419', '48', '160',
                                   'передний привод', 'независимая McPherson, полузависимая',
                                   'Neo, Ultra',
                                   '2 759 900 - 2 419 900', 'https://omoda.ru/models/s5gt/'),
        'S5': get_specification('1.5 - 1.5T', '113 - 147', '138 - 210', '13.2 - 9.7', 'CVT18 - CVT25',
                                '4644 x 1814 x 1493', '1386 - 1395', '48', '160',
                                'передний привод', 'независимая McPherson, полузависимая',
                                'Life, Tech, Ultra',
                                '2 249 900 - 2 549 900', 'https://omoda.ru/models/models5/'),
    },
    'Jaecoo': {
        'J7': get_specification('1.6T', '186', '275', '9,4 - 8,9', 'DCT7',
                                '4500 x 1865 x 1680', '1619 - 1709', '51-57', '196 - 186',
                                'передний - интеллектуальный полный', 'независимая McPherson, независимая многорычажная',
                                'Lifestyle, Ultimate, Active, Supreme',
                                '3 339 900 - 3 749 900', 'https://jaecoo.ru/models/modelj7/'),
    },
    'Haval': {
        'H9': get_specification('2.0T Dis/Pet', 'Dis 190/Pet 218', '420/380', '14.0 - 11.0', 'АКПП8 ZF',
                                '4856 x 1926 x 1900', '2450 - 2480', '80', '206',
                                'полный привод', 'независимая двурычажная, зависимая пятирычажная',
                                'Elite Pet&Dis, Premium',
                                '4 099 000 - 4 299 000', 'https://haval.ru/models/haval-h9-new/'),
        'DargoX': get_specification('2.0T', '192', '320', '10.0', 'DCT7',
                                     '4620 x 1890 x 1780', '1700 - 1815', '60', '200',
                                     'подключаемый полный 4WD', 'независимая McPherson, независимая двурычажная',
                                     'Elite, Premium',
                                     '3 269 000 - 3 469 000', 'https://haval.ru/models/new-haval-dargo/#dargox'),
        'Dargo': get_specification('2.0T', '192', '320', '10.0', 'DCT7',
                                   '4620 x 1890 x 1780', '1700 - 1815', '60', '200',
                                   'передний - подключаемый полный 4WD', 'независимая McPherson, независимая двурычажная',
                                   'Comfort, Elite, Premium',
                                   '2 999 000 - 3 549 000', 'https://haval.ru/models/new-haval-dargo/#dargo'),
        'M6': get_specification('1,5T', '143', '202', '12.9 - 12.7', 'MT6 - DCT7',
                                '4664 x 1830 x 1729', '1535 - 1565', '55', '170',
                                'передний привод', 'независимая McPherson, независимая двурычажная',
                                '1.5 MT (143 л.с.), 1.5 DCT (143 л.с.)',
                                '2 179 000 - 2 299 000', 'https://haval.ru/models/new-haval-m6/'),
        'F7': get_specification('1.5T - 2.0T', '150 - 190', '280 - 340', '11 - 9', 'DCT7',
                                '4691 x 1866 x 1690', '1680 - 1795', '56', '190',
                                'передний - подключаемый полный', 'независимая McPherson, независимая двухрычажная',
                                'Comfort, Elite, Elite plus, Premium',
                                '2 399 000 - 3 299 000', 'https://haval.ru/models/new-haval-f7/'),
        'Jolion': get_specification('1.5T', '143 - 150', '210 -230', '9,8', 'MT6 - DCT7',
                                    '4472 x 1841 x 1574', '1420 - 1625', '55', '190',
                                    'передний - подключаемый полный', 'независимая McPherson, полузависимая / независимая многорычажная',
                                    'Comfort, Elite, Premium, Tech Plus',
                                    '1 949 000 - 2 599 000', 'https://haval.ru/models/new-haval-jolion/'),
    },
    'Changan': {
        'CS95': get_specification('2.0T', '226', '380', '??', 'AT8 Aisin',
                                   '4949 x 1940 x 1805', '2117', '74', '190',
                                   'интеллектуальный полный', 'независимая McPherson, независимая многорычажная',
                                   'DLX, Black edition',
                                   '4 199 900 - 4 269 900', 'https://changanauto.ru/models/cs95new/'),
        'Uni-K': get_specification('2.0T', '226', '380', '??', 'AT8 Aisin',
                                   '4865 x 1948 x 1695', '1920 - 2005', '70', '190',
                                   'передний - интеллектуальный полный', 'независимая McPherson, независимая многорычажная',
                                   'Comfort, Luxe, Tech',
                                   '3 639 900 - 4 239 900', 'https://changanauto.ru/models/uni-k/'),
        'Uni-T': get_specification('1.5T', '167', '280', '??', 'DCT7',
                                   '4515 x 1870 x 1565', '1465', '55', '??',
                                   'передний привод', 'независимая McPherson, независимая многорычажная',
                                   'Luxe, Tech',
                                   '2 869 900 - 2 969 900', 'https://changanauto.ru/models/uni-t/'),
        'CS75_Plus': get_specification('1.5T', '167', '265', '??', 'AT6 Aisin',
                                       '4700 x 1865 x 1710', '1610', '58', '190',
                                       'передний привод', 'независимая, типа McPherson, независимая многорычажная',
                                       'Luxury',
                                       '2 849 900', 'https://changanauto.ru/models/cs75plus/'),
        'CS55_Plus': get_specification('1.5T', '181', '280', '??', 'DCT7',
                                       '4515 x 1865 x 1680', '1520 - 1535', '55', '171',
                                       'передний привод', 'независимая McPherson, независимая многорычажная',
                                       'Comfort, Luxe, Tech',
                                       '2 629 900 - 2 749 900', 'https://changanauto.ru/models/cs55plus/'),
        'CS55': get_specification('1.5T', '143', '210', '', 'MT6 - AT6',
                                  '4500 x 1855 x 1690', '1535 - 1565', '58', '190',
                                  'передний привод', 'независимая McPherson, независимая многорычажная',
                                  'Comfort, Luxe',
                                  '2 189 900 - 2 389 900', 'https://changanauto.ru/models/cs55/'),
        'CS35_Plus': get_specification('1.4T', '150', '255', '', 'DCT7',
                                  '4330 x 1825 x 1660', '1465', '52', '??',
                                  'передний привод', 'независимая McPherson, полузависимая',
                                  'Advance, Tech',
                                  '2 339 900 - 2 399 900', 'https://changanauto.ru/models/cs35plusnew/'),
        'Uni-V': get_specification('1.5T', '181', '300', '??', 'DCT7',
                                   '4680 x 1838 x 1430', '1400', '51', '152',
                                   'передний привод', 'независимая McPherson, независимая многорычажная',
                                   'LX, DLX',
                                   '2 859 900 - 2 929 900', 'https://changanauto.ru/models/uni-v/'),
    },
    'Geely': {
        'Monjaro': get_specification('2.0T', '238', '350', '7.7', 'AT8',
                                     '4770 x 1895 x 1689', '1855', '62', '210',
                                     'полный привод', 'независимая McPherson, независимая многорычажная',
                                     'Luxury, Flagship, Exclusive',
                                     '4 694 990 - 4 994 990', 'https://www.geely-motors.com/model/monjaro'),
        'Tugella': get_specification('2.0T', '200 - 238', '350', '7.4 - 6.9', 'AT8',
                                     '4605 х 1878 х 1643', '1815', '54', '204',
                                     'полный привод', 'независимая McPherson, независимая многорычажная',
                                     'Luxury, Flagship, Flagship Sport',
                                     '3 959 990 - 4 389 990', 'https://www.geely-motors.com/model/newtugella'),
        'Atlas_pro': get_specification('1.5T', '150 - 177', '255', '11 - 9.9', 'AT6 - DCT7',
                                       '4544 х 1831 х 1713', '1685 - 1780', '58', '171',
                                       'передний - полный(MHEV)привод', 'независимая McPherson, независимая многорычажная',
                                       'Comfort, Luxury, Flagship, Flagship+',
                                       '2 763 990 - 3 393 990', 'https://www.geely-motors.com/model/atlaspro'),
        'Coolray': get_specification('1.5T', '147', '270', '8.1', 'DCT7',
                                     '4380 х 1810 х 1615', '1432', '45', '180',
                                     'передний привод', 'независимая McPherson, полузависимая',
                                     'Comfort, Luxury, Flagship, Exclusive',
                                     '2 609 990 - 2 949 990', 'https://www.geely-motors.com/model/geely-coolray-2023'),
        'Emgrand': get_specification('1.5', '122', '152', '12.9 - 12.6', 'MT5 - AT6',
                                     '4638 x 1822 x 1460', '1270 - 1340', '', '151',
                                     'передний привод', 'независимая McPherson, полузависимая',
                                     'Standart, Comfort, Luxury, Flagship',
                                     '2 009 990 - 2 489 990', 'https://www.geely-motors.com/model/emgrand'),
    },
    'Москвич': {
        '3_jaq_gs4': get_specification('1.5T', '136', '200', '', 'MT6 - CVT',
                                       '4410 х 1800 х 1660', '1440', '50', '170',
                                       'передний привод', 'независимая McPherson, полузависимая',
                                       'Стандарт, Стандарт плюс, Комфорт',
                                       '2 220 000 - 2 478 000', 'https://moskvich-auto.ru/models/moskvich-3'),
        '6_jaq_j7': get_specification('1.5T', '136 - 174', '', '10.4 - 7.8', 'T - DCT6',
                                      '4770 х 1820 х 1492', '1460 - 1560', '55', '140',
                                      'передний привод', 'независимая McPherson, независимая многорычажная',
                                      'Комфорт, Бизнес, Техно',
                                      '2 626 000 - 3 116 000', 'https://moskvich-auto.ru/models/moskvich-6'),
    },
    'Evolute': {
        'I_Jet': get_specification('', '', '', '', '',
                                   '', '', '', '',
                                    '', '',
                                    '',
                                    '', ''),

        'I_Sky': get_specification('', '', '', '', '',
                                   '', '', '', '',
                                    '', '',
                                    '',
                                    '', ''),
        'I_Joy': get_specification('', '', '', '', '',
                                   '', '', '', '',
                                    '', '',
                                    '',
                                    '', ''),
        'I_Jet': get_specification('', '', '', '', '',
                                   '', '', '', '',
                                    '', '',
                                    '',
                                    '', ''),
    }
}
"""
get_specification('', '', '', '', '',
                                      '', '', '', '',
                                      '', '',
                                      '',
                                      '', ''),

"""
