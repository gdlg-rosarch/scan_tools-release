# Script generated with Bloom
pkgdesc="ROS - The laser_ortho_projector package calculates orthogonal projections of LaserScan messages."
url='http://wiki.ros.org/laser_scan_matcher'

pkgname='ros-kinetic-laser-ortho-projector'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pcl'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

depends=('pcl'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=laser_ortho_projector
source=()
md5sums=()

prepare() {
    cp -R $startdir/laser_ortho_projector $srcdir/laser_ortho_projector
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

