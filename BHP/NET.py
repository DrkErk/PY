# based on chap 2 pages 32-34

#
# TCP CLIENT
#
def tcpClient():
    import socket

    target_host = "www.google.com"
    target_port = 80

    #creating the socket (1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create the connection (2)
    client.connect((target_host, target_port))
    # sending a get request to google (3)
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    # response/receive data (4)
    response = client.recv(4096)

    print(response.decode())
    client.close()

    #(1) AF_INET is a IPv4 Address/hostname and SOCK_STREAM is a TCP client
    #(2) connect to ther server
    #(3) send the header data out
    #(4) receive data and set it to a cmlOut and close with client.close










































