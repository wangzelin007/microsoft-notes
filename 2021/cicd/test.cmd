@echo on

:: set TEST_DIR="C:\Program Files (x86)"
::
:: if exist %TEST_DIR% (
::     echo SUCCESS.
::     goto END
:: ) else (
::     echo FAILED.
::     goto ERROR
:: )

where python || goto ERROR
where curl || goto ERROR
where unzip || goto ERROR
where msbuild || goto ERROR
where aaa || goto ERROR

if %errorlevel% neq 0 goto ERROR

:ERROR
echo Error occurred, please check the output for details.
exit /b 1

:END
exit /b 0
popd
