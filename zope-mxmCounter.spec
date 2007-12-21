%define Product mxmCounter
%define product mxmcounter
%define name    zope-%{Product}
%define version 1.1.0
%define release %mkrel 5

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A simple filesystem based hit counter for Zope, CMF & Plone, for multiple pages
License:	GPL
Group:		System/Servers
URL:		http://www.mxm.dk/products/public/mxmCounter/
Source:		http://www.mxm.dk/products/public/mxmCounter/files/mxmCounter.%{version}.tar.bz2
Requires:	zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
A simple filesystem based hit counter for Zope, 
CMF & Plone, for multiple pages.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
