%define product		mxmCounter
%define version		1.1.0
%define release		4

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	A simple filesystem based hit counter for Zope, CMF & Plone, for multiple pages
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://www.mxm.dk/products/public/mxmCounter/files/mxmCounter.%{version}.tar.bz2
URL:		http://www.mxm.dk/products/public/mxmCounter/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*



