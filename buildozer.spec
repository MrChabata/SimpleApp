[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.3.0
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
android.sdk_path = /root/.buildozer/android/platform/android-sdk
android.ndk_path = /root/.buildozer/android/platform/android-ndk-r25b