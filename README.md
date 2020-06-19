# 3-tier-door-lock-security-system
# The system will provide a 3-level access control security.
1. Facial Recognition.
2. Password entry(provision to reset password is also present).
3. One time password verification.

Note: for reseting the whole project delete all entries in entry_log and personal_data and remove all folders in level_1 and level_2.

Algorithm 

Algorithm for creating datasets
1. Start.
2. Import all the required libraries like cv2, os, and openpyxl.
3. Take name, password email and clearance level from the user and store it in n, p, e, m respectively.
4. If m = 1, open directory level_1 and if m = 2 then directory level_2 is opened.
5. Open the camera.
6. Choose the desired dimensions of the dataset images.
7. Using the haar cascade, the face of the user would be detected and 100 pictures would be stored in a new directory with the user’s name to be used as the dataset.
8. Open the excel file personal_data and store the user's password and email in the bottom-most row.
9. Save and close the excel file.
10. Keep the provision to close the camera by pressing the ESC key.
11. Stop.

Algorithm for hanging the password
1. Start.
2. Load the excel file personal_data.
3. Take the name and the current password from the user.
4. If the password is correct ask for the updated password.
5. Replace the old password with the updated one in the excel file, save it and close it.
6. Stop.

Algorithm for access control
1. Start.
2. Import all the required libraries like smtplib, random, datetime, cv2, numpy, os, pytz, and openpyxl.
3. Create two variables c1 and c2 and store the number 0 in both of them.
4. Load the excel files personal_data and entry_log.
5. Open the camera.
6. Detect any face using the haar cascade.
7. Compare the detected face from the datasets available in the directories level_1 and level_2.
8. If the faces are similar, then it is a match.
9. Find the name and level of the dataset directory similar to the detected face.
10. Using the now function of the datetime library, get the current time.
11. Request the user to provide their password.
12. Compare the entered password to the one in the excel file.
13. If it is a match then go to step 16.
14. If it is not a match, increment the counter c1 by 1 and let the user try again. 
15. If c1 = 3, then print access denied and go to step 25
16. Then generate a random 4-digit OTP using the randint function of the random library and send it to the user via email.
17. After that request the user to provide their OTP.
18. Compare the entered OTP to the one sent.
19. If it is a match then go to step 22.
20. If it is not a match, increment the counter c2 by 1 and let the user try again. 
21. If c2 = 3, then print access denied and go to step 25
22. Print access granted.
23. Enter the name, date, and time of the user's entry to the bottom-most row of the entry_log excel file.
24. Save and close the entry_log file.
25. Stop.
# Results

The Facial Recognition Algorithm has been implemented successfully with an accuracy of 70%.
The Raspberry Pi will stream the video feed from the camera to the laptop.
The laptop will run the Facial Recognition Algorithm on the video stream and create a CSV file of the personnel.
The CSV file will be updated every time there is an entry
The Numeric Keypad is also been programmed and implemented for the personnel to enter the passcode.
