# Using Puppet, create a file in /tmp.

file { '/tmp/school'
  ensure => file,
  mode => '0774'
  owner => 'www.data',
  group => 'www-data',
  content => 'I love Puppet'
}

