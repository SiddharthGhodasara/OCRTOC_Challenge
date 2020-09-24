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

echo_and_run cd "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/description/robotiq_85_gripper-master/robotiq_85_driver"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/install/lib/python2.7/dist-packages:/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build" \
    "/usr/bin/python2" \
    "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/src/description/robotiq_85_gripper-master/robotiq_85_driver/setup.py" \
     \
    build --build-base "/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/build/description/robotiq_85_gripper-master/robotiq_85_driver" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/install" --install-scripts="/home/gaurav/NEW/OCRTOC_Challenge/ocrtoc_ws/install/bin"
