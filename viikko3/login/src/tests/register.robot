*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  seppo
    Set Password  seppo123
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  matti123
    Click  button >> text=Register
    Register Should Fail With Message  Username must have atleast 3 characters

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  matti1
    Click  button >> text=Register
    Register Should Fail With Message  Password must have atleast 8 characters

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
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