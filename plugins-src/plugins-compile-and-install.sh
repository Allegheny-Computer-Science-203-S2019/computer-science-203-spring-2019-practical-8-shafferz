# NOTE: You should run this script from the plugins-src/ directory
python3 -m compileall .
mkdir -p ../plugins
cp __pycache__/*.pyc ../plugins
mv ../plugins/frequencies1.cpython-36.pyc ../plugins/frequencies1.pyc
# TODO: move the second frequencies plugin
mv ../plugins/words1.cpython-36.pyc ../plugins/words1.pyc
# TODO: move the second words plugin
mv ../plugins/words2.cpython-36.pyc ../plugins/words2.pyc
