
Import("env")
import os
import shutil
from base64 import b64decode

def after_build(source, target, env):
    # print(ARGUMENTS)
    print(env.Dump())
    shutil.copy(target[0].path, "./builds/latest_"+b64decode(ARGUMENTS.get("LANG"))+".bin")


env.AddPostAction("$BUILD_DIR/firmware.bin", after_build)
