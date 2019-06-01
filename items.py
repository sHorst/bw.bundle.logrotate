pkg_apt = {
    "logrotate": {},
}

files = {
    "/etc/logrotate.d/syslog-ng": {
        'delete': True,
    },
}
