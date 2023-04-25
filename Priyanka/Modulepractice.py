import pywhatkit
import time
import datetime
# Send a WhatsApp Message to a Contact at 1:30 PM

contact_list = [{"name":"Swathi","mob_no":"6309466788"},{"name":"Cherry","mob_no":"7780618989"},{"name":"Kalyan","mob_no":"8106646699"}]
while True:

    starttime = datetime.datetime.now()
    print(starttime.hour,starttime.minute)
    for contact in contact_list:
        pywhatkit.sendwhatmsg("+91" + contact['mob_no'], "Hi "+ contact['name']  +"\n Wake up, class will start @9.15PM", starttime.hour, starttime.minute+1)
        
    time.sleep(60)
    