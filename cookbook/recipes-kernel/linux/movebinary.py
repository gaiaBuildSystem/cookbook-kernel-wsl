#!/usr/bin/python3

import os
import shutil
import subprocess

# get the environment

ARCH = os.getenv('ARCH')
MACHINE = os.getenv('MACHINE')
BUILD_PATH = os.getenv('BUILD_PATH')
USER_PASSWD = os.getenv('USER_PASSWD')

# get the actual script path
_path = os.path.dirname(os.path.realpath(__file__))

LINUX_IMAGE = "vmlinuz"
LINUX_ARCH = os.getenv('ARCH')

if LINUX_ARCH == "linux/arm64":
    LINUX_ARCH = "arm64"
    LINUX_IMAGE = "Image"
elif LINUX_ARCH == "linux/amd64":
    LINUX_ARCH = "x86"
    LINUX_IMAGE = "bzImage"

os.environ['LINUX_ARCH'] = LINUX_ARCH

print("Deploying kernel binary to build deploy folder ...")

DEPLOY_PATH = f"{BUILD_PATH}/tmp/{MACHINE}/deploy"
# create the deploy folder
os.makedirs(DEPLOY_PATH, exist_ok=True)

# copy the kernel binary to the deploy folder
shutil.copy2(
    f"{BUILD_PATH}/tmp/{MACHINE}/linux/arch/{LINUX_ARCH}/boot/{LINUX_IMAGE}",
    f"{DEPLOY_PATH}/{LINUX_IMAGE}"
)

print("Kernel binary deployed successfully!")
