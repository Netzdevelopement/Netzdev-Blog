import ftplib

host = "192.168.178.22"
username = "testuser"
password = "testuser"

ftp_server = ftplib.FTP(host, username, password)
 
ftp_server.encoding = "utf-8"

filename = "test.txt"

with open(filename, "wb") as file:
    ftp_server.retrbinary(f"RETR {filename}", file.write)

ftp_server.dir()
 
file= open(filename, "r")
print('File Content:', file.read())

ftp_server.quit()