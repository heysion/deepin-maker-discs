# deepin-maker-discs
deepin build  maker discs tools  platform

## init db
```
git clone https://github.com/heysion/deepin-maker-discs.git
cd deepin-maker-discs/dmd
python manager.py --initdir
python manager.py --initdb
```

## run

```
git clone https://github.com/heysion/deepin-maker-discs.git
cd deepin-maker-discs
virtualenv -p python3 env
source  env/bin/activate
cd /tmp
git clone https://github.com/heysion/deepin-auto-build.git
cd deepin-auto-build
python setup.py install
cd -
cd dmd/dmdweb/
pip install -r requirements.txt
python app.py
```

## test

chrome http://127.0.0.1:8000/newtask

