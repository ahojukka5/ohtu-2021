*** Settings ***
Resource        resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Documentation   A new user account can be created if a proper unused username and a proper password are given

*** Test Cases ***

Register With Valid Username And Password
    Register  kalle  kalle456  kalle456
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register  ka  kalle456  kalle456
    Page Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Register  kalle  kalle  kalle
    Page Should Contain  Password is too short

Register With Nonmatching Password And Password Confirmation
    Register  kalle  kalle123  kalle234
    Page Should Contain  Password confirmation failed

Login After Successful Registration
    Register         jukka  jukka123  jukka123
    Go To Login Page
    Input Text       username  jukka
    Input Password   password  jukka123
    Click Button     Login
    Main Page Should Be Open

*** Keywords ***

Register
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Go To Register Page
    Input Text      username  ${username}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}
    Click Button    Register
