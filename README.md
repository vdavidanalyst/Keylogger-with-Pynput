# Project Title: Keylogger with Encryption
# Project Overview:
The Keylogger with Encryption project demonstrates how to create a keylogger using the Pynput library in Python. It captures keyboard inputs, encrypts them using the Fernet encryption algorithm, and logs them into a file. The encrypted keystrokes are also decrypted and displayed in the console.

# Aims:
- Develop a keylogger using the Pynput library in Python.
- Capture and log keyboard inputs, including alphanumeric characters, space, enter, and tab keys.
- Handle special characters and log them appropriately.
- Encrypt the captured keystrokes using the Fernet encryption algorithm.
- Implement email capabilities to send the captured keystrokes to a specified email address.
- Demonstrate the functionality of a basic keylogger with email integration.

# Objectives:
- Acquire proficiency in using the Pynput library for keyboard input monitoring.
- Understand and implement logging functionality to store the captured keystrokes in a log file.
- Handle different types of keys, including alphanumeric characters, space, enter, and tab keys.
- Encrypt the captured keystrokes to ensure data privacy and security.Configure email settings to send the encrypted keystrokes as an email.
- Ensure proper documentation and code organization for the project.
- Practice responsible use of keylogging techniques and emphasize the importance of obtaining proper authorization when implementing such functionality.
- Showcase the ability to combine multiple libraries and technologies to create a functional and secure keylogger with email capabilities.

# Technologies Used:
  Python
  Pynput library
  Logging module
  Cryptography library

# Features:
- Capture and log alphanumeric characters, space, enter, and tab keys.
- Handle special characters and log them appropriately.
- Encrypt the captured keystrokes using the Fernet encryption algorithm.
- Decrypt and display the keystrokes in the console.
- Store the encrypted keystrokes in a log file.
- Basic error handling for logging and key press events.

# Project Structure:
  keylogger.py: The main script that implements the keylogger functionality with encryption and decryption.

# Instructions:
- Install the required libraries: pip install pynput cryptography
- Run the script: python keylogger.py
The keylogger will start capturing keyboard inputs. The captured keystrokes will be encrypted, logged into the specified log file (C:\ProgramData\mylog.txt), and displayed in the console after decryption.
- Use Ctrl+C to stop the keylogger.

# Notes:
- Use this keylogger responsibly and only on your own devices or with proper authorization from the users involved.
- Ensure that you have the necessary permissions to access and modify the log file path specified in the script.
- Customize the script as per your requirements, such as modifying the log file path or extending the functionality.
- Keep the encryption key (b'I9qf4guuRucF1qdxok8s3tJ5lV+GzrYXjL7pCeBnvwQ=') secure and avoid hard-coding it in the code. Generate a new key using Fernet.generate_key() for added security.
- You might need to temporarily disable antivirus protection to run your scripts.

# Conclusion:
- The Keylogger with Encryption project showcases the implementation of a keylogger in Python using the Pynput library. By incorporating encryption and decryption functionality, it ensures that the captured keystrokes remain secure and protected from unauthorized access. This project serves as a foundation for understanding keylogging techniques, encryption algorithms, and basic file logging.

- With the modifications, the [keylogger_extended](https://github.com/vdavidanalyst/Keylogger-with-Pynput/blob/main/keylogger_extended.ipynb) will send an email with the captured keystrokes when the Enter key is pressed. The keystrokes will also be logged into the specified log file (C:\ProgramData\mylog.txt).

  Please note that using a Gmail account for sending emails may require enabling access for less secure apps or generating an app password. Ensure that you have the necessary permissions and follow the email service provider's guidelines to successfully send emails from your script.

  Regarding persistence and autostart, the implementation may vary depending on the operating system you're using. Here are some general guidelines:
Windows: You can create a shortcut to the Python script and place it in the "Startup" folder. This will make the script run automatically when the user logs in. The "Startup" folder can be accessed by pressing Win+R, entering shell:startup, and pressing Enter.

  Feel free to adjust the email subject, body, or add more content to the email as needed. Remember to handle any potential security considerations and use this functionality responsibly.
