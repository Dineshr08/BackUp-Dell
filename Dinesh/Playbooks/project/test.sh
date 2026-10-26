seq 2 | xargs -P0 -n1 timeout 10 md5sum /dev/zero
