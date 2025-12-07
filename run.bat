@echo off

@REM Examples:
@REM run 04 a
@REM run 07 b
@REM run 08 test
@REM run all test
@REM run mypy


setlocal

set first=%1
set second=%2

set mypy_command=mypy . --no-incremental

if %first%==mypy (
    echo %mypy_command%
    call %mypy_command%
    goto :eof
)

set number=%first%
set command=%second%

if %command%==a (
    call :script_a
    goto :eof
)

if %command%==b (
    call :script_b
    goto :eof
)

if %command%==test (
    if %number%==all (
        call cls && uv run pytest .
        goto :eof
    )
    call uv run pytest src/days/day%number%
    goto :eof
)

goto :eof

:script_a
    set script=src.days.day%number%.a
    call uv run python -m %script%
    exit /b

:script_b
    set script=src.days.day%number%.b
    call uv run python -m %script%
    exit /b

:eof
