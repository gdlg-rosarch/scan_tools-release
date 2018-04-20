# Script generated with Bloom
pkgdesc="ROS - The laser_scan_sparsifier takes in a LaserScan message and sparsifies it."
url='http://wiki.ros.org/laser_scan_matcher'

pkgname='ros-kinetic-laser-scan-sparsifier'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=laser_scan_sparsifier
source=()
md5sums=()

prepare() {
    cp -R $startdir/laser_scan_sparsifier $srcdir/laser_scan_sparsifier
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

