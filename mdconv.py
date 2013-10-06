#!/usr/bin/python
import glob
import markdown
import sys

def openFile(path, mode):
    # check python version so we always open UTF-8.
    if sys.version_info[0] == 2:
        import codecs
        return codecs.open(path, mode, "utf-8")
    else:
        return open(path, mode, encoding="utf-8")

def convert(fn):
    # make the new filename
    newfn = fn[:-3]+".html"

    print("[CONV] %s => %s" % (fn, newfn))

    # open and read the md file
    try:
        mdfile = openFile(fn,"r")
    except IOError:
        print("[NOPE] File %s doesn't exist, are you mad!?" % fn)
        sys.exit(1)

    mdtext = mdfile.read()

    # convert it
    html = markdown.markdown(mdtext)

    # close it
    mdfile.close()

    # write the new html
    htmlfile = openFile(newfn,"w")
    htmlfile.write(header+"\n\n"+html+"\n\n"+footer)
    htmlfile.close()

# get the header/footer
try:
    hfile = openFile(".mdc_header","r")
except IOError:
    hfile = None

try:
    ffile = openFile(".mdc_footer","r")
except IOError:
    ffile = None

if hfile is None:
    header = "<!doctype html>"
else:
    header = hfile.read()
    hfile.close()

if ffile is None:
    footer = ""
else:
    footer = ffile.read()
    ffile.close()

# figure out if it's a full-on convert or just a single file
try:
    target = sys.argv[1:]
except IndexError:
    target = None

if target is None or target == []:
    print("[INFO] Converting all files in cwd")
    for f in glob.glob("*.md"):
        convert(f)
else:
    print("[INFO] Converting selected file(s)")
    for t in target:
        for f in glob.glob(t):
            convert(f)
