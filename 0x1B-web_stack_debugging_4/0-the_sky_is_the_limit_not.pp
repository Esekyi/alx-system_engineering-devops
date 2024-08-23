# This Puppet manifest configures Nginx and Gunicorn for optimal performance
# and to minimize the number of failed requests under high load.

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

-> service { 'nginx':
  ensure => 'running',
}

exec { 'nginx-restart':
  command     => 'nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
  subscribe   => Exec['fix--for-nginx'],
}
