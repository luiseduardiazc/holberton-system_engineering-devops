# Increase open files limit from 15 to 4096
exec { '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
