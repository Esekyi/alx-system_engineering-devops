# Puppet manifest to fix Apache 500 (server) error

exec { 'wP_conf_phpp_to_php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
