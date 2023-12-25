# config ssh via puppet 
$curr_user = $facts['id']
class { 'stdlib': }

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

exec { 'Restart SSH service':
  command     => 'sudo service ssh restart',
  refreshonly => true,
}
