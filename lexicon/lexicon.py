lexicon_ru: dict[str, str] = {
    '/start': '<b>Привет!</b>, я попробую подсказывать тебе '
              'информацию и тх по автомобилям на тесте',
    '/help': 'Создан для удобства работы на проектах.'
             'Ниже представлены основные ТТХ автомобилей'
             '/start для выбора бренда',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'Chery': 'Выбери модель из клавиатуры',
    'Haval': 'Выбери модель из клавиатуры',


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
    'Haval': {

    }
}
