import ftplib

host = "192.168.178.22"
username = "testuser"
password = "testuser"

ftp_server = ftplib.FTP(host, username, password)
 
ftp_server.encoding = "utf-8"

print(ftp_server.getwelcome())

ftp_server.dir()

ftp_server.quit()