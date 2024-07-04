# execute a command that kills a process named killmenow using pkill
exec { 'kill_killmenow':
  command => 'pkill -9 killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}
