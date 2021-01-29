*** Settings ***
Resource        resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Documentation   A new user account can be created if a proper unused username and a proper password are given

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Input Text      username  kalle
    Input Password  password  kalle456
    Input Password  password_confirmation  kalle456
    Click Button    Register
    Welcome Page Should Be Open