# find out error and fix it 

exec {'fix-line':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => ['/bin','/usr/bin']
}
