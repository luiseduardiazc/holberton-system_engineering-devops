# Postmortem Report

![](https://media.makeameme.org/created/post-mortem-meetings.jpg)

### Summary
After deploy new features, the server access went down resulting in 500 error for anyone trying to access a website.
The last deploy was at middle night. 02-18-2020

### Timeline

| Time   | Description                                                  |
|------------|--------------------------------------------------------------|
| 09:00 COT  | 500 error for anyone trying to access the website was report |
| 09:05 COT  | Check server logs                                            |
| 09: 10 COT | Check database conection                                     |
| 09: 12 COT | Run  strace comand                                           |
| 09: 20 COT | Identified  wrong configuration in wp\-config\.php file      |
| 09:21 COT  | wp\-config\.php have a \.phpp extension into config files    |
| 09:22 COT  | Write puppet script for replace \.phpp extension to \.php    |
| 09:30 COT  | Run puppet script                                            |
| 09:31 COT  | Restart apache2                                              |
| 09: 32 COT | Test url access through curl                                 |
| 09: 33 COT | Url result 200 OK                                            |

### Root Cause Analysis
The server being based on a LAMP stack.
wp-config.php is one of the core WordPress files. It contains information about the database, including the name, host (typically localhost), username, and password. This information allows WordPress to communicate with the database to store and retrieve data (e.g. Posts, Users, Settings, etc). The file is also used to define advanced options for WordPress.
Our team added an advanced configuration on this file for include path to others .php files but some extension of files was wrong and we deploy this features to web server without tests.


### Incident Actions
Once the error was reported we review the database conexion, the server status and the application status.
we used a strace command for test apache2 and curl for retrieve url
we identified wrong extensions in wp-config.php. We wrote the below script for fix it.

```sh
# Fix misconfiguration in Wordpress
exec { 'replace phpp':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
exec {'restart apache':
  command => '/usr/sbin/service apache2 restart'
}
```

### Corrective and Preventive Measures

- All servers and sites should be tested locally before deploying on a multi-server setup this will result in correcting errors before going live resulting in less fixing time if site goes down.