quasar build
cd cordova
cordova prepare ios
python3 ../preprocess.py
cordova run ios
cd ..
