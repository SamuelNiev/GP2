#!/usr/bin/env python3

import os
import subprocess
cmd = "streamlit run /home/admin/GP2-Projektarbeit/Home.py"

cmdarray = cmd.split()
shell_cmd = subprocess.run(cmdarray)

mainloop()



