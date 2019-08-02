$file_location = out-host 'please enter the file location of your user list'
$Users = Import-CSV $file_location


function chr_gen{
    $chr = ([char](get-random -max 128))
    return $chr
}


foreach ($item in $Users) {
    $Username= $item.Username
    $password = ''
    1..15 | chr_gen >> $password
    New-ADUser
    -UserPrincipalName $item.email `
    -SamAccountName $item.Username `
    -UserPrincipalName "$Username@yourdomain.com" `
    -Name "$item.Firstname $item.Lastname" `
    -GivenName $item.Firstname `
    -Surname $item.Lastname `
    -Enabled $True `
    -ChangePasswordAtLogon $True `
    -DisplayName "$item.Lastname, $item.Firstname" `
    -Department $Department `
    -Path $OU `
    -AccountPassowrd (convertto-securestring $password -AsPlainText -Force)
    
}