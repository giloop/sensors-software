
Import("env")
import os
import shutil
import configparser
from base64 import b64decode

# uncomment line below to see environment variables
# print('----\nenv.Dump() : \n------------------------')
# print(env.Dump())
# print('----\nARGUMENTS : \n------------------------')
# print(ARGUMENTS)
# print(b64decode(ARGUMENTS.get("PROJECT_CONFIG", 1)))

# Get langage in config file (b64decode(ARGUMENTS.get("LANG")) not working)
config = configparser.ConfigParser()
config.read(env['PROJECT_CONFIG'])
lang = config['platformio']['lang']

def after_build(source, target, env):
  if not os.path.exists("./builds"):
    os.mkdir("./builds")
  shutil.copy(target[0].path, "./builds/latest_"+lang+".bin")

env.AddPostAction("$BUILD_DIR/firmware.bin", after_build)
