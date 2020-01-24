'''
module for install and uninstall mysql
and run task for make db replication

use:
fab -f task_install.py function_to_execute

exp:
fab -f task_install.py install_mysql

by: Luis Eduardo Diaz
'''
from fabric.api import env, hosts,  run, put

env.hosts.extend(['35.229.36.131', '34.74.68.170'])
env.user = 'ubuntu'


def uninstall_mysql():
    '''
    Uninstall mysql
    '''
    run('sudo apt-get remove --purge mysql-server mysql-client mysql-common -y')
    run('sudo apt-get autoremove -y')
    run('sudo apt-get autoclean')
    run('sudo rm -rf /etc/mysql')
    run("sudo find / -iname 'mysql*' -exec rm -rf {} \;")


def install_mysql():
    '''
    install mysql
    '''
    run('sudo apt-get install mysql-server mysql-client -y')
    run('mysql --version')


def create_user_replication():
    '''
    run script for create user holberton_user
    '''
    put('create_user_replication.sql', '/home/ubuntu/')
    run('cat create_user_replication.sql | mysql -hlocalhost -uroot -proot')


@hosts('35.229.36.131')
def create_table():
    '''
    run script for create database tyrell_corp
    '''
    put('create_database.sql', '/home/ubuntu/')
    run('cat create_database.sql | mysql -hlocalhost -uroot -proot')


@hosts('35.229.36.131')
def create_primary_replica_user():
    '''
    run script for create user replica_user
    '''
    put('replica_user.sql', '/home/ubuntu/')
    run('cat replica_user.sql | mysql -hlocalhost -uroot -proot')


def allow_port_mysql():
    '''
    allow port 3306
    '''
    run('sudo ufw allow 3306')
    run('sudo service ufw restart')


@hosts('35.229.36.131')
def show_master_status():
    '''
    check master status
    '''
    run('echo "show master status;" | mysql -hlocalhost -uholberton_user -pprojectcorrection280hbtn')


@hosts('34.74.68.170')
def show_slave_status():
    '''
    check slave status
    '''
    run('echo "show slave status\G;" | mysql -hlocalhost -uholberton_user -pprojectcorrection280hbtn')


@hosts('35.229.36.131')
def up_script_backup():
    '''
    up script for make backups
    '''
    put('5-mysql_backup', '/home/ubuntu', mode='0775')
