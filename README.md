# 3-tier-door-lock-security-system

# The system will provide a 3-level access control security.
 Facial Recognition.
 Password entry(provision to reset password is also present).
 One time password verification.

Note: for reseting the whole project delete all entries in entry_log and personal_data and remove all folders in level_1 and level_2.

# Algorithm

Algorithm for creating datasets:
 Start.
 Import all the required libraries like cv2, os, and openpyxl.
 Take name, password email and clearance level from the user and store it in n, p, e, m respectively.
 If m = 1, open directory level_1 and if m = 2 then directory level_2 is opened.
 Open the camera.
 Choose the desired dimensions of the dataset images.
 Using the haar cascade, the face of the user would be detected and 100 pictures would be stored in a new directory with the user’s name to be used as the dataset.
 Open the excel file personal_data and store the user's password and email in the bottom-most row.
 Save and close the excel file.
 Keep the provision to close the camera by pressing the ESC key.
 Stop.

Algorithm for hanging the password:
 Start.
 Load the excel file personal_data.
 Take the name and the current password from the user.
 If the password is correct ask for the updated password.
 Replace the old password with the updated one in the excel file, save it and close it.
 Stop.

Algorithm for access control:
 Start.
 Import all the required libraries like smtplib, random, datetime, cv2, numpy, os, pytz, and openpyxl.
 Create two variables c1 and c2 and store the number 0 in both of them.
 Load the excel files personal_data and entry_log.
 Open the camera.
 Detect any face using the haar cascade.
 Compare the detected face from the datasets available in the directories level_1 and level_2.
 If the faces are similar, then it is a match.
 Find the name and level of the dataset directory similar to the detected face.
 Using the now function of the datetime library, get the current time.
 Request the user to provide their password.
 Compare the entered password to the one in the excel file.
 If it is a match then go to step 16.
 If it is not a match, increment the counter c1 by 1 and let the user try again. 
 If c1 = 3, then print access denied and go to step 25
 Then generate a random 4-digit OTP using the randint function of the random library and send it to the user via email.
 After that request the user to provide their OTP.
 Compare the entered OTP to the one sent.
 If it is a match then go to step 22.
 If it is not a match, increment the counter c2 by 1 and let the user try again. 
 If c2 = 3, then print access denied and go to step 25
 Print access granted.
 Enter the name, date, and time of the user's entry to the bottom-most row of the entry_log excel file.
 Save and close the entry_log file.
 Stop.

# Results

The Facial Recognition Algorithm has been implemented successfully with an accuracy of 70%.
The Raspberry Pi will stream the video feed from the camera to the laptop.
The laptop will run the Facial Recognition Algorithm on the video stream and create a CSV file of the personnel.
The CSV file will be updated every time there is an entry
The Numeric Keypad is also been programmed and implemented for the personnel to enter the passcode.
