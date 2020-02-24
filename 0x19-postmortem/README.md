# Postmortem Report

![](https://media.makeameme.org/created/post-mortem-meetings.jpg)


| Timeline   | Description                                                  |
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