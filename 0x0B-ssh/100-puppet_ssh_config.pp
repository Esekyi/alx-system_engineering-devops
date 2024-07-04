# puppet configuration file for ssh so that password authentication would be disabled
file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'ssh_config':
  path => '/etc/ssh/ssh_config',
  line => '  PasswordAuthentication no',
}
file_line { 'configure using private key for ssh':
  path => '/etc/ssh/ssh_config',
  line => '  IdentityFile ~/.ssh/school',
}
