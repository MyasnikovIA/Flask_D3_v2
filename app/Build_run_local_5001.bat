rem  создаем виртуальную среду
python -m venv env
rem активируем виртуальную среду
env\Scripts\activate.bat &&

rem подгружаем библиотеки для виртуальной среды
   pip install pkg/window/colorama-0.4.4-py2.py3-none-any.whl
   pip install pkg/window/importlib_metadata-4.9.0-py3-none-any.whl
   pip install pkg/window/typing_extensions-4.0.1-py3-none-any.whl
   pip install pkg/window/Werkzeug-2.0.2-py3-none-any.whl
   pip install pkg/window/zipp-3.6.0-py3-none-any.whl
   pip install pkg/window/requests-2.26.0-py2.py3-none-any.whl
   pip install pkg/window/six-1.16.0-py2.py3-none-any.whl
   pip install pkg/window/pandas-1.3.5-cp37-cp37m-win_amd64.whl
   pip install pkg/window/psycopg2_binary-2.9.2-cp37-cp37m-win_amd64.whl
   pip install pkg/window/python_dateutil-2.8.2-py2.py3-none-any.whl
   pip install pkg/window/pytz-2021.3-py2.py3-none-any.whl
   pip install pkg/window/numpy-1.21.4-cp37-cp37m-win_amd64.whl
   pip install pkg/window/Flask-2.0.2-py3-none-any.whl
   pip install pkg/window/idna-3.3-py3-none-any.whl
   pip install pkg/window/itsdangerous-2.0.1-py3-none-any.whl
   pip install pkg/window/Jinja2-3.0.3-py3-none-any.whl
   pip install pkg/window/MarkupSafe-2.0.1-cp37-cp37m-win_amd64.whl
   pip install pkg/window/certifi-2021.10.8-py2.py3-none-any.whl
   pip install pkg/window/charset_normalizer-2.0.9-py3-none-any.whl
   pip install pkg/window/click-8.0.3-py3-none-any.whl
   pip install pkg/window/cx_Oracle-8.3.0-cp39-cp39-win_amd64.whl

rem Запкскаем сервер
python app.py 5001


