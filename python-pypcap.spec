Summary:	Simplified object-oriented Python extension module for libpcap
Name:		python-pypcap
Version:	1.1
Release:	%mkrel 5
License:	BSD
Group:		Development/Python
URL:		http://monkey.org/~dugsong/pypcap/
Source0:	http://monkey.org/~dugsong/pypcap/pypcap-%{version}.tar.bz2
Patch0:		pypcap-1.1-lib64.diff
BuildRequires:	python-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Simplified object-oriented Python extension module for libpcap - 
the current tcpdump.org version, the legacy version shipping with
some of the BSD operating systems, and the WinPcap port for
Windows.

%prep

%setup -q -n pypcap-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" python setup.py config
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%doc CHANGES LICENSE README
%defattr(-,root,root)


