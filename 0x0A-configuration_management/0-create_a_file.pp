file { '/tmp/school':
  owner => 'www-data',
	mode => '0744',
	group => 'www-data',
	content => 'I love Puppet'
}
