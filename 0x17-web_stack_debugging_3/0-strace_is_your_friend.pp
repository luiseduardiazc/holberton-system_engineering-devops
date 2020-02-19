# Fix misconfiguration in Wordpress
exec { 'replace phpp':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
exec {'restart apache':
  command => '/usr/sbin/service apache2 restart'
}
