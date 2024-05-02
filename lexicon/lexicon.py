from lexicon.classes import Brand, ModelD, ModelE, ModelHE


lexicon_ru: dict[str, str] = {
    '/start': 'Привет\n! Я попробую подсказывать тебе информацию и характеристики автомобилей на тесте и не только.\nНажми - /menu и мы начнем\nЛибо - /help если нужна помощь\n\nПожалуйста пользуйся встроенной клавиатурой.\n\nВерсия бота 1.310124 цены актуальны на январь \'24года.\nО неточностях или ошибках просьба сообщить мне: @MikhBorisov\n\nРЕКОМЕНДУЮ включить автоудаление переписки, т.к. файлы хоть и не большие, но могут сжирать память\nЗаходим в чат - справа вверху иконка бота - ещё - Автоудаление',
    '/help': 'Создан для удобства работы на проектах. Ниже представлены основные характеристики автомобилей.\nДля выбора используйте встроенные кнопки:\n/start запуск бота\n/menu для выхода в главное меню',
    '/menu': 'Вы в главном меню, выберите машины или маршрут',
    'choice': 'Выбери модель из клавиатуры',
    'Меню': 'Вы в главном меню, выберите машины или маршрут',
    'Маршрут': 'Доступных маршрутов нет',
    'Автомобили': 'Выбери из доступных ниже',
    'До обеда': 'Маршрут не прописан',
    'После обеда': 'Маршрут не прописан',
    'Карта': 'Маршрут не прописан',
    'Презентации': 'У меня не так много през осталось от прошлых проектов, если у вас есть ещё какие нибудь - скидывайте мне, добавлю.\n\n Выбери нужную презентацию из списка',
    'Chery': str(Brand(name='Chery', concern='Chery Holdings', foundation=1997,
                       type_of='кроссоверы, внедорожники, седаны и микрофургоны',
                       start=2005, in_russia='«Автотор» в Калининградской области',
                       year='с 2006 по 2008', site='https://www.chery.ru/')),
    'Jetour': str(Brand(name='Jetour', concern='Chery Automobile', foundation=2018,
                        type_of='кроссоверы', start=2023, site='https://jetour-ru.com/')),
    'Jaecoo': str(Brand(name='Jaecoo', concern='Chery Automobile', foundation=2023,
                        type_of='кроссоверы', start=2023, site='https://jaecoo.ru/')),
    'Omoda': str(Brand(name='Omoda', concern='Chery Automobile', foundation=2022,
                       type_of='кроссоверы и седаны', start=2022, site='https://omoda.ru/')),
    'Exeed': str(Brand(name='Exeed', concern='Chery Automobile', foundation=2017,
                       type_of='кроссоверы и внедорожники премиум класса',
                       start=2020, site='https://exeed.ru/')),
    'Haval': str(Brand(name='Haval', concern='Great Wall Motors', foundation=2013,
                       type_of='кроссоверы и внедорожники', start=2015,
                       in_russia='«Хавейл Мотор» в Тульской области', year='с 2015',
                       site='https://haval.ru/')),
    'Tank': str(Brand(name='Tank', concern='Great Wall Motors', foundation=2020,
                      type_of='рамные внедорожники', start=2023, site='https://tank.ru/')),
    'Changan': str(Brand(name='Changan', concern='Changan Automobile Group', foundation=1993,
                       type_of='седаны и кроссоверы', start=2013,
                       in_russia='«Моторинвест» в Липецкой области', year='с 2017 по 2019',
                       site='https://changanauto.ru/')),
    'Evolute': str(Brand(name='Evolute', local='Dongfeng', foundation=2022,
                         type_of='электрические седаны и кроссоверы', start=2022,
                         in_russia='«Моторинвест» в Липецкой области', year='с 2022',
                         site='https://www.evolute.ru/')),
    'Москвич': str(Brand(name='Москвич', local='JAC', foundation=2022,
                         type_of='седаны и кроссоверы', start=2022,
                         in_russia='«Москвич» в Москве', year='с 2022',
                         site='https://moskvich-auto.ru/')),
    'Geely': str(Brand(name='Geely', concern='Geely Holding Group', foundation=1986,
                       type_of='кроссоверы и внедорожники', start=2008,
                       in_russia='БелДжи в Борисове, Белорусия', year='с 2011',
                       site='https://www.geely-motors.com/')),
    'Great Wall': str(Brand(name='Great Wall', concern='Great Wall Motors', foundation=1976,
                            type_of='кроссоверы и внедорожники', start=2004,
                            site='https://haval.ru/')),
    'Ora': str(Brand(name='Ora', concern='Great Wall Motors', foundation=2018,
                     type_of='электрические автомобили', start=2023, site='https://gwm-ora.ru/')),
    'Voyah': str(Brand(name='Voyah', concern='Dongfeng', foundation=2020,
                       type_of='гибридные и электрические автомобили', start=2023, site='https://voyah.su/')),
    'Oting': str(Brand(name='Oting', concern='Dongfeng', foundation=2024,
                       type_of='кроссоверы и внедорожники', start=2024, site='https://otingcars.ru/')),
    # 'MG': str(Brand(name='MG', concern='SAIC Motor', foundation=2005, type_of='седаны и кроссоверы',
    #                 start=2023, site='https://mgcars-russia.ru/')),
    # 'Li Auto': str(Brand(name='Li Auto / Li Xiang', foundation=2015,
    #                      type_of='электрические и гибридные кроссоверы', start=2023,
    #                      site='https://lixiang-russia.com/')),
    # 'Aito': str(Brand(name='Aito', concern='Входит в концерн Huawei',  foundation=2021,
    #                   type_of='электрические и гибридные кроссоверы', start=2023,
    #                   site='https://mbrus.ru/aito-cars/')),
}

