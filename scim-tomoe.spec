Summary:	Tomoe module for SCIM for handwritten input
Summary(pl.UTF-8):	Moduł SCIM tomoe pozwalający na wprowadzanie pisma ręcznego
Name:		scim-tomoe
Version:	0.6.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tomoe/%{name}-%{version}.tar.gz
# Source0-md5:	21207dad4ceb5c00651673ec3737e010
Patch0:		%{name}-gcc43-cstring.patch
URL:		http://tomoe.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.2.0
BuildRequires:	tomoe-devel >= %{version}
BuildRequires:	tomoe-gtk-devel >= %{version}
Requires:	gtk+2 >= 2:2.4.0
Requires:	scim >= 1.2.0
Requires:	tomoe >= %{version}
Requires:	tomoe-gtk >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-tomoe allows handwritten input of Chinese and Japanese characters
with tomoe using SCIM.

%description -l pl.UTF-8
Scim-tomoe pozwala na wprowadzanie ręcznie pisanych znaków chińskich i
japońskich przy użyciu biblioteki tomoe poprzez SCIM.

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/scim-tomoe
%attr(755,root,root) %{_libdir}/scim-1.0/*/Helper/tomoe.so
%{_datadir}/scim/icons/scim-tomoe.png
