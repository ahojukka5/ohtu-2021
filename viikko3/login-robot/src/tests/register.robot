*** Settings ***
Resource       resource.robot
Documentation  A new user account can be created if a proper unused username and a proper password

*** Test Cases ***
Register With Valid Username And Password
    Create User        kalle  kalle123
    User Should Exist  kalle

Register With Already Taken Username And Valid Password
    Create User             kalle  kalle123
    Create User             kalle  kalle123
    Output Should Contain   User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User             ka     kalle123
    Output Should Contain   Username is too short
