# config ssh via puppet 
$curr_user = $facts['id']
class { 'stdlib': }

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => "/home/${curr_user}/.ssh/config",
  line  => "IdentityFile /home/${curr_user}/.ssh/school",
  match => '^#?IdentityFile',
}

exec { 'Restart SSH service':
  command     => 'sudo service ssh restart',
  refreshonly => true,
}
