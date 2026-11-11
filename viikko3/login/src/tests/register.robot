*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  seppo
    Set Password  seppo123
    Set Password Confirmation  seppo123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  seppo2
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  seppo5
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Non-Matching Password Confirmation
    Set Username  seppo6
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  matti123
    Set Password Confirmation  matti123
    Click  button >> text=Register
    Register Should Fail With Message  Username must have atleast 3 characters

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  matti1
    Set Password Confirmation  matti1
    Click  button >> text=Register
    Register Should Fail With Message  Password must have atleast 8 characters

Register With Password Containing Only Lowercase Letters
    Set Username  seppo3
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or special character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  seppo4
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or special character

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Username already in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page