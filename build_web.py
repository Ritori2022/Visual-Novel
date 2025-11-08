#!/usr/bin/env python3
"""
Manual web build script for Ren'Py projects
"""

import os
import sys
import shutil
import zipfile
import subprocess

# Configuration
RENPY_SDK = os.path.abspath("./renpy-8.4.1-sdk")
PROJECT_DIR = os.path.abspath("./vortex_and_firefly")
OUTPUT_DIR = os.path.abspath("./web-dist")
RENPY_BIN = os.path.join(RENPY_SDK, "renpy.sh")

def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def main():
    print("=" * 60)
    print("Ren'Py Web Build Script")
    print("=" * 60)

    # Check if SDK exists
    if not os.path.exists(RENPY_SDK):
        print(f"ERROR: Ren'Py SDK not found at {RENPY_SDK}")
        return 1

    # Check if project exists
    if not os.path.exists(PROJECT_DIR):
        print(f"ERROR: Project not found at {PROJECT_DIR}")
        return 1

    print(f"\nSDK: {RENPY_SDK}")
    print(f"Project: {PROJECT_DIR}")
    print(f"Output: {OUTPUT_DIR}")

    # Method 1: Try the official launcher web_build command
    print("\n" + "=" * 60)
    print("Attempting Method 1: launcher web_build")
    print("=" * 60)

    # Set environment variables to disable graphics
    env = os.environ.copy()
    env['SDL_VIDEODRIVER'] = 'dummy'
    env['SDL_AUDIODRIVER'] = 'dummy'
    env['RENPY_SIMPLE_EXCEPTIONS'] = '1'

    cmd = [
        RENPY_BIN,
        os.path.join(RENPY_SDK, "launcher"),
        "web_build",
        PROJECT_DIR,
        "--dest", OUTPUT_DIR
    ]

    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode == 0 and os.path.exists(OUTPUT_DIR):
        print(f"\n✓ Success! Web build created at: {OUTPUT_DIR}")
        return 0

    # Method 2: Try distribute command with web package
    print("\n" + "=" * 60)
    print("Attempting Method 2: distribute --package web")
    print("=" * 60)

    cmd = [
        RENPY_BIN,
        PROJECT_DIR,
        "distribute",
        "--package", "web",
        "--dest", os.path.dirname(OUTPUT_DIR)
    ]

    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if result.returncode == 0:
        print(f"\n✓ Success! Distribution created")
        return 0

    print("\n✗ Web build failed")
    print("\nTroubleshooting:")
    print("1. Check that script.rpy has no syntax errors")
    print("2. Run lint: ./renpy-8.4.1-sdk/renpy.sh ./vortex_and_firefly lint")
    print("3. Check Ren'Py version compatibility")

    return 1

if __name__ == "__main__":
    sys.exit(main())
