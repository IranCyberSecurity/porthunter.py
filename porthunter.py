import socket, select, sys

Banner = '''
    #####################################################
    #                 ICG PorT HuntEr                   #
    #                WwW.IraN-Cyber.NeT                 #
    #                 White Hat Hacker                  #
    #  Real Hackers Make security, Not Kill Security !  #
    #####################################################
'''

print Banner

Send_data = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length:'
__Deface = "<center><H1>ICG 4 EVER</H1></center>"

__sessSocket = socket.socket()
print '  [*] Socket ---> Ok'
try:
    __sessSocket.bind(('',1337))
except socket.error:
    print '  [-] Socket Bind ---> No'
    sys.exit()
print '  [*] Socket bind ---> Ok'
__sessSocket.listen(10)
__client = []
print '  [+] port Listened : ) <3 '
while True:
    _list, _list2, _list3 = select.select([__sessSocket] + __client, __client, [])

    for __SoCket in _list:
        if __SoCket is __sessSocket:
            _sessSocketNew, addr = __sessSocket.accept()
            __client.append(_sessSocketNew)
        else:
            __Socket_recv_Data = __SoCket.recv(1024)
            if __Socket_recv_Data == "":
                __client.remove(__SoCket)
            else:
                __SoCket.send(Send_data + str(len(__Deface)) + "\r\n\r\n" + __Deface)
