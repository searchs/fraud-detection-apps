# Backwards-compat shim: re-export the canonical Commander implementation
# The real implementation lives in mysiri.commands; keep this module so other
# code that imports `mysiri.commander` continues to work.

from mysiri.commands import Commander  # noqa: F401
