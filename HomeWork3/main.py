import random
import time


def tsToDate(timestamp):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1970

    days_till_now = timestamp // (24 * 60 * 60)
    extra_time = timestamp % (24 * 60 * 60)
    extra_days = 0 
    is_leap = False

    while days_till_now >= 365:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            is_leap = True
            if days_till_now < 366:
                break

            days_till_now -= 366
        else:
            days_till_now -= 365

        year += 1


    extra_days = days_till_now + 1


    month = 0
    month_index = 0

    if is_leap:
        while True:
            if month_index == 1:
                if extra_days - 29 < 0:
                    break

                month += 1
                extra_days -= 29
            else:
                if extra_days - days_in_month[month_index] < 0:
                    break

                month += 1
                extra_days -= days_in_month[month_index]

            month_index += 1
    else:
        while True:
            if extra_days - days_in_month[month_index] < 0:
                break

            month += 1
            extra_days -= days_in_month[month_index]
            month_index += 1


    if extra_days > 0:
        month += 1
        day = extra_days
    else:
        if month == 2 and is_leap == 1:
            day = 29
        else:
            day = days_in_month[month - 1]

    hours = extra_time // (60 * 60)
    minutes = (extra_time % (60 * 60)) // 60
    seconds = (extra_time % (60 * 60)) % 60

    date_str = str(int(year)) + "-" + str(int(month)) + "-" + str(int(day))
    time_str = str(int(hours + 4)) + ":" + str(int(minutes)) + ":" + str(int(seconds))

    timestamp_str = date_str + " " + time_str

    return timestamp_str


def MinOn(listik):
    minim = listik[0]
    for i in range(len(listik)):
        if minim > listik[i]:
            minim = listik[i]
    return minim


if __name__ == "__main__":
    print("Задание 1")
    ts = 1678003932
    print(tsToDate(time.time()))
    
    print("\nЗадание 2")
    listik = []
    for i in range(random.randint(5, 10)):
        listik.append(random.randint(-10, 10))

    print("Исходный список: " + str(listik) + "\n")

    print("Если массив не отсортирован")
    print("Минимальное число с сложностью O(n): " + str(MinOn(listik)) + "\n")

    print("Если массив отсортирован")
    listik = sorted(listik)
    print(listik)
    print("Минимальное число с сложностью O(1): " + str(listik[0]) + "\n")