# Using Puppet, create a school file in /tmp.
file { '/tmp/school':
  owner => 'www-data',
  mode => '0774',
  group => 'www-data',
  content => 'I love Puppet',
}

