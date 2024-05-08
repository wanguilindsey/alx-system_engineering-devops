#Using strace  and Puppet to automate fix for 500 error on Apache

exec { 'fix_typo':
  path        => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command     => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  onlyif      => 'test -f /var/www/html/wp-settings.php',  # Check if file exists
  refreshonly => true,  # Only run when triggered
  provider    => 'shell',
  logoutput   => true,  # Log output of the command
  unless      => "grep -q '.phpp' /var/www/html/wp-settings.php || ! test -f /var/www/html/wp-settings.php",  # Ensure idempotency
}
