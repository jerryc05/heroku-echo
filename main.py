#!/usr/bin/env python3

import os
import socket

def main():
  HOST = '0.0.0.0'
  PORT = int(os.environ.get('PORT', 17995))

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print('Connected from:', addr)
          conn.sendall(b'Connected from: ' + str(addr).encode())
          while True:
              data = conn.recv(1024)
              if not data:
                  break
              print('Connected from:', addr, end='')
              conn.sendall(data)
  
if __name__ == '__main__':
  main()
