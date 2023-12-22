# Using Puppet, create a file in /tmp.

file { 'school_file':
    ensure  => 'file',
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
