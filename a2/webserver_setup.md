1) on the aws account make the lightsail server be able to listen to port 8008 using TCP
2) login to server
3) sudo apt install apache2 -y
4) sudo vi /etc/apache2/ports.conf, make default port 8008
5) sudo vi /etc/apache2/sites-available/000-default.conf, make default port 8008
6) sudo vi /var/www/html/comp370_hw2.txt, create the text file
7) sudo systemctl restart apache2, start apache
8) http://3.96.159.115:8008/comp370_hw2.txt, this link work