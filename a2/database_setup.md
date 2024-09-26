1) make port 6002 available via TCP in AWS console
2) sudo apt install mariadb-server -y
3) sudo vi /etc/mysql/mariadb.conf.d/50-server.cnf, add port = 6002 in the document, set bind-address = 0.0.0.0
4) sudo systemctl restart mariadb, start the database
5) sudo mysql_secure_installation, install mysql
6) sudo mysql -u root -p, run mysql
7) CREATE DATABASE comp370_test;
	CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
	GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';
	create username and password, give privilege

8) Test if we can connected, worked for me.