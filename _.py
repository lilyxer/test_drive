from dataclasses import dataclass

@dataclass
class ModelD:
    brand: str = '???'
    model: str = '???'
    engine: str = '???'
    power: str = '???'
    torque: str = '???'
    acceleration: str = '???'
    consumption: str = '???'
    transmission: str = '???'
    size: str = '???'
    mass: str = '???'
    fuel: str = '???'
    clearance: str = '???'
    drive: str = '???'
    susp: str = '???'
    equip: str = '???'
    price: str = '???'
    page: str = '???'

    def __str__(self) -> str:
        return (f'{self.brand.upper()}\n'
                f'{self.model.upper()}\n\n'
                f'*Двигатель:*\nБензин {self.engine}\n'
                f'*Мощность:*\n{self.power} л.с.\n'
                f'*Момент:*\n{self.torque} Нм\n'
                f'*Разгон до 100 км/ч:*\n{self.acceleration} сек\n'
                f'*Средний расход топлива*\n{self.consumption}\n\n'
                f'*Трансмиссия автомобиля:*\n{self.transmission}\n\n'
                f'*Габариты автомобиля:*\n{self.size}\n'
                f'*Масса автомобиля:*\n{self.mass}кг\n'
                f'*Объём бака:*\n{self.fuel} л\n'
                f'*Дорожный просвет:*\n{self.clearance} мм\n\n'
                f'*Тип привода:*\n{self.drive}\n'
                f'*Подвеска:*\n{self.susp}\n\n'
                f'*Комплектации:*\n{self.equip}\n'
                f'*Цена:*\n{self.price} руб\n\n'
                f'*[официальная страница {self.model}]({self.page})*')


@dataclass
class ModelHE:
    brand: str = ''
    model: str = ''
    engine: str = ''
    power: str = ''
    torque: str = ''
    acceleration: str = ''
    wltc: str = ''
    size: str = ''
    mass: str = ''
    battery: str = ''
    clearance: str = ''
    drive: str = ''
    susp: str = ''
    equip: str = ''
    price: str = ''
    page: str =''

