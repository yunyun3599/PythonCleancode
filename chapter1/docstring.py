from enum import Enum
from datetime import time


class TimeZone(Enum):
    morning = "morning"
    afternoon = "afternoon"
    evening = "evening"
    night = "night"


def get_time_zone(input_time: time) -> str:
    """
    시간을 받으면 5시 ~ 12까지는 morning,
    12시 ~ 17시까지는 afternoon,
    17시 ~ 21시까지는 evening,
    21시 ~ 5시 까지는 night을 반환한다.

    :param input_time: 시간대 문자열로 변경을 원하는 시간
    :return: 시간대 문자열
    """
    if type(input_time) != time:
        raise TypeError("input type must be time")

    if input_time.hour < 5:
        return TimeZone.night.value
    elif input_time.hour < 12:
        return TimeZone.morning.value
    elif input_time.hour < 17:
        return TimeZone.afternoon.value
    elif input_time.hour < 21:
        return TimeZone.evening.value
    else:
        return TimeZone.night.value


print(get_time_zone.__doc__)
print("9:00 is " + get_time_zone(time(9, 00, 00)))
print("14:00 is " + get_time_zone(time(15, 00, 00)))
print("20:00 is " + get_time_zone(time(20, 00, 00)))
print("3:00 is " + get_time_zone(time(3, 00, 00)))
print("3:00 is " + get_time_zone(time("시간이 아닌데...")))
