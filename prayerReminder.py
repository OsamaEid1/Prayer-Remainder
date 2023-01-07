# source: https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf
# source of api: https://aladhan.com/prayer-times-api#GetTimingsByAddresss

from plyer import notification
import requests
import time

# Secs time that i want the notfic appear before
notifc_time = 20 * 60

next_pray = ""

def get_remaining_secs_to_next_prayer(fajr, dhuhr, asr, maghrib, isha):
    global next_pray

    # Get time for now
    t = time.time()
    time_now = time.ctime(t)

    # Extract hours and minutes from time strings to calculate the diferenet
    time_now_h = int(time_now[11:13])
    time_now_m = int(time_now[14:16])

    fajr_h = int(fajr[:2])
    fajr_m = int(fajr[3:])

    dhuhr_h = int(dhuhr[:2])
    dhuhr_m = int(dhuhr[3:])

    asr_h = int(asr[:2])
    asr_m = int(asr[3:])

    maghrib_h = int(maghrib[:2])
    maghrib_m = int(maghrib[3:])

    isha_h = int(isha[:2])
    isha_m = int(isha[3:])

    # Get the next pray and calculate the remaining time and return the seconds are left
    if time_now_h > isha_h:
        next_pray += "اقتربت صلاةُ الفجْر"
        secs_to_display_notfic = ((((24 - time_now_h) + fajr_h) * 60) + (fajr_m - time_now_m)) * 60

        # Case of we passed the pray just for minutes Wait for this hour pass and return0 to call the func again
        if secs_to_display_notfic < 0:
            time.sleep((60 * 60) - (time_now_m * 60))
            return 0
        else:
            return secs_to_display_notfic
    elif time_now_h <= dhuhr_h:
        next_pray += "اقتربت صلاةُ الظُهر"
        secs_to_display_notfic = (((dhuhr_h - time_now_h) * 60) + (dhuhr_m - time_now_m)) * 60

        # Case of we passed the pray just for minutes Wait for this hour pass and return0 to call the func again
        if secs_to_display_notfic < 0:
            time.sleep((60 * 60) - (time_now_m * 60))
            return 0
        else:
            return secs_to_display_notfic
    elif time_now_h <= asr_h:
        next_pray += "اقتربت صلاةُ العَصر"
        secs_to_display_notfic = (((asr_h - time_now_h) * 60) + (asr_m - time_now_m)) * 60

        # Case of we passed the pray just for minutes Wait for this hour pass and return0 to call the func again
        if secs_to_display_notfic < 0:
            time.sleep((60 * 60) - (time_now_m * 60))
            return 0
        else:
            return secs_to_display_notfic
    elif time_now_h <= maghrib_h:
        next_pray += "اقتربت صلاةُ المغرِب"
        secs_to_display_notfic = (((maghrib_h - time_now_h) * 60) + (maghrib_m - time_now_m)) * 60

        # Case of we passed the pray just for minutes Wait for this hour pass and return0 to call the func again
        if secs_to_display_notfic < 0:
            time.sleep((60 * 60) - (time_now_m * 60))
            return 0
        else:
            return secs_to_display_notfic
    elif time_now_h <= isha_h:
        next_pray += "اقتربت صلاةُ العِشاء"
        secs_to_display_notfic = (((isha_h - time_now_h) * 60) + (isha_m - time_now_m)) * 60

        # Case of we passed the pray just for minutes Wait for this hour pass and return0 to call the func again
        if secs_to_display_notfic < 0:
            time.sleep((60 * 60) - (time_now_m * 60))
            return 0
        else:
            return secs_to_display_notfic

#Repeate the code foreever
while True:
        time.sleep(5)
        notification.notify(title="sdsd",
                            message="لو مصليتش سيب الي ف ايدك وقوم صلي ي بابااا",
                            app_name="Prayer Remainder By Osama",
                            app_icon="D:\Python\images\mosque_clock.ico",
                            timeout=10)

    # Call the prayer times api and get the data
    # response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Giza&country=Egypt&method=5")
    # data = response.json()
    #
    # # Get the exact time of prayers today
    # fajr = data['data']['timings']['Fajr']
    # dhuhr = data['data']['timings']['Dhuhr']
    # asr = data['data']['timings']['Asr']
    # maghrib = data['data']['timings']['Maghrib']
    # isha = data['data']['timings']['Isha']
    #
    # # Wait for the remaining seconds for the next pray
    # secs_to_display_notfic = get_remaining_secs_to_next_prayer(fajr, dhuhr, asr, maghrib, isha)
    # print(secs_to_display_notfic, next_pray)
    # if secs_to_display_notfic == 0:
    #     time.sleep(get_remaining_secs_to_next_prayer(fajr, dhuhr, asr, maghrib, isha) - notifc_time)
    #
    #     # Display the notification
    #     notification.notify(title=next_pray,
    #                         message="ثو مصليتش سيب الي ف ايدك وقوم صلي ي بابااا",
    #                         app_name="Prayer Remainder By Osama",
    #                         app_icon="D:\College\AI\images\mosque_clock.ico",
    #                         timeout=20)
    #     print("from If")
    # else:
    #     time.sleep(secs_to_display_notfic - notifc_time)
    #
    #     # Display the notification
    #     notification.notify(title=next_pray,
    #                         message="ثو مصليتش سيب الي ف ايدك وقوم صلي ي بابااا",
    #                         app_name="Prayer Remainder By Osama",
    #                         app_icon="D:\Python\images\mosque_clock.ico",
    #                         timeout=20)
    #     print("from Else")