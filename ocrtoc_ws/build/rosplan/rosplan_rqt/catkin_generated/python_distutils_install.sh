#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/kaushik/ocrtoc_ws/src/rosplan/rosplan_rqt"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/kaushik/ocrtoc_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/kaushik/ocrtoc_ws/install/lib/python2.7/dist-packages:/home/kaushik/ocrtoc_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/kaushik/ocrtoc_ws/build" \
    "/usr/bin/python2" \
    "/home/kaushik/ocrtoc_ws/src/rosplan/rosplan_rqt/setup.py" \
     \
    build --build-base "/home/kaushik/ocrtoc_ws/build/rosplan/rosplan_rqt" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/kaushik/ocrtoc_ws/install" --install-scripts="/home/kaushik/ocrtoc_ws/install/bin"