cars: list[ModelD] = [
    ModelD(brand='Chery', model='tiggo_8_pro_max', engine='2.0T', power='197', torque='375',
           acceleration='8.4', consumption='8.3', transmission='роботизированная DCT7',
           size='4720 х 1860 х 1705', mass='1829', fuel='57', clearance='190',
           drive='интеллектуальный полный', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Dreamline, Ultimate', price='4 160 000 - 4 651 000', page='https://www.chery.ru/models/newtiggo8promax/'),
    ModelD(brand='Chery', model='tiggo_7_pro_max', engine='1.5T - 1.6T', power='147 - 150', torque='210 - 275',
           acceleration='9.8', consumption='8.2 - 7.7', transmission='Вариатор CVT9 - роботизированная DCT7',
           size='4500 x 1842 x 1705', mass='1540 - 1643', fuel='51', clearance='190',
           drive='передний - интеллектуальный полный', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Elite(FWD), Prestige(FWD), Ultimate(FWD), Prestige(AWD), Ultimate(AWD)',
           price='2 820 000 - 3 570 000', page='https://www.chery.ru/models/tiggo7promax/'),
    ModelD(brand='Chery', model='tigo_4_pro', engine='1.5 - 1.5T', power='113 - 147', torque='138 - 210',
           acceleration='14.6 - 9.7', consumption='7.4 - 7.1', transmission='Механика MT5 - Вариатор CVT7 - Вариатор CVT9',
           size='4318 x 1831 x 1662', mass='1350 - 1439', fuel='51', clearance='190',
           drive='передний', susp='независимая типа McPherson\nполузависимая, пружинная, с гидравлическими телескопическими '
          'амортизаторами и стабилизатором поперечной устойчивости',
           equip='Action MT, Action, Family, Travel, Style, Ultimate',
           price='2 120 000 - 2 620 000', page='https://www.chery.ru/models/tiggo4pro/'),
    ModelD(brand='Chery', model='arrizo_8', engine='1.6T', power='186', torque='275',
           acceleration='8.9', consumption='6.2', transmission='роботизированная DCT7',
           size='4757 x 1832 x 1469', mass='1489 - 1538', fuel='55', clearance='144',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Prestige, Ultimate, Ultimate SE',
           price='3 410 000 - 3 560 000', page='https://www.chery.ru/models/arrizo8/'),
    ModelD(brand='Jetour', model='T2', engine='2.0T', power='245', torque='375',
           acceleration='8.7', consumption='9.3', transmission='роботизированная DCT7',
           size='4785 x 2006 x 1880', mass='1915 - 1955', fuel='70', clearance='220',
           drive='интеллектуальный полный', susp='независимая типа McPherson, с телескопическими амортизаторами,'
           ' со стабилизатором поперечной устойчивости\nнезависимая, многорычажная, пружинная, с'
           ' телескопическими амортизаторами, со стабилизатором поперечной устойчивости',
           price='ПРЕДЗАКАЗ', page='https://jetour-ru.com/models/T2/'),
    ModelD(brand='Jetour', model='X90_PLUS', engine='1.6T - 2.0T', power='190 - 245', torque='275 - 375',
           acceleration='11.0 - 8.5', consumption='8.1 - 8.0', transmission='роботизированная DCT7',
           size='4858 x 1925 x 1780', mass='1709 -1790', fuel='57', clearance='210',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort, Elite, Luxury',
           price='3 399 900 - 3 889 900', page='https://jetour-ru.com/models/x90Plus/'),
    ModelD(brand='Jetour', model='X70_PLUS', engine='1.6T', power='190', torque='275',
           acceleration='11.0 - 8.5', consumption='8.1 - 8.0', transmission='роботизированная DCT7',
           size='4724 x 1900 x 1720', mass='1662 - 1694', fuel='57', clearance='204',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort, Luxury',
           price='2 999 900 - 3 299 900', page='https://jetour-ru.com/models/x70Plus/'),
    ModelD(brand='Jetour', model='DASHING', engine='1.5T - 1.6T', power='147 - 190', torque='210 - 275',
           acceleration='13.2 - 10.5', consumption='7,5 - 8.4', transmission='механика МТ5 - роботизированная DCT6/DCT7',
           size='4590 x1900 x 1685', mass='1570 - 1655', fuel='57', clearance='160',
           drive='передний', susp='независимая типа McPherson\nнезависимая многорычажная',
           equip='Comfort plus, Comfort, Elite, Luxury',
           price='2 489 900 - 3 189 900', page='https://jetour-ru.com/models/dashing/'),
    ModelD(brand='Omoda', model='C5', engine='1.5T - 1.6T', power='147 - 150', torque='210 - 275',
           acceleration='9.9 - 8.6', consumption='7,1 - 7.4', transmission='Вариатор CVT9 - роботизированная DCT7',
           size='4400 x 1830 x 1588', mass='1456 - 1610', fuel='52 - 57', clearance='190 - 180',
           drive='передний - интеллектуальный полный', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами/многорычажная, пружинная, с гидравлическими телескопическими амортизаторами',
           equip='Joy, Lifestyle, Ultimate, Active, Supreme',
           price='2 679 900 - 3 309 900', page='https://omoda.ru/models/modelc5/'),
    ModelD(brand='Omoda', model='S5_GT', engine='1.6T', power='150', torque='275',
           acceleration='7.5', consumption='6.9', transmission='роботизированная DCT7',
           size='4691 x 1814 x 1493', mass='1419', fuel='48', clearance='160',
           drive='передний', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами', equip='Neo, Ultra',
           price='2 759 900 - 2 859 900', page='https://omoda.ru/models/s5gt/'),
    ModelD(brand='Omoda', model='S5', engine='1.5 - 1.5T', power='113 - 1147', torque='138 - 210',
           acceleration='13.2 - 9.7', consumption='7.3 - 6.9', transmission='Вариатор CVT7 - Вариатор CVT9',
           size='4644 x 1814 x 1493', mass='1386 - 1395', fuel='48', clearance='160',
           drive='передний', susp='независимая типа McPherson\nполузависимая, с гидравлическими'
           ' телескопическими амортизаторами', equip='Life, Tech, Ultra',
           price='2 249 900 - 2 549 900', page='https://omoda.ru/models/models5/'),
]



brands = sorted({x.brand for x in cars})
models = [x.model for x in cars if x.brand == 'Chery']
car = str(*(x for x in cars if x.model == 'T2'))
# print(car)