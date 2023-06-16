# Email Verification Through OTP

---

This script lets you verify your email by sending an OTP.

## IMPORTANT -
### Execute the script in Terminal and not in any IDE
1. This Script uses Google Outgoing Mail Server. Hence your email id must be a Gmail-ID.
2. The Email from which sends you the OTP must have 2-factor-authentication setup and created an App password.
3. Use that Email and Password here :-
   #### connection.login(user = ________, password = ______)
4. The Email which you wish to verify goes here :-
   #### connection.sendmail(.... to_addrs = _______, ...)
5. After the OTP has been verified, You could generate a password for test purpose.
6. The Email and generated password will be stored in a user_data.csv file.