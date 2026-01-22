@echo off
call venv_captcha\Scripts\activate
python captcha_solver.py https://www.google.com/recaptcha/api2/demo
pause
