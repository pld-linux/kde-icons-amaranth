#$Revision: 1.2 $, $Date: 2003-08-01 14:12:54 $

%define         _name	amaranth
%define		_subver	.7
Summary:        KDE icons - %{_name}
Summary(pl):    Motyw ikon do KDE - %{_name}
Name:           kde-icons-%{_name}
Version:	0%{_subver}
Release:        1
License:        GPL
Group:          Themes
Source0:        http://download.freshmeat.net/themes/amaranth/%{_name}-default-%{_subver}.tar.gz
# Source0-md5:	2d33adea3a9435e5b2ad2671786deaa8
URL:		http://www.kde-look.org/content/show.php?content=5895
Requires:       kdelibs
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description
%{_name} is a smooth iconset for KDE.

%description -l pl
%{_name} to g³adki motyw ikon do KDE.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/Amaranth
