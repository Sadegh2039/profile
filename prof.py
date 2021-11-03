import pyrogram
from datetime import datetime
import schedule
import time
import pytz
import cv2

api_id = 7191310
api_hash = "82918c0b046ee88ca74f43b17b3e8cda"

app = pyrogram.Client("sadegh", api_id, api_hash)


def job():
    image = cv2.imread('./ddwd.png')

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (40, 600)
    fontScale = 3
    color = (255, 0, 0)
    thickness = 4
    matn = "TIME: " + \
           str(datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M"))
    image = cv2.putText(image, matn, org, font,
                        fontScale, color, thickness, cv2.LINE_AA)

    cv2.imwrite(f'./profile_temp.png', image)

    with app:
        app.set_profile_photo(photo=f'./profile_temp.png')
        me = app.get_me()
        print(app.get_profile_photos_count(me['id']))

        print("*/*/*/*/" * 100)
        print(str(datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")))
        try:
            try:
                app.delete_profile_photos(
                    app.get_profile_photos(me['id'])[1]["file_id"])
            except:
                print("except")
        except:
            print("except2")
        print("akhar")


schedule.every(4).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

app.run()
