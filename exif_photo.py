from exif import Image
from colorama import init, Fore, Back, Style
import webbrowser

def add_photo_format(old_list):
    print(Fore.BLACK + Back.WHITE + f'Программа проверяет фотографии следующих форматов: {old_list}'.ljust(50))
    print()
    print(Fore.BLACK + Back.WHITE + 'Хотите добавить ещё новый формат? Введите yes или no'.ljust(50))
    while check_answer_yes_no():
        print(Fore.BLACK + Back.WHITE + 'Введите новый формат, пример - .jpeg'.ljust(50))
        new_format = input()
        if new_format[0] != '.':
            print(Fore.RED + Back.YELLOW + 'Формат должен начинаться с точки'.ljust(50))
            print()
            print(Fore.BLACK + Back.WHITE + 'Хотите ввести заново формат фотографии? Напишите yes или no'.ljust(50))
        else:
            old_list.append(new_format)
            print(Fore.BLACK + Back.WHITE + f'Программа проверяет фотографии следующих форматов: {old_list}'.ljust(50))
            print()
            print(Fore.BLACK + Back.WHITE + 'Хотите добавить ещё новый формат? Введите yes или no'.ljust(50))
    return old_list
    
def name_photo():                                                               # Пользователь указывает имя фото включая формат, которое необходимо проверить на методанные           
    print(Fore.BLACK + Back.WHITE + 'Введите название имя.формат, пример: IMG_1241.jpeg'.ljust(50))
    while True:
        el = input()
        for i in list_of_format:
            if i in el:
                return el
        print(Fore.RED + Back.YELLOW + 'Некоректный формат ввода названия фото <имя фото>.<формат фото>'.ljust(50))

def check_exif_data(photo):                                                     # Проверяем наличие методанных в фото
    if photo.has_exif:
        print(Fore.BLACK + Back.WHITE + f"Фото имеет EXIF методанные(version {photo.get('exif_version', 'нет данных')}).".ljust(50))
        return True
    else:
        print(Fore.BLACK + Back.WHITE + "Фото не имеет EXIF методанные.".ljust(50))
        return False

def check_objects_in_photo(photo):                                              # Вывод количества и объектов методанных в фото
    global photo_members
    photo_members = dir(photo)    
    print(Fore.BLACK + Back.WHITE + f'Данное фото содержит {len(photo_members)} объектов:'.ljust(50))
    for el in photo_members:
        print(' '*10, el)

def device_information(photo):
    make_photo = photo.get('make', 'нет данных')
    model_photo = photo.get('model', 'нет данных')    
    print(Fore.BLACK + Back.WHITE + f"Информация об устройстве".ljust(50))
    print(Fore.BLACK + Back.YELLOW + f"Производитель: {make_photo}".ljust(50))
    print(Fore.BLACK + Back.YELLOW + f"Модель: {model_photo}".ljust(50))  
    print("-------------------------")
    
def find_datetime(photo):
    print(Fore.BLACK + Back.WHITE + f"Дата/время".ljust(50))
    print(Fore.BLACK + Back.YELLOW + f"{photo.get('datetime_original', 'нет данных')}.{photo.get('subsec_time_original', 'нет данных')} {photo.get('offset_time', '')}".ljust(50))
    print("-------------------------")
    
def format_dms_coordinates(coordinates):
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    webbrowser.open_new_tab(url)

def gps_coord(photo):          
    if 'gps_latitude' in photo_members and 'gps_longitude' in photo_members:  
        print(Fore.BLACK + Back.WHITE + 'Координаты места где была сделана фотография'.ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Широта (DMS): {format_dms_coordinates(photo.gps_latitude)} {photo.gps_latitude_ref}".ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Долгота (DMS): {format_dms_coordinates(photo.gps_longitude)} {photo.gps_longitude_ref}".ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Широта (DD): {dms_coordinates_to_dd_coordinates(photo.gps_latitude, photo.gps_latitude_ref)}".ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Долгота (DD): {dms_coordinates_to_dd_coordinates(photo.gps_longitude, photo.gps_longitude_ref)}".ljust(50))
        print("-------------------------")
        draw_map_for_location(photo.gps_latitude, 
                              photo.gps_latitude_ref, 
                              photo.gps_longitude,
                              photo.gps_longitude_ref)        
    else:
        print(Fore.BLACK + Back.YELLOW + 'В методанных нет объектов gps позиционирования'.ljust(50))
