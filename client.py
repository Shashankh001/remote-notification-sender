import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#defining a socket

IP = '192.168.0.102'#ip (to be changed accordingly)
PORT = 1234#must be the same on both the ends

notification = input("Enter your message: ")#input for notification
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

s.send(bytes(notification,'utf-8')) #send the notification details
print("Sent notification successfully!")
