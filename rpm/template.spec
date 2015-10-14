Name:           ros-indigo-scan-to-cloud-converter
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS scan_to_cloud_converter package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/laser_scan_matcher
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl
Requires:       pcl-tools
Requires:       ros-indigo-pcl-conversions
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp

%description
Converts LaserScan to PointCloud messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 14 2015 Ivan Dryanovski <ccnyroboticslab@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

