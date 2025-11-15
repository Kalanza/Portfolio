@echo off
echo ================================
echo Django Portfolio - Setup Script
echo ================================
echo.

echo Creating superuser for admin panel...
echo.
python manage.py createsuperuser

echo.
echo ================================
echo Setup complete!
echo ================================
echo.
echo Your portfolio is ready!
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   Portfolio: http://127.0.0.1:8000/
echo   Admin: http://127.0.0.1:8000/admin/
echo.
pause
