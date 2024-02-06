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

    def __str__(self):
        ru =  f'В России собирались на заводе <b>{self.in_russia}</b> {self.year}\n' if self.in_russia else ''
        con = f'Входит в концерн <b>{self.concern}</b>, ' if self.concern else f'Локализованная версия <b>{self.local}</b>,'
        return (f'{self.name.upper()}\n\n'
                f'{con}основание в <b>{self.foundation}</b>\n'
                f'Основными типами автомобилей компании являются <b>{self.type_of}</b>\n'
                f'Продажи автомобилей в России начались в <b>{self.start}</b>\n'
                f'{ru}'
                f'<b><a href="{self.site}">официальная страница {self.name}</a></b>')


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
                f'<b>Двигатель:</b> ..... Бензин {self.engine}\n'
                f'<b>Мощность:</b> ..... {self.power} л.с.\n'
                f'<b>Момент:</b> ..... {self.torque} Нм\n'
                f'<b>Разгон до 100 км/ч:</b> ..... {self.acceleration} сек\n'
                f'<b>Средний расход топлива</b> ..... {self.consumption}\n\n'
                f'<b>Трансмиссия автомобиля:</b> ..... {self.transmission}\n\n'
                f'<b>Габариты автомобиля:</b> ..... {self.size}\n'
                f'<b>Масса автомобиля:</b> ..... {self.mass}кг\n'
                f'<b>Объём бака:</b> ..... {self.fuel} л\n'
                f'<b>Дорожный просвет:</b> ..... {self.clearance} мм\n\n'
                f'<b>Тип привода:</b> ..... {self.drive}\n'
                f'<b>Подвеска:</b> ..... {self.susp}\n\n'
                f'<b>Комплектации:</b> ..... {self.equip}\n'
                f'<b>Цена:</b> ..... {self.price} руб\n\n'
                f'<b><a href="{self.page}">официальная страница {self.model}</a></b>')


@dataclass
class ModelE:
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
                f'<b>Двигатель:</b> ..... Электрический {self.engine}\n'
                f'<b>Пиковая мощность:</b> ..... {self.power} л.с.\n'
                f'<b>Момент:</b> ..... {self.torque} Нм\n'
                f'<b>Разгон до 100 км/ч:</b> ..... {self.acceleration} сек\n'
                f'<b>Запас хода WLTP</b> ..... {self.wlpt} км\n\n'
                f'<b>Габариты автомобиля:</b> ..... {self.size}\n'
                f'<b>Масса автомобиля:</b> ..... {self.mass} кг\n'
                f'<b>Объём батареи:</b> ..... {self.battery} кВт\ч\n'
                f'<b>Дорожный просвет:</b> ..... {self.clearance} мм\n\n'
                f'<b>Тип привода:</b> ..... {self.drive}\n'
                f'<b>Подвеска:</b> ..... {self.susp}\n\n'
                f'<b>Комплектации:</b> ..... {self.equip}\n'
                f'<b>Цена:</b> ..... {self.price} руб\n\n'
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
    consumption: str = '???'
    size: str = ''
    mass: str = ''
    fuel: str = '???'
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
                f'<b>Двигатель:</b> ..... Электрический {self.engine}\n'
                f'<b>Пиковая мощность:</b> ..... {self.power} л.с.\n'
                f'<b>Момент:</b> ..... {self.torque} Нм\n'
                f'<b>Разгон до 100 км/ч:</b> ..... {self.acceleration} сек\n'
                f'<b>Средний расход топлива</b> ..... {self.consumption}\n\n'
                f'<b>Запас хода WLTP</b> ..... {self.wlpt} км\n\n'
                f'<b>Габариты автомобиля:</b> ..... {self.size}\n'
                f'<b>Масса автомобиля:</b> ..... {self.mass} кг\n'
                f'<b>Объём бака:</b> ..... {self.fuel} л\n'
                f'<b>Объём батареи:</b> ..... {self.battery} кВт\ч\n'
                f'<b>Дорожный просвет:</b> ..... {self.clearance} мм\n\n'
                f'<b>Тип привода:</b> ..... {self.drive}\n'
                f'<b>Подвеска:</b> ..... {self.susp}\n\n'
                f'<b>Комплектации:</b> ..... {self.equip}\n'
                f'<b>Цена:</b> ..... {self.price} руб\n\n'
                f'<b><a href="{self.page}">официальная страница {self.model}</a></b>')