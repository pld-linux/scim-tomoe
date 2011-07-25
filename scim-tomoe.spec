Summary:	Tomoe module for SCIM for handwritten input
Name:		scim-tomoe
Version:	0.6.0
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tomoe/%{name}-%{version}.tar.gz
# Source0-md5:	21207dad4ceb5c00651673ec3737e010
Patch0:		%{name}-gcc43-cstring.patch
URL:		http://tomoe.sourceforge.net/
BuildRequires:	perl(XML::Parser)
BuildRequires:	gettext
BuildRequires:	scim-devel
BuildRequires:	tomoe-devel >= %{version}
BuildRequires:	tomoe-gtk-devel >= %{version}
Requires:	scim
Requires:	tomoe >= %{version}
Requires:	tomoe-gtk >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-tomoe allows handwritten input of Chinese and Japanese characters
with tomoe using SCIM.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/scim-tomoe
%attr(755,root,root) %{_libdir}/scim-1.0/*/Helper/tomoe.so
%{_datadir}/scim/icons/scim-tomoe.png
