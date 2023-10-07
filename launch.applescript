#!/usr/bin/osascript

set openfoam to (path to me as text) & "Contents:Resources:etc:openfoam"

tell application "Terminal"
    do script (quoted form of POSIX path of openfoam)
    activate
end tell
