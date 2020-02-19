# Fix misconfiguration in Wordpress
exec { 'replace phpp':
    command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
exec {'restart apache':
  command => 'service apache2 restart'
}