def degrees_to_direction(degrees):
    COMPASS_DIRECTIONS = [
        "N",
        "ССВ",
        "СВ",
        "ВСВ",
        "В", 
        "ВЮВ", 
        "ВЮ", 
        "ЮЮВ",
        "Ю", 
        "ЮЮЗ", 
        "ЗЮ", 
        "ЗЮЗ", 
        "З", 
        "ЗСЗ", 
        "СЗ", 
        "ССЗ"
    ]
    
    compass_directions_count = len(COMPASS_DIRECTIONS)
    compass_direction_arc = 360 / compass_directions_count
    return COMPASS_DIRECTIONS[int(degrees / compass_direction_arc) % compass_directions_count]

def format_direction_ref(direction_ref):
    direction_ref_text = Fore.BLACK + Back.YELLOW + "(Неизвестно истинный или магнитный северер)"
    if direction_ref == "T":
        direction_ref_text = Fore.BLACK + Back.YELLOW + "Истинный север"
    elif direction_ref == "M":
        direction_ref_text = Fore.BLACK + Back.YELLOW + "Магнитный север"
    return direction_ref_text.ljust(50)

def degrees_info(photo):
    if 'gps_img_direction' in photo_members:
        print(Fore.BLACK + Back.WHITE + f"Направление объектива камеры по сторона света".ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Направление: {degrees_to_direction(photo.gps_img_direction)} ({photo.gps_img_direction}°)".ljust(50))
        print(Fore.BLACK + Back.YELLOW + f"Привязка: {format_direction_ref(photo.gps_img_direction_ref)}".ljust(50))
        if 'gps_altitude' in photo_members:
            print(Fore.BLACK + Back.YELLOW + f"Высота: {format_altitude(photo.gps_altitude, photo.gps_altitude_ref)}".ljust(50))
        print("-------------------------")

def format_altitude(altitude, altitude_ref):
    altitude_ref_text = "(неизвестно выше или ниже уровня моря)"
    if altitude_ref == 0:
        altitude_ref_text = "выше уровня моря"
    elif altitude_ref == 1:
        altitude_ref_text = "ниже уровня моря"
    return f"{altitude} meters {altitude_ref_text}"

def intro():
    print(Fore.BLUE + Back.WHITE + 'ПРОГРАММА ПРОВЕРЯЕТ ФОТОГРАФИЮ НА НАЛИЧИЕ EXIF ДАННЫХ'.ljust(50))
    print("-------------------------")
    print(Fore.YELLOW + 'Чтобы программа проверила фотографию:')
    print(Fore.YELLOW + '1. Переместить фотографию в туже папку, где находится программа')
    print(Fore.YELLOW + '2. Указать полное имя фотографии')
    print("-------------------------")

def check_answer_yes_no():
    while True:
        answer = input().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print(Fore.BLACK + Back.YELLOW + 'Введите yes или no'.ljust(50))
            
#------------------------main------------------------
init(autoreset=True)
intro()
list_of_format = [".jpg", ".jpeg", ".bmp", ".HEIC"]    
list_of_format = add_photo_format(list_of_format) 

while True:
    flag = True
    while flag:
        try:
            with open(name_photo(), "rb") as photo_file:
                photo_image = Image(photo_file)
        except Exception:
            print(Fore.RED + Back.YELLOW + 'Фото не найдено'.ljust(50))
        else: flag = False
    check_exif = check_exif_data(photo_image)
    if check_exif:
        check_objects_in_photo(photo_image)
        device_information(photo_image)
        find_datetime(photo_image)
        gps_coord(photo_image)
        degrees_info(photo_image)
    print(Fore.BLACK + Back.WHITE + 'Проверить ещё фотографию? Напишите yes или no'.ljust(50))
    if not check_answer_yes_no():
        print(Fore.RED + Back.WHITE + 'ПРОГРАММА ЗАВЕРШЕНА'.ljust(50))
        value = input()
        break
