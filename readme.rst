tradesocket
============

The point of "tradesocket" is to be able to create a socket in one process and
then send it over to be used by another process. The primary use-case is when
you have a server that starts off running as root and then drops down into
another user but still wants to create special sockets like those using port
80. You have the process fork before it drops into its user, and now the user
process will request the root process for sockets which can then be sent using
tradesocket.

See "tests/test_tradesocket.py" for an example of this.


The module exposes two functions:

    ``tradesocket.send_fd( fd_a, fd_b )``::
        
        Send a file descriptor ``fd_b`` over the file-descriptor ``fd_a``.
        
        Returns the number of characters sent over the socket or -1 if failed.
    
    ``tradesocket.recv_fd( fd )``::
    
        Recieve a file descriptor over the file-descriptor ``fd``.
    
        Returns the recieved file-descriptor or a negative value if failed.
    

Example
------------

Before forking::

    server_unix_sock, client_unix_sock = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM, 0)
    
    ... fork

Server::
    
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(5000)
    tradesocket.send_fd( server_unix_sock.fileno(), sock.fileno())


Client::

    fd = tradesocket.recv_fd(self._unix_socket.fileno())
    if fd < 0:
        raise RuntimeError("Socket trading failed.")
    sock = socket.fromfd( fd, socket.AF_INET, socket.SOCK_STREAM )
