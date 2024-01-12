lexicon_ru: dict[str, str] = {
    '/start': '<b>Привет!</b>, я попробую подсказывать тебе '
              'информацию и тх по автомобилям на тесте',
    '/help': 'Создан для удобства работы на проектах.'
             'Ниже представлены основные ТТХ автомобилей'
             '/start для выбора бренда',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'choice': 'Выбери модель из клавиатуры',


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
    'Getour': {
        'X90 PLUS': get_specification('1.6T - 2.0T', '190 - 245', '275 - 375', '11.0 - 8.5', 'DCT7',
                                      '4858 x 1925 x 1780', '1709 -1790', '57', '210',
                                      'передний привод', 'независимая McPherson, независимая многорычажная',
                                      'Comfort, Elite, Luxury',
                                      '3 399 900 - 3 889 900', 'https://jetour-ru.com/models/x90Plus'),
        'X70 PLUS': get_specification('1.6T', '190', '275', '11.7', 'DCT7',
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
        'S5 GT': get_specification('1.6T', '150', '275', '7.5', 'DCT7',
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
        'H9': get_specification('2.0T Dis/Pet', 'Dis 190/Pet 218', '420/380', '<14.0 - 11.0', 'АКПП8 ZF',
                                '4856 x 1926 x 1900', '2450 - 2480', '80', '206',
                                'полный привод', 'независимая двурычажная, зависимая пятирычажная',
                                'Elite Pet&Dis, Premium',
                                '4 099 000 - 4 299 000', 'https://haval.ru/models/haval-h9-new/'),
        'Dargo X': get_specification('2.0T', '192', '320', '<10.0', 'DCT7',
                                     '4620 x 1890 x 1780', '1700 - 1815', '60', '200',
                                     'подключаемый полный 4WD', 'независимая McPherson, независимая двурычажная',
                                     'Elite, Premium',
                                     '3 269 000 - 3 469 000', 'https://haval.ru/models/new-haval-dargo/#dargox'),
        'Dargo': get_specification('2.0T', '192', '320', '<10.0', 'DCT7',
                                   '4620 x 1890 x 1780', '1700 - 1815', '60', '200',
                                   'передний - подключаемый полный 4WD', 'независимая McPherson, независимая двурычажная',
                                   'Comfort, Elite, Premium',
                                   '3 269 000 - 3 469 000', 'https://haval.ru/models/new-haval-dargo/#dargo'),
        'M6': get_specification('1,5T', '143', '202', '12.9 - 12.7', 'MT6 - DCT7',
                                '4664 x 1830 x 1729', '1535 - 1565', '55', '170',
                                'передний привод', 'независимая McPherson, независимая двурычажная',
                                '1.5 MT (143 л.с.), 1.5 DCT (143 л.с.)',
                                '2 179 000 - 2 299 000', 'https://haval.ru/models/new-haval-m6/'),
        'Jolion': get_specification('1.5T', '143 - 150', '210 -230', '9,8', 'MT6 - DCT7',
                                    '4472 x 1841 x 1574', '1420 - 1625', '55', '190',
                                    'передний - подключаемый полный', 'независимая McPherson, полузависимая / независимая многорычажная',
                                    'Comfort, Elite, Elite plus, Premium',
                                    '1 949 000 - 2 599 000', 'https://haval.ru/models/new-haval-jolion/'),
    },
    'Changan': {
        'Uni-T': get_specification('1.5T', '167', '280', '', 'DCT7',
                                   '4515 x 1870 x 1565', '1465', '55', '87??',
                                   'передний привод', 'независимая McPherson, независимая многорычажная',
                                   'Luxe, Tech',
                                   '2 869 900 - 2 969 900', 'https://changanauto.ru/models/uni-t/'),
        'CS55 Plus': get_specification('1.5T', '181', '280', '', 'DCT7',
                                       '4515 x 1865 x 1680', '1520 - 1535', '55', '171',
                                       'передний привод', 'независимая McPherson, независимая многорычажная',
                                       'Comfort, Luxe, Tech',
                                       '2 629 900 - 2 749 900', 'https://changanauto.ru/models/cs55plus/'),

    }
}
"""
get_specification('', '', '', '', '',
                                      '', '', '', '',
                                      '', '',
                                      '',
                                      '', ''),

"""
