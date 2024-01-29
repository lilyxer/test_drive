from dataclasses import dataclass, field

@dataclass
class Brand:
    name: str = field(default='')
    concern: str = field(default='')
    local: str = field(default='')
    foundation: int = field(default='')
    type_of: str = field(default='')
    start: int = field(default='')
    in_russia: str = field(default='')
    year: str = field(default='')
    site: str = field(default='')
    lang: str = field(default='')

    def __post_init__(self):
        self.name = f'{self.name.upper()}'
        self.concern = f'\n\nВходит в концерн <b>{self.concern}</b>' if self.concern else ''
        self.local = f'Локализованная версия <b>{self.local}</b>,' if self.local else ''
        self.foundation = f' основание в <b>{self.foundation}</b>\n'
        self.type_of = f'Основными типами автомобилей компании являются <b>{self.type_of}</b>\n'
        self.start = f'Продажи автомобилей в России начались в <b>{self.start}</b>\n'
        self.in_russia = f'В России собирались на заводе <b>{self.in_russia}</b>' if self.in_russia else ''
        self.year = f' _{self.year}_\n' if self.year else ''
        self.site = f'\n<b><a href="{self.name}">официальная страница {self.site}</a></b>'

    def __str__(self):
        return ''.join(self.__dict__.values())


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
                f'<b>Двигатель:</b>\nБензин {self.engine}\n'
                f'<b>Мощность:</b>\n{self.power} л.с.\n'
                f'<b>Момент:</b>\n{self.torque} Нм\n'
                f'<b>Разгон до 100 км/ч:</b>\n{self.acceleration} сек\n'
                f'<b>Средний расход топлива</b>\n{self.consumption}\n\n'
                f'<b>Трансмиссия автомобиля:</b>\n{self.transmission}\n\n'
                f'<b>Габариты автомобиля:</b>\n{self.size}\n'
                f'<b>Масса автомобиля:</b>\n{self.mass}кг\n'
                f'<b>Объём бака:</b>\n{self.fuel} л\n'
                f'<b>Дорожный просвет:</b>\n{self.clearance} мм\n\n'
                f'<b>Тип привода:</b>\n{self.drive}\n'
                f'<b>Подвеска:</b>\n{self.susp}\n\n'
                f'<b>Комплектации:</b>\n{self.equip}\n'
                f'<b>Цена:</b>\n{self.price} руб\n\n'
                f'<b><a href="{self.page}">официальная страница {self.model}</a></b>')


@dataclass
class ModelHE:
    brand: str = ''
    model: str = ''
    engine: str = ''
    power: str = ''
    torque: str = ''
    acceleration: str = ''
    wlpt: str = ''
    size: str = ''
    mass: str = ''
    battery: str = ''
    clearance: str = ''
    drive: str = ''
    susp: str = ''
    equip: str = ''
    price: str = ''
    page: str =''

    def __str__(self) -> str:
        return (f'{self.brand.upper()}\n'
                f'{self.model.upper()}\n\n'
                f'<b>Двигатель:</b>\nЭлектрический {self.engine}\n'
                f'<b>Пиковая мощность:</b>\n{self.power} л.с.\n'
                f'<b>Момент:</b>\n{self.torque} Нм\n'
                f'<b>Разгон до 100 км/ч:</b>\n{self.acceleration} сек\n'
                f'<b>Запас хода WLTP</b>\n{self.wlpt} км\n\n'
                f'<b>Габариты автомобиля:</b>\n{self.size}\n'
                f'<b>Масса автомобиля:</b>\n{self.mass} кг\n'
                f'<b>Объём батареи:</b>\n{self.battery} кВт\ч\n'
                f'<b>Дорожный просвет:</b>\n{self.clearance} мм\n\n'
                f'<b>Тип привода:</b>\n{self.drive}\n'
                f'<b>Подвеска:</b>\n{self.susp}\n\n'
                f'<b>Комплектации:</b>\n{self.equip}\n'
                f'<b>Цена:</b>\n{self.price} руб\n\n'
                f'<b><a href="{self.page}">официальная страница {self.model}</a></b>')
