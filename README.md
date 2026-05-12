A Python-based utility designed for high-speed mouse input simulation with randomized delay intervals. This tool is capable of achieving frequencies up to 150 clicks per second (CPS).
**⚠️ System Stability Warning**

Due to the extreme input velocity this script can generate, users must exercise caution. Rapid-fire input can overwhelm the operating system's UI thread, which may result in a system hang or the forced termination of Windows Explorer (explorer.exe). It is recommended to use this utility in a controlled environment.
**Features**

    High Performance: Optimized for burst rates of up to 150 CPS.

    Stochastic Timing: Implements randomized intervals to simulate more natural input patterns.

    Open Source: The codebase is fully modular; users are encouraged to fork and modify the logic to suit their specific requirements.

**Prerequisites & Installation**

This application requires Python 3.x and specific external libraries to interface with system hardware. The script will remain non-functional until these dependencies are satisfied.
**Required Modules**

    pyautogui: Facilitates programmatic mouse control.

    keyboard: Enables global hotkey monitoring for starting and stopping the script.

**Installation Command**

Execute the following command in your terminal or command prompt:

*pip install pyautogui keyboard*

**Usage:**

    Ensure all dependencies are installed.

    Run the script via your preferred Python interpreter.

    Use the designated hotkeys to toggle the clicking mechanism.
