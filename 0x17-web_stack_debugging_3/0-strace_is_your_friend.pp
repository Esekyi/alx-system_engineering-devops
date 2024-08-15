# Puppet manifest to fix Apache 500 (server) error

# making sure the neccessary configuration file exists
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache/000-default.conf',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['apache2'],
}
# if the conf exists, make sure it runs
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf'],
}
# correct permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
  require => Package['apache2'],
}

package { 'apache2':
  ensure => installed,
}

package { ['php', 'php-mysql', 'libapache2-mod-php']:
  ensure  => installed,
  require => Package['apache2'],
}

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['apache2'],
}

service { 'mysql':
  ensure  => running,
  enable  => true,
  require => Package['mysql-server'],
}

package { 'mysql-server':
  ensure => installed,
}
