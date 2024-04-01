#!/bin/dash

echo "Creando BD finvero"
systemctl start mysql
systemctl enable mysql

/usr/bin/mysql -u root -p < db_config.sql

source finveroapi-env/bin/activate