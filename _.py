from lexicon.classes import ModelD, ModelHE
cars: list[ModelD, ModelHE] = [
    ModelHE(brand='Ora', model='O3', engine='переменного тока трехфазный синхронный', power='171', torque='250',
            acceleration='8.6 - 8.3', wlpt='500', size='4235 x 1825 x 1603', mass='', battery='63.1',
            clearance='145', drive='передний', susp='независимая McPherson\nполузависимая с гидравлическими телескопическими амортизаторами',
            equip='Premium GT', price='3 899 000 - 3 999 000', page='https://gwm-ora.ru/')

    # ModelD(brand='', model='', engine='', power='', torque='', acceleration='', consumption='', transmission='', size='', mass='', fuel='', clearance='', drive='', susp='', equip='', price='', page=''),
]





brands = sorted({x.brand for x in cars})
models = [x.model for x in cars if x.brand == 'Chery']
car = str(*(x for x in cars if x.model == 'T2'))
# print(car)