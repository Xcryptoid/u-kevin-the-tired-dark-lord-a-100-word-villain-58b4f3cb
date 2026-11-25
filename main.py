import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))

# The monologue itself was written before this program ever runs, so
# this script does no writing of its own: it only carries the finished
# text into the folder the judge reads, making that folder first when
# it is missing, and the words arrive exactly as they were written.
