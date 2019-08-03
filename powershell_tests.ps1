$file_location = out-host 'please enter the file location of your user list'
$Users = Import-CSV $file_location

# need to convert this all to functions. 

function chr_gen{
    $chr = ([char](get-random -max 128))
    return $chr
}

function password_creator($length, $chr_randomizer){
    $password = $null
    1.. $length | & $chr_randomizer >> $password
    return $password
}


function map($function, $iterable){
    $old_iterable = $iterable
    $new_iterable = @()
    foreach ($item in $old_iterable){   
        & $function($item) >> $new_iterable
    }
    return $new_iterable
}


#setting functions as variables requires scoping the variable to be a function.
#$foo1 = $function:foo
#then it's called with &

function create_user($user){
    #$user should have every parameter available as an attribute

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
    -AccountPassword (convertto-securestring $password -AsPlainText -Force)
    
}