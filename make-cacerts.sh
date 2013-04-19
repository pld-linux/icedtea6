#!/bin/sh -e
#
# make-cacerts.sh
#
# based on:
#
# update-ca-certificates
#
# Copyright (c) 2003 Fumitoshi UKAI <ukai@debian.or.jp>
# Copyright (c) 2009 Philipp Kern <pkern@debian.org>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02111-1301,
# USA.
#

verbose=0
DESTDIR=
while [ $# -gt 0 ];
do
  case $1 in
  --verbose|-v)
  	verbose=1;;
  --destdir)
	DESTDIR=$2; shift;;
  --help|-h|*)
	echo "$0: [--verbose]"
	exit;;
  esac
  shift
done

CERTSCONF=$DESTDIR/etc/ca-certificates.conf
CERTSCONFD=$DESTDIR/etc/ca-certificates.d
CERTSDIR=$DESTDIR/usr/share/ca-certificates
LOCALCERTSDIR=$DESTDIR/etc/certs
CERTBUNDLE=$DESTDIR/etc/certs/ca-certificates.crt
ETCCERTSDIR=$DESTDIR/etc/openssl/certs

KEYSTORE=$PWD/cacerts
KEYTOOL=$PWD/openjdk.build/bin/keytool

# Adds a certificate to the list of trusted ones.
# Adds the certificate to the cacerts file
add() {
  CERT="$1"
  NAME="$2"
  ALIAS="$(echo "$NAME" | sed -e 's/.\(crt|pem\)$//' -e 's/ /_/g' \
                                                -e 's/[()]/=/g' -e 's/,/_/g')"

  if [ "$verbose" = 1 ] ; then
    echo "  adding '$CERT' as '$ALIAS'"
  fi
  if ! $KEYTOOL -noprompt -import -alias "$ALIAS" \
                -keystore $KEYSTORE -storepass 'changeit' \
                -file "$CERT" ; then
        echo "W: $NAME certification could not be added"
  fi 
}

cd $ETCCERTSDIR

for conf in $CERTSCONF $CERTSCONFD/*.conf; do
  # skip inexistent files (matched by glob)
  [ -f $conf ] || continue

  sed -e '/^$/d' -e '/^#/d' -e '/^!/d' $conf | while read crt
  do
    if test -f "$CERTSDIR/$crt"
    then
      add "$CERTSDIR/$crt" "$crt"
    elif test -f "$LOCALCERTSDIR/$crt"
    then
      add "$LOCALCERTSDIR/$crt" "$crt"
    else
      echo "W: $CERTSDIR/$crt or $LOCALCERTSDIR/$crt not found, but listed in $conf." >&2
      continue
    fi
  done
done

echo "done."

# vim:set et sw=2:

