# Fix open file limit for holberton user

exec { 'change-os-configuration-for-holberton-user':
  command  => 'sed -i "/holberton hard/d" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}
