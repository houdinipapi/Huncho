# Using Puppet, create a manifest that kills a process named killmenow.
# Requirements:
  # Must use the exec Puppet resource
  # Must use pkill

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  onlyif      => 'pgrep -f killmenow',
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
  provider    => shell,
}
