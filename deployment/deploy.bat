@echo off
REM Deploy services using Docker Compose

REM Combine Docker Compose files and build the services
docker compose -f docker-compose.yml ^
               -f ..\infra\api-gateway\docker-compose.yml ^
               -f ..\services\iam-service\docker-compose.yml ^
               -f ..\services\media-service\docker-compose.yml ^
               -f ..\services\ocr-service\docker-compose.yml ^
               up -d --build

REM Check the exit code of the last command and print result
if %ERRORLEVEL% EQU 0 (
    echo Deployment succeeded.
) else (
    echo Deployment failed with error code %ERRORLEVEL%.
)

REM Wait for user input before closing
echo.
echo Press any key to exit...
pause >nul
