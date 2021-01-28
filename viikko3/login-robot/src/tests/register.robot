*** Settings ***
Resource       resource.robot
Documentation  A new user account can be created if a proper unused username and a proper password

*** Test Cases ***
Register With Valid Username And Password
    Create User        kalle  kalle123
    User Should Exist  kalle
