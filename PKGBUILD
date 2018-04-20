# Script generated with Bloom
pkgdesc="ROS - Laser scan processing tools."
url='http://ros.org/wiki/scan_tools'

pkgname='ros-kinetic-scan-tools'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
'LGPLv3'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-laser-ortho-projector'
'ros-kinetic-laser-scan-matcher'
'ros-kinetic-laser-scan-sparsifier'
'ros-kinetic-laser-scan-splitter'
'ros-kinetic-ncd-parser'
'ros-kinetic-polar-scan-matcher'
'ros-kinetic-scan-to-cloud-converter'
)

conflicts=()
replaces=()

_dir=scan_tools
source=()
md5sums=()

prepare() {
    cp -R $startdir/scan_tools $srcdir/scan_tools
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

