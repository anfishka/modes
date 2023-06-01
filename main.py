# BLACK = '\033[0;30m'
# RED = '\033[0;31m'
# GREEN = '\033[0;32m'
# YELLOW = '\033[0;33m'
# BLUE = '\033[0;34m'
# PURPLE = '\033[0;35m'
# CYAN = '\033[0;36m'
# WHITE = '\033[0;37m'
# RESET = '\033[0m'

# Легкое
# Пользователь вводит НОМЕР ДНЯ НЕДЕЛИ, программа выводит название этого дня
# Интересное
# Пользователь вводит обьем бака и расход по городу.
# Вывести сколько километров он проедет по трассе
# с учетом
# - уменьшения расхода в теплую погоду на  30%
# - уменьшения расхода в холодную погоду на  23%

choice = int(input('\033[0;32mСделайте ваш выбор: 1 - Узнать день недели 2 - Расчитать сколько км можно проехать по трассе '))

if(choice != 1 and choice != 2):
    print('\033[0;31mНеправильный ввод!')
elif(choice == 1):
    day_n = int(input('\033[0;33mВведите цифру от 1 до 7, чтобы узнать какой это день:'))
    days_of_the_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Cуббота', 'Воскресенье']
    if ( 1 <= day_n <= 7):
            print(str(day_n) + ' это ' + str(days_of_the_week[day_n - 1]))
    else:
        print('\033[0;31mНеправильный ввод!')
else:
    city_fuel_consumption = float(input('\033[0;32mВведите ваш расход по городу: '))
    fuel_tank_capacity = float(input('Введите ваш обьем бака: '))
    warm_weather = 0.30
    cold_weather = 0.23
    if city_fuel_consumption > 0 and fuel_tank_capacity > 0:
        res_warm_weather = (fuel_tank_capacity / city_fuel_consumption) * 100 * (1 - warm_weather)
        res_cold_weather = (fuel_tank_capacity / city_fuel_consumption) * 100 * (1 - cold_weather)
        print('\033[0;33mПо трассе в теплую погоду Вы проедите: ' + str(res_warm_weather) + ' километров')
        print('По трасее в холодную погоду Вы проедите: ' + str(res_cold_weather) + ' километров')
    else:
        print('\033[0;31mНеправильный ввод!')


