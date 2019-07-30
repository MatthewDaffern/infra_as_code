import subprocess
from functools import partial, reduce



def CentOS_apache2_install(web_app_name, web_app_location, web_app_directories, config_location):
    install = ['yum','install', 'httpd','-y']
    systemctl_1 = ['systemctl', 'enable', 'httpd']
    systemctl_2 = ['systemctl', 'start', 'httpd']
    new_location = ('/var/www/' + example.com + web_app_directories)
    config_dir = ['mkdir', '-p', ('/var/www/' + example.com + web_app_directories)]
    copy_files = ['cp', web_app_location, new_location]
    change_permissions = ['chmod', '-R', '755', '/var/www']
    chown = ['chown', '-R', 'apache:apache', new_location ]
    httpd_config = ['cp', config_location, '/etc/httpd/conf/httpd.conf']
    command_list = [install, systemctl_1, systemctl_2, new_location, config_dir, copy_files, change_permissions, chown, httpd_config]
    add_semi_colon = list(map(lambda x: x.append(';'), command_list))
    single_list = reduce(lambda x,y: x + y, add_semi_colon)
    resultant_string = str.join(' ', single_list)
    return resultant_string
    

def server_install():
    return CentOS_apache2_install(example_name, example_location, example_directories, example_config)

def install_web_server(username, hostname, path_to_key_file, command):
    remote_command = ['ssh', username, '@', hostname, '-i', path_to_key_file, '<<', command]

def install_arbitrary_servers(hostname_range):
    server_partial=partial(install_web_server, username=input('what is the username?\n', ),
                                               path_to_key_file=input('where is your private key located?'),
                                               command=server_install())
    for i in hostname_range:
        server_partial(hostname=i)
    
