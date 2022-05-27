import ftplib

host = "192.168.178.22"
username = "testuser"
password = "testuser"

ftp_server = ftplib.FTP(host, username, password)
 
ftp_server.encoding = "utf-8"

filename = "test2.txt"

with open(filename, "rb") as file:
    ftp_server.storbinary(f"STOR {filename}", file)

ftp_server.quit()