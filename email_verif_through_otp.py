import getpass # to make the password hidden in asteriks
from environ import Env  # importing ENV class from environ module (helping us to access the env variables and manipulate them.)
import smtplib, ssl  # using the smtplib module to send otp via email
from email.mime.text import MIMEText  # using email.mime module to format the email
from email.mime.multipart import MIMEMultipart
import csv

def otp_gen():
    """
    This function Generates a truly random six digits password.
    :return: 6-Digit password
    """
    import secrets
    import string
    content = string.digits
    otp = ""
    for i in range(6):
        otp+=secrets.choice(content)
    return otp

def create_pass():
    """
    This function is used to create a password for the Your Use Case
    :return: Password
    """
    pass1 = getpass.getpass(prompt='Enter Password - ')
    pass2 = getpass.getpass(prompt='Re-Enter Password - ')
    if pass1 == pass2:
        return pass2
    else:
        print("Passwords didn't match!")
        retry = input('Press "R" to retry.')
        if retry == "R":
            create_pass()


def email_send_verify(__username):
    """
    This is the Main function used to verify your email and generate a password for it.
    :param __username: Your Email ID which you wish to verify.
    :return: Stores your Email and Created Password in a user_data.csv file
    """
    message = MIMEMultipart()
    message["Subject"] = "OTP for Verification"
    otp = otp_gen() # calling the otp_gen function
    message.attach(MIMEText(f"The One Time Password for your email verification is {otp}"))

    env = Env() # creating an instance of Env class
    env.read_env(env_file=".env") # locating the .env file

    context = ssl.create_default_context()
    outgoing_address = "smtp.gmail.com"
    port = 465

    try:
        connection = smtplib.SMTP_SSL(host=outgoing_address, port=port, context=context)
        connection.login(user = env('SENDER'), password = env('PASSWORD'))
        connection.sendmail(from_addr = env("SENDER"), to_addrs = __username, msg = message.as_string())
        connection.quit()
        print("OTP has been Sent Successfully.")

    except Exception as e:
        print(f'Error - {e}',"Make sure the Email and password are correct.",sep='\n')

    else:
        otp_received = getpass.getpass(prompt='Enter OTP - ')
        if otp_received == otp:
            print('Your Email has been successfully verified.')
            with open('user_data.csv','a') as file:
                fieldnames = ['Email','Password']
                writer = csv.DictWriter(file,delimiter=',',lineterminator='\n',quotechar='"',fieldnames=fieldnames)
                writer.writeheader()
                i = input('Press C to create a password - ')
                if i == 'C':
                    writer.writerow({"Email":__username,"Password":create_pass()})
                    print('Password set successfully.')
                else:
                    writer.writerow({"Email": __username, "Password":"Nil"})


username = input('Enter email - ')
email_send_verify(username)