#!/bin/sh

mv transcript-curr.out transcript-old.out
~/minervaclient/mnvc transcript > transcript-curr.out
diff transcript-old.out transcript-curr.out
exit 0