buttons = {
    '/menu': ('Автомобили', 'Маршрут', 'Презентации'),
    'Маршрут': ('До обеда', 'После обеда', 'Карта'),
}

cars: list[ModelD] = [
    ModelD(brand='Chery', model='tiggo_8_pro_max', engine='2.0T', power='197', torque='375',
           acceleration='8.4', consumption='8.3', transmission='роботизированная DCT7',
           size='4720 х 1860 х 1705', mass='1829', fuel='57', clearance='190',
           drive='интеллектуальный полный', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Dreamline Ultimate', price='3 900 000 - 4 170 000', page='https://www.chery.ru/models/newtiggo8promax/'),
    ModelD(brand='Chery', model='8_pro', engine='1.6T', power='186', torque='275',
           acceleration='8.9', consumption='7.0', transmission='роботизированная DCT7',
           size='4722 х 1860 х 1705', mass='1640', fuel='51', clearance='190',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Dreamline Ultimate', price='3 430 000 - 3 550 000', page='https://www.chery.ru/models/tiggo8pro/'),
    ModelD(brand='Chery', model='tiggo_7_pro_max', engine='1.5T - 1.6T', power='147 - 150', torque='210 - 275',
           acceleration='9.8', consumption='8.2 - 7.7', transmission='вариатор CVT9 - роботизированная DCT7',
           size='4500 x 1842 x 1705', mass='1540 - 1643', fuel='51', clearance='190',
           drive='передний - интеллектуальный полный', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Elite(FWD) Prestige(FWD) Ultimate(FWD) Prestige(AWD) Ultimate(AWD)',
           price='2 700 000 - 3 260 000', page='https://www.chery.ru/models/tiggo7promax/'),
    ModelD(brand='Chery', model='7_pro', engine='1.5T', power='147', torque='210',
           acceleration='9.8', consumption='8.2', transmission='вариатор CVT9',
           size='4500 x 1842 x 1705', mass='1540', fuel='51', clearance='190',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Elite Prestige',
           price='2 570 000 - 2 700 000', page='https://www.chery.ru/models/tiggo7pro/'),
    ModelD(brand='Chery', model='tigo_4_pro', engine='1.5 - 1.5T', power='113 - 147', torque='138 - 210',
           acceleration='14.6 - 9.7', consumption='7.4 - 7.1', transmission='механическая MT5 - вариатор CVT7 - вариатор CVT9',
           size='4318 x 1831 x 1662', mass='1350 - 1439', fuel='51', clearance='190',
           drive='передний', susp='независимая типа McPherson\nполузависимая, пружинная, с гидравлическими телескопическими '
          'амортизаторами и стабилизатором поперечной устойчивости',
           equip='Action MT Action Family Travel Style Ultimate',
           price='2 120 000 - 2 640 000', page='https://www.chery.ru/models/tiggo4pro/'),
    ModelD(brand='Chery', model='arrizo_8', engine='1.6T', power='186', torque='275',
           acceleration='8.9', consumption='6.2', transmission='роботизированная DCT7',
           size='4757 x 1832 x 1469', mass='1489 - 1538', fuel='55', clearance='144',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Prestige Ultimate Ultimate_SE',
           price='2 950 000 - 3 100 000', page='https://www.chery.ru/models/arrizo8/'),
    ModelD(brand='Jetour', model='T2', engine='2.0T', power='245', torque='375',
           acceleration='8.7', consumption='9.3', transmission='роботизированная DCT7',
           size='4785 x 2006 x 1880', mass='1915 - 1955', fuel='70', clearance='220',
           drive='интеллектуальный полный', susp='независимая типа McPherson, с телескопическими амортизаторами,'
           ' со стабилизатором поперечной устойчивости\nнезависимая, многорычажная, пружинная, с'
           ' телескопическими амортизаторами, со стабилизатором поперечной устойчивости', equip='VOYAGE EXPEDITION',
           price='3 759 000 - 3 999 000', page='https://jetour-ru.com/models/T2/'),
    ModelD(brand='Jetour', model='X90_PLUS', engine='1.6T - 2.0T', power='190 - 245', torque='275 - 375',
           acceleration='11.0 - 8.5', consumption='8.1 - 8.0', transmission='роботизированная DCT7',
           size='4858 x 1925 x 1780', mass='1709 -1790', fuel='57', clearance='210',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort Elite Luxury',
           price='3 399 900 - 3 889 900', page='https://jetour-ru.com/models/x90Plus/'),
    ModelD(brand='Jetour', model='X70_PLUS', engine='1.6T', power='190', torque='275',
           acceleration='11.0 - 8.5', consumption='8.1 - 8.0', transmission='роботизированная DCT7',
           size='4724 x 1900 x 1720', mass='1662 - 1694', fuel='57', clearance='204',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort Luxury',
           price='2 999 900 - 3 299 900', page='https://jetour-ru.com/models/x70Plus/'),
    ModelD(brand='Jetour', model='DASHING', engine='1.5T - 1.6T', power='147 - 190', torque='210 - 275',
           acceleration='13.2 - 10.5', consumption='7,5 - 8.4', transmission='механика МТ5 - роботизированная DCT6/DCT7',
           size='4590 x1900 x 1685', mass='1570 - 1655', fuel='57', clearance='160',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort_plus Comfort Elite Luxury',
           price='2 489 900 - 3 189 900', page='https://jetour-ru.com/models/dashing/'),
    ModelD(brand='Omoda', model='C5', engine='1.5T - 1.6T', power='147 - 150', torque='210 - 275',
           acceleration='9.9 - 8.6', consumption='7,1 - 7.4', transmission='вариатор CVT9 - роботизированная DCT7',
           size='4400 x 1830 x 1588', mass='1456 - 1610', fuel='52 - 57', clearance='190 - 180',
           drive='передний - интеллектуальный полный', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами/многорычажная, пружинная, с гидравлическими телескопическими амортизаторами',
           equip='Joy Lifestyle Ultimate Active Supreme',
           price='2 679 900 - 3 309 900', page='https://omoda.ru/models/modelc5/'),
    ModelD(brand='Omoda', model='S5_GT', engine='1.6T', power='150', torque='275',
           acceleration='7.5', consumption='6.9', transmission='роботизированная DCT7',
           size='4691 x 1814 x 1493', mass='1419', fuel='48', clearance='160',
           drive='передний', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами', equip='Neo Ultra',
           price='2 759 900 - 2 859 900', page='https://omoda.ru/models/s5gt/'),
    ModelD(brand='Omoda', model='S5', engine='1.5 - 1.5T', power='113 - 1147', torque='138 - 210',
           acceleration='13.2 - 9.7', consumption='7.3 - 6.9', transmission='вариатор CVT7 - вариатор CVT9',
           size='4644 x 1814 x 1493', mass='1386 - 1395', fuel='48', clearance='160',
           drive='передний', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами', equip='Life Tech Ultra',
           price='2 249 900 - 2 549 900', page='https://omoda.ru/models/models5/'),
    ModelD(brand='Jaecoo', model='J7', engine='1.6T', power='186', torque='275',
           acceleration='9.4 - 8.9', consumption='7.6 - 8.2', transmission='роботизированная DCT7',
           size='4500 x 1865 x 1680', mass='1619 - 1709', fuel='51-57', clearance='196 - 186',
           drive='передний - интеллектуальный полный', susp='независимая McPherson, независимая многорычажная '
           'с гидравлическими телескопическими амортизаторами и стабилизатороми поперечной устойчивости',
           equip='Lifestyle Ultimate Active Supreme',
           price='3 049 900 - 3 379 900', page='https://jaecoo.ru/models/modelj7/'),
    ModelD(brand='Jaecoo', model='J8', engine='2.0T', power='249', torque='385',
           acceleration='8.6', consumption='независимая типа McPherson\nнезависимая многорычажная',
           transmission='роботизированная DCT7',
           size='4820 x 1930 x 1710', mass='1929', fuel='65', clearance='210',
           drive='интеллектуальный полный', equip='Active Supreme SupremeV', susp='независимая McPherson\nнезависимая многорычажная',
           price='ПРЕДЗАКАЗ', page='https://jaecoo.ru/models/modelj8/'),
    ModelD(brand='Haval', model='H9', engine='2.0T', power='218', torque='380',
           acceleration='11.0', consumption='12.6', transmission='АКПП8 ZF',
           size='4856 x 1926 x 1900', mass='2405 - 2432', fuel='80', clearance='206',
           drive='полный', susp='независимая двухрычажная, с гидравлическими телескопическими амортизаторами\n'
           'зависимая пятирычажная с гидравлическими телескопическими амортизаторами и со стабилизаторами поперечной устойчивости',
           equip='Elite Premium',
           price='4 099 000 - 4 299 000', page='https://haval.ru/models/haval-h9-new/'),
    ModelD(brand='Haval', model='H3', engine='1.5T', power='143 - 177', torque='210 - 270',
           acceleration='', consumption='', transmission='DCT7',
           size='', mass='', fuel='', clearance='',
           drive='передний - подключаемый полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='',
           price='', page='https://haval.ru/about/media/press/debyut-haval-h3-sovershenno-novaya-model-v-ryadu-krossoverov/'),
    ModelD(brand='Haval', model='DargoX', engine='2.0T', power='192', torque='320',
           acceleration='10.0', consumption='9.2', transmission='роботизированная DCT7',
           size='4620 x 1890 x 1780', mass='1700 - 1815', fuel='60', clearance='200',
           drive='подключаемый полный', susp='независимая McPherson\nнезависимая многорычажная', equip='Elite Premium',
           price='3 349 000 - 3 549 000', page='https://haval.ru/models/new-haval-dargo/#dargox'),
    ModelD(brand='Haval', model='Dargo', engine='2.0T', power='192', torque='320',
           acceleration='10.0', consumption='9.2', transmission='роботизированная DCT7',
           size='4620 x 1890 x 1780', mass='1700 - 1815', fuel='60', clearance='200',
           drive='передний - подключаемый полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Comfort Elite Premium Tech_plus',
           price='3 049 000 - 3 599 000', page='https://haval.ru/models/new-haval-dargo/#dargo'),
    ModelD(brand='Haval', model='M6', engine='1.5T', power='143', torque='202',
           acceleration='12.9 - 12.7', consumption='8.2 - 8.3', transmission='механическая MT6 - роботизированная DCT7',
           size='4664 x 1830 x 1729', mass='1535 - 1565', fuel='55', clearance='170',
           drive='передний', susp='независимая McPherson\nнезависимая двурычажная', equip='MT DCT',
           price='2 179 000 - 2 299 000', page='https://haval.ru/models/new-haval-m6/'),
    ModelD(brand='Haval', model='F7x', engine='1.5T - 2.0T', power='150 - 190', torque='280 - 340',
           acceleration='11.0 - 9.0', consumption='8.4 - 9.4', transmission='роботизированная DCT7',
           size='4691 x 1866 x 1660', mass='1680 - 1785', fuel='56', clearance='190',
           drive='передний - подключаемый полный', susp='независимая McPherson\nнезависимая двурычажная',
           equip='Comfort Elite Premium Tech_plus',
           price='2 449 000 - 3 399 000', page='https://haval.ru/models/new-haval-f7x/'),
    ModelD(brand='Haval', model='F7', engine='1.5T - 2.0T', power='150 - 190', torque='280 - 340',
           acceleration='11.0 - 9.0', consumption='8.4 - 9.4', transmission='роботизированная DCT7',
           size='4691 x 1866 x 1690', mass='1680 - 1795', fuel='56', clearance='190',
           drive='передний - подключаемый полный', susp='независимая McPherson\nнезависимая двурычажная',
           equip='Comfort Elite Premium Tech_plus',
           price='2 449 000 - 3 349 000', page='https://haval.ru/models/new-haval-f7/'),
    ModelD(brand='Haval', model='Jolion', engine='1.5T', power='143 - 150', torque='210 - 230',
           acceleration='9.8', consumption='7.5 - 8.2', transmission='механическая MT6 - роботизированная DCT7',
           size='4472 x 1841 x 1574', mass='1420 - 1625', fuel='55', clearance='190',
           drive='передний - подключаемый полный', susp='полузависимая пружинная\n'
           'независимая многорычажная с гидравлическими телескопическими амортизаторами',
           equip='Comfort Elite Elite_plus Premium',
           price='1 949 000 - 2 599 000', page='https://haval.ru/models/new-haval-jolion/'),
    ModelD(brand='Haval', model='new_Jolion', engine='1.5T', power='143 - 150', torque='210 - 230',
           acceleration='9.8', consumption='7.5 - 8.2', transmission='механическая MT6 - роботизированная DCT7',
           size='4472 x 1841 x 1574', mass='1420 - 1625', fuel='55', clearance='190',
           drive='передний - подключаемый полный', susp='независимая McPherson\n'
           'полузависимая, пружинная, с гидравлическими телескопическими амортизаторами либо'
            ' независимая многорычажная с гидравлическими телескопическими амортизаторами',
           equip='Comfort Elite Premium Tech_plus',
           price='1 999 000 - 2 799 000', page='https://haval.ru/models/haval-jolion-new2024/'),
    ModelD(brand='Changan', model='Hunter_plus', engine='2.0T', power='226', torque='390',
           transmission='автоматическая AT8', size='5350 x 1980 x 1875', mass='2060', fuel='80', clearance='225',
           drive='полный', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'пружинная с гидравлическими телескопическими амортизаторами', equip='Comfort Luxe',
           price='3 479 900 - 3 529 900', page='https://changanauto.ru/models/hunter/'),
    ModelD(brand='Changan', model='CS95', engine='2.0T', power='226', torque='380',
           transmission='автоматическая AT8', size='4949 x 1940 x 1805', mass='2117', fuel='74', clearance='190',
           drive='полный', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'независимая многорычажная и гидравлическими телескопическими амортизаторами',
           equip='DLX Black_edition',
           price='4 249 900 - 4 319 900', page='https://changanauto.ru/models/cs95new/'),
    ModelD(brand='Changan', model='Uni-K', engine='2.0T', power='226', torque='380',
           transmission='автоматическая AT8', size='4865 x 1948 x 1695', mass='1920 - 2005', fuel='70', clearance='190',
           drive='передний - интеллектуальный полный', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'инезависимая многорычажная  гидравлическими телескопическими амортизаторами', equip='Comfort Luxe Tech',
           price='3 689 900 - 4 269 900', page='https://changanauto.ru/models/uni-k/'),
    ModelD(brand='Changan', model='Uni-T', engine='1.5T', power='167', torque='280',
           transmission='роботизированная DCT7', size='4515 x 1870 x 1565', mass='1465', fuel='55', clearance='180',
           drive='передний', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'инезависимая многорычажная  гидравлическими телескопическими амортизаторами', equip='Luxe Tech',
           price='2 899 900 - 2 999 900', page='https://changanauto.ru/models/uni-t/'),
    ModelD(brand='Changan', model='CS75_Plus', engine='1.5T', power='167', torque='265',
           transmission='автоматическая AT6', size='4700 x 1865 x 1710', mass='1610', fuel='58', clearance='190',
           drive='передний', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'инезависимая многорычажная  гидравлическими телескопическими амортизаторами', equip='Luxury',
           price='2 849 900', page='https://changanauto.ru/models/cs75plus/'),
    ModelD(brand='Changan', model='CS55_Plus', engine='1.5T', power='181', torque='280',
           transmission='роботизированная DCT7', size='4515 x 1865 x 1680', mass='1520 - 1535',
           fuel='55', clearance='171', drive='передний',
           susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'инезависимая многорычажная  гидравлическими телескопическими амортизаторами', equip='Comfort Luxe Tech',
           price='2 629 900 - 2 749 900', page='https://changanauto.ru/models/cs55plus/'),
    ModelD(brand='Changan', model='CS35_Plus', engine='1.4T', power='150', torque='255',
           transmission='роботизированная DCT7', size='4330 x 1825 x 1660', mass='1465', fuel='52', clearance='180',
           drive='передний', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'полузависимая с торсионной балкой и гидравлическими телескопическими амортизаторами', equip='Advance Tech',
           price='2 339 900 - 2 399 900', page='https://changanauto.ru/models/cs35plusnew/'),
    ModelD(brand='Changan', model='Uni-V', engine='1.5T', power='181', torque='300',
           transmission='роботизированная DCT7', size='4680 x 1838 x 1430', mass='1400', fuel='51', clearance='152',
           drive='передний', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'независимая многорычажная с гидравлическими телескопическими амортизаторами', equip='LX DLX',
           price='2 889 900 - 2 959 900', page='https://changanauto.ru/models/uni-v/'),
    ModelD(brand='Changan', model='Lamore', engine='1.5T', power='181', torque='300',
           transmission='роботизированная DCT7', size='4770 x 1840 x 1434', mass='1325', fuel='51', clearance='128',
           drive='передний', susp='независимая McPherson со стабилизатором поперечной устойчивости\n'
           'полузависимая с торсионной балкой с гидравлическими телескопическими амортизаторами', equip='???',
           price='2 789 900', page='https://changanauto.ru/models/lamore/'),
    ModelD(brand='Geely', model='Monjaro', engine='2.0T', power='238', torque='350',
           acceleration='7.7', consumption='8.5', transmission='автоматическая AT8',
           size='4770 x 1895 x 1689', mass='1855', fuel='62', clearance='210',
           drive='интеллектуальный полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Luxury Flagship Exclusive',
           price='4 694 990 - 4 994 990', page='https://www.geely-motors.com/model/monjaro/'),
    ModelD(brand='Geely', model='Okavango', engine='2.0T', power='200', torque='325',
           acceleration='9.6', consumption='7.7', transmission='роботизированная DCT7',
           size='4860 x 1910 x 1770', mass='1780', fuel='60', clearance='184',
           drive='передний', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Luxury Flagship',
           price='3 449 990 - 3 599 990', page='https://www.geely-motors.com/model/geely-okavango/'),
    ModelD(brand='Geely', model='Tugella', engine='2.0T', power='200 - 238', torque='350',
           acceleration='7.4 - 6.9', consumption='8.1', transmission='автоматическая AT8',
           size='4605 х 1878 х 1643', mass='1815', fuel='54', clearance='204',
           drive='интеллектуальный полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Luxury Flagship Flagship_sport',
           price='3 959 990 - 4 389 990', page='https://www.geely-motors.com/model/newtugella/'),
    ModelD(brand='Geely', model='Atlas_pro', engine='1.5T', power='150 - 177', torque='255',
           acceleration='11.0 - 9.9', consumption='7.4 - 6.8', transmission='автоматическая AT6 - роботизированная DCT7',
           size='4544 х 1831 х 1713', mass='1685 - 1780', fuel='58', clearance='171',
           drive='передний - интеллектуальный полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Comfort Luxury Flagship Flagship_plus',
           price='2 763 990 - 3 393 990', page='https://www.geely-motors.com/model/atlaspro/'),
    ModelD(brand='Geely', model='Atlas', engine='2.0T', power='200', torque='325',
           acceleration='8.2', consumption='7.4', transmission='роботизированная DCT7',
           size='4670 x 1900 x 1705', mass='1645', fuel='54', clearance='215',
           drive='передний', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Luxury Flagship Flagship_sport',
           price='3 194 990 - 3 494 990', page='https://www.geely-motors.com/model/geely-atlas-2024/'),
    ModelD(brand='Geely', model='Coolray', engine='1.5T', power='147', torque='270',
           acceleration='8.1', consumption='6.1', transmission='роботизированная DCT7',
           size='4380 х 1810 х 1615', mass='1432', fuel='45', clearance='180',
           drive='передний', susp='независимая McPherson\nнезависимая многорычажная', equip='Comfort Luxury Flagship Exclusive',
           price='2 609 990 - 2 949 990', page='https://www.geely-motors.com/model/geely-coolray-2023/'),
    ModelD(brand='Geely', model='X50', engine='1.5T', power='150', torque='255',
           acceleration='8.4', consumption='6.4', transmission='роботизированная DCT7',
           size='4330 х 1800 х 1609', mass='1415', fuel='45', clearance='180',
           drive='передний', susp='независимая McPherson\nполузависимая', equip='Active Style Prestige',
           price='2 290 990 - 2 500 990', page='https://www.geely-motors.com/model/belgee-x50/'),
    ModelD(brand='Geely', model='Emgrand', engine='1.5', power='122', torque='152',
           acceleration='12.9 - 12.6', consumption='', transmission='меъаника MT5 - автоматическая AT6',
           size='4638 x 1822 x 1460', mass='1270 - 1340', fuel='50', clearance='151',
           drive='передний', susp='независимая McPherson\nполузависимая', equip=' Standart  Comfort Luxury, Flagship',
           price='2 009 990 - 2 489 990', page='https://www.geely-motors.com/model/emgrand/'),
    ModelD(brand='Москвич', model='3_jaq_gs4', engine='1.5T', power='136', torque='200',
           acceleration='11.0', consumption='7.3', transmission='механика MT6 - вариатор CVT',
           size='4410 х 1800 х 1660', mass='1440', fuel='50', clearance='170',
           drive='передний', susp='независимая McPherson\nполузависимая с торсионом', equip='Стандарт Стандарт_плюс Комфорт',
           price='1 655 000 - 1 865 000', page='https://moskvich-auto.ru/models/moskvich-3/'),
    ModelD(brand='Москвич', model='6_jaq_j7', engine='1.5T', power='136 - 174', torque='200 - 280',
           acceleration='10.4 - 7.8', consumption='8.5', transmission='вариатор CVT6 - роботизированная DCT6',
           size='4770 х 1820 х 1492', mass='1460 - 1560', fuel='55', clearance='140',
           drive='передний', susp='независимая McPherson, независимая многорычажная', equip='Комфорт Бизнес Бизнес Техно',
           price='2 136 000 - 2 626 000', page='https://moskvich-auto.ru/models/moskvich-6/'),
    ModelE(brand='Москвич', model='3e_jaq_e40x', engine='Синхронный с постоянным магнитом, трёхфазный', power='193',
            torque='340', acceleration='', wlpt='410', size='4410 х 1800 х 1660', mass='2175', battery='65.7',
            clearance='170', drive='передний', susp='независимая McPherson\nполузависимая с торсионом',
            equip='3е', price='3 950 000', page='https://moskvich-auto.ru/models/moskvich-3e/'),
    ModelE(brand='Evolute', model='I_Jet', engine='асинхронный переменного тока, синхронный с постоянными магнитами', power='585',
            torque='940', acceleration='3.7', wlpt='483', size='4710 x 1930 x 1620',
            mass='2350', battery='92', clearance='', drive='интеллектуальный полный',
            susp='независимая на двойных поперечных рычагах\nнезависимая многорычажная',
            equip='', price='6 920 000', page='https://www.evolute.ru/models/i-jet/'),
    ModelE(brand='Evolute', model='I_Sky', engine='Синхронный двигатель с постоянными магнитами', power='204',
            torque='340', acceleration='8.6', wlpt='511', size='4565 x 1860 x 1680',
            mass='2025', battery='8.6', clearance='175', drive='передний', susp='независимая McPherson\nнезависимая многорычажная',
            equip='???', price='4 920 000', page='https://www.evolute.ru/models/i-sky/'),
    ModelE(brand='Evolute', model='I_Joy', engine='Синхронный двигатель с постоянными магнитами', power='163',
            torque='195', acceleration='8.9', wlpt='407', size='4385 x 1850 x 1650',
            mass='1756', battery='53', clearance='180', drive='передний', susp='независимая McPherson,\nзависимая торсионная балка',
            equip='???', price='3 995 000', page='https://www.evolute.ru/models/i-joy/'),
    ModelE(brand='Evolute', model='I_Pro', engine='Синхронный двигатель с постоянными магнитами', power='150',
            torque='210', acceleration='9.5', wlpt='433', size='4680 x 1720 x 1530',
            mass='1577', battery='53', clearance='120', drive='передний', susp='независимая McPherson,\nзависимая торсионная балка',
            equip='???', price='2 990 000', page='https://www.evolute.ru/models/i-pro/'),
    ModelE(brand='Evolute', model='I_Van', engine='Синхронный двигатель с постоянными магнитами', power='122',
            torque='300', acceleration='18.0', wlpt='400', size='5135 x 1720 x 1990',
            mass='???', battery='67.5', clearance='???', drive='задний', susp='независимая двурычажная,\nзависимая рессорная',
            equip='???', price='???', page='https://www.evolute.ru/models/i-van/'),
    ModelD(brand='Exeed', model='VX', engine='2.0T', power='249', torque='385', acceleration='9.3',
           consumption='8.2', transmission='автоматическая AT8', size='4970 x 1940 x 1792', mass='1995',
           fuel='65', clearance='200', drive='полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='President 6 President 7', price='6 500 000 - 6 700 000', page='https://exeed.ru/vx-fl/'),
    ModelD(brand='Exeed', model='RX', engine='2.0T', power='249', torque='385', acceleration='7.6',
           consumption='7.6', transmission='роботизированная DCT7', size='4775 х 1920 х 1671', mass='1865',
           fuel='65', clearance='187', drive='полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Prestige Platinum', price='5 150 000 - 5 450 000', page='https://exeed.ru/rx/'),
    ModelD(brand='Exeed', model='TXL', engine='1.6T - 2.0T', power='186 - 197', torque='275 - 375', acceleration='9.8 - 9.0',
           consumption='7.8 - 8.7', transmission='роботизированная DCT7', size='4780 x 1885 x 1730', mass='1796 - 1853',
           fuel='55', clearance='210', drive='полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Flagship Sport Edition', price='4 260 000 - 4 680 000', page='https://exeed.ru/txl/'),
    ModelD(brand='Exeed', model='LX', engine='1,5T - 1.6T', power='147 - 150', torque='210 - 275', acceleration='10.5 - 10.2',
           consumption='8.0 - 8.1', transmission='вариатор CVT9 - роботизированная DCT7', size='4533 x 1848 x 1690', mass='1536 - 1658',
           fuel='51 - 57', clearance='185', drive='передний - полный', susp='независимая McPherson\nнезависимая многорычажная',
           equip='Luxury Prestige_plus Luxury_plus Premium_plus', price='3 060 000 - 3 840 000', page='https://exeed.ru/lx/'),
    ModelD(brand='Tank', model='500', engine='гибридные 2.0T - 3.0T', power='299', torque='616 - 500', acceleration='7.9 - 9.6',
           consumption='8.5 - 11.5', transmission='автоматическая AT9', size='5078 х 1934 х 1905', mass='2605 - 2535',
           fuel='80', clearance='224', drive='полный с пониженной передачей', susp='независимая двурычажная\n'
           'зависимая рычажная и стабилизаторами поперечной устойчивости', equip='Urban Adventure Premium',
           price='6 499 000 - 7 099 000', page='https://tank.ru/models/tank-500/'),
    ModelD(brand='Tank', model='300', engine='2.0T', power='220', torque='380', acceleration='10.6', consumption='10.7',
           transmission='автоматическая AT8', size='4760 х 1930 х 1903', mass='2230', fuel='80', clearance='224',
           drive='полный с пониженной передачей', susp='независимая двурычажная\n'
           'зависимая рычажная и стабилизаторами поперечной устойчивости',
           equip='Adventure City_Adventure Premium City_premium', price='4 199 000 - 4 799 000', page='https://tank.ru/models/tank-300/'),
    ModelD(brand='Great Wall', model='Poer', engine='2.0T', power='150', torque='400', acceleration='16.0',
           consumption='9.9 - 9.5', transmission='механическая MT6 - автоматическая AT8', size='5403 x 1934 x 1886',
           mass='2155 - 2175', fuel='78', clearance='232', drive='полный с пониженной передачей',
           susp='независимая торсионная двухрычажная со стабилизатором поперечной устойчивости\n'
           'рессорная зависимая с гидравлическими телескопическими амортизаторами', equip='Comfort Premium',
           price='3 449 000 - 3 749 000', page='https://haval.ru/models/poer/'),
    ModelD(brand='Oting', model='Паладин', engine='2.0T', power='218', torque='360', acceleration='???',
           consumption='9.0', transmission='автоматическая AT8', size='4882 x 1850 x 1815',
           mass='1950', fuel='73', clearance='215', drive='задний / полный с пониженной передачей',
           susp='независимая двухрычажная\n'
           'зависимая неразрезной мост', equip='Делюкс Премиум Интеллект Престиж',
           price='3 799 000 - 4 499 000', page='https://otingcars.ru/models/paladin/'),
    ModelE(brand='Ora', model='O3', engine='переменного тока трехфазный синхронный', power='171', torque='250',
            acceleration='8.6 - 8.3', wlpt='500', size='4235 x 1825 x 1603', mass='', battery='63.1',
            clearance='145', drive='передний', susp='независимая McPherson\nполузависимая с гидравлическими телескопическими амортизаторами',
            equip='Premium GT', price='3 499 000 - 3 699 000', page='https://gwm-ora.ru/'),
    ModelHE(brand='Voyah', model='Free_evr', engine='генератор 1.5T и 2 синхронных электродвигателя '
            'с твердыми магнитами и жидкостным охлаждением', power='693',
            torque='1040', acceleration='4.5', wlpt='674', consumption='1.3', size='4905 x 1950 x 1645',
            mass='2290', fuel='56', battery='33', clearance='180', drive='полный',
            susp='двурычажная адаптивная пневмоподвеска\nмногорычажная адаптивная пневмоподвеска',
            equip='EVR', price='5 500 000', page='https://voyah.su/voyah-free-evr?main_menu/'),
    ModelHE(brand='Voyah', model='Free_evr_lr', engine='генератор 1.5T и 2 синхронных электродвигателя '
            'с твердыми магнитами и жидкостным охлаждением', power='489',
            torque='720', acceleration='4.8', wlpt='800', consumption='1.3', size='4905 x 1950 x 1645',
            mass='2280', fuel='56', battery='39', clearance='180', drive='полный',
            susp='двурычажная адаптивная пневмоподвеска\nмногорычажная адаптивная пневмоподвеска',
            equip='EVR Long Range', price='6 000 000', page='https://voyah.su/voyah-free-evr-long-range?main_menu/'),
    ModelE(brand='Voyah', model='Free_ev', engine='2 синхронных электродвигателя '
            'с твердыми магнитами и жидкостным охлаждением', power='489', torque='750',
           acceleration='4.7', wlpt='500', size='4905 x 1950 x 1645', mass='2340', battery='106',
           clearance='180', drive='полный',
           susp='двурычажная адаптивная пневмоподвеска\nмногорычажная адаптивная пневмоподвеска',
           equip='EV', price='9 390 000', page='https://voyah.su/voyah-free?main_menu/'),
    ModelE(brand='Voyah', model='Dream_ev', engine='2 электромотора', power='435', torque='620',
           acceleration='5.9', wlpt='482', size='5315 x 1985 x 1800', mass='2625', battery='108.7',
           clearance='150', drive='полный', susp='двурычажная адаптивная пневмоподвеска\n'
           'многорычажная адаптивная пневмоподвеска', equip='EV', price='11 290 000',
           page='https://voyah.su/voyah-dream-ev?main_menu/'),
    ModelHE(brand='Voyah', model='Dream_phev', engine='генератор 1.5T и 2 электромотора', power='394',
            torque='610', acceleration='6.6', wlpt='750', consumption='1.3', size='5315 x 1985 x 1800',
            mass='2540', fuel='51', battery='25.57', clearance='150', drive='полный',
            susp='двурычажная адаптивная пневмоподвеска\nмногорычажная адаптивная пневмоподвеска',
            equip='PHEV', price='10 290 000', page='https://voyah.su/voyah-dream?main_menu/'),
    ModelHE(brand='Voyah', model='Dream_first', engine='генератор 1.5T и 2 электромотора', power='394',
            torque='610', acceleration='6.6', wlpt='750', consumption='1.1', size='5315 x 1985 x 1800',
            mass='2672', fuel='51', battery='25.57', clearance='150', drive='полный',
            susp='двурычажная адаптивная пневмоподвеска\nмногорычажная адаптивная пневмоподвеска',
            equip='First', price='16 990 000', page='https://voyah.su/voyah-dream-first?main_menu/'),
    ModelE(brand='Voyah', model='  ', engine='2 электромотора', power='510', torque='730',
           acceleration='3.8', wlpt='483', size='5088 x 1970 x 1505', mass='2266', battery='82.11',
           clearance='121', drive='полный', susp='двурычажная адаптивная пневмоподвеска\n'
           'многорычажная адаптивная пневмоподвеска', equip='EV', price='8 490 000',
           page='https://voyah.su/voyah-passion?main_menu/'),
    ModelE(brand='Voyah', model='Passion_ev_lr', engine='2 электромотора', power='510', torque='730',
           acceleration='4.2', wlpt='608', size='5088 x 1970 x 1505', mass='2266', battery='108.73',
           clearance='121', drive='полный', susp='двурычажная адаптивная пневмоподвеска\n'
           'многорычажная адаптивная пневмоподвеска', equip='EV', price='9 790 000',
           page='https://voyah.su/voyah-passion-long-range?main_menu/'),
    ModelHE(brand='Voyah', model='Mhero_I', engine='генератор 1.5T и 3 электромотора', power='816',
            torque='1050', acceleration='6.0', wlpt='750', consumption='12.5', size='5066 x 2080 x 1934',
            mass='3160', fuel='84', battery='65', clearance='150', drive='полный',
            susp='независимая двурычажная адаптивная пневмоподвеска\nнезависимая двурычажная адаптивная пневмоподвеска',
            equip='EVR', price='15 990 000', page='https://mhero.su/'),
]
