
%define		_name	amaranth
%define		_subver	.8
Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0%{_subver}
Release:	2
License:	GPL
Group:		Themes
Source0:	http://download.freshmeat.net/themes/amaranth/%{_name}-default-%{_subver}.tar.gz
# Source0-md5:	6a7be5952e9286515523a486d3666260
Source1:	http://download.freshmeat.net/themes/amaranth/%{_name}-large-%{_subver}.tar.gz
# Source1-md5:	d4a29806def7739e642da8045e4f1bb2
URL:		http://www.kde-look.org/content/show.php?content=5895
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a smooth iconset for KDE.

%description -l pl.UTF-8
%{_name} to gładki motyw ikon do KDE.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}
%{__tar} xfz %{SOURCE1} -C $RPM_BUILD_ROOT%{_iconsdir}/Amaranth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/Amaranth
