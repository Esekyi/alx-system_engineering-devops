# puppet file to install nginx web server 301 moved permanently

class nginx {
    package { 'nginx':
        ensure => installed
    }
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx']
}
