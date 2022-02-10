# NS

# Task 2

I tried to use selenium with chrome browser on MacOs, but chrome keep chrasing when tried to open the browser. Also tried to find dolution online but didn't work. so i decided to write down pseudo code of Task-2.


So steps that i would follow for task 2 will be:

1. Open link in the brower and then find reCaptcha frame and click on it to .(using selenium)
2. After reCaptcha is opened then click on headphone icon (click on audio challenge)
3. get the mp3 audio file using find_element_by_id and download it.
4. translate audio to text with google voice recognition (using speech_recognition library)
5. send result to step 4 with help of send_keys to repective reCaptcha frame.
6. click on submit using click()
7. Auto fill URL field using send_keys.
8. CLick on Submit Report using click()
