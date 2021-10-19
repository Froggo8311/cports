pkgname = "base-minimal"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "base-files", "musl", "apk-tools", "bsdutils", "bsddiff", "bsdgrep",
    "bsdsed", "bsded", "bsdgzip", "bsdtar", "dash", "awk", "util-linux",
    "shadow", "procps-ng", "iana-etc", "tzdata",
]
pkgdesc = "Minimal set of packages for a Chimera system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# TODO: dinit-chimera
