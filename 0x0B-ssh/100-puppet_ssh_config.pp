# config ssh via puppet 

class { 'ssh':
  storeconfigs_enabled => false,
  client_options      => {
    'Host *' => {
      'Port'       => 22,
      'User'       => 'ubuntu',
      'HostName'   => '54.159.1.198',
      'IdentityFile' => '~/.ssh/school',
    },
  },
}

