# Using Puppet, create a file in /tmp.

file { '/tmp/school':
    owner   => 'www-data',
    mode    => '0744',
    group   => 'www-data',
    content => 'I love Puppet',
}
