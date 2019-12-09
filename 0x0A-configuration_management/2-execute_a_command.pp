exec { 'killmenow':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  command  => 'pkill killmenow',
}
