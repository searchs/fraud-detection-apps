# Backwards-compat shim: transcriber functionality was consolidated into
# mysiri.audio. Re-export public names so existing imports keep working.

from mysiri.audio import *  # noqa: F401,F403
