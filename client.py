import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '192.168.0.102'
PORT = 1234

notification = input("Enter your message: ")
print("")


if notification == "":
    print("Cant send an empty message!")
    print("")
    quit()


try:
    s.connect((IP,PORT))
except:
    print("Hmm, looks like the receiver is offline. Try again later.")
    quit()

s.send(bytes(notification,'utf-8'))
print("Sent notification successfully!")