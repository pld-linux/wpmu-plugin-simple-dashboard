%define		package	wpmu
%define		plugin	simple-dashboard
Summary:	WordPressMU plugin for simplifying the wordpress dashboard
Name:		wpmu-plugin-%{plugin}
Version:	1.3.4
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.wordpress.org/plugin/wpmu-simple-dashboard.zip
# Source0-md5:	1d10be8e4dc5d5d979e28e634d6eddbf
URL:		http://wordpress.org/extend/plugins/wpmu-simple-dashboard/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	wpmu >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgdir		%{_datadir}/wpmu
%define		wp_root		%{pkgdir}
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins
%define		_sysconfdir	/etc/webapps/wpmu

%define		_svnserver	svn+ssh://svn.delfi.net
%define		_svnroot	%{_svnserver}%{_svnprefix}
%define		_svnprefix	/wpmu/mu-plugins/%{plugin}
%define		_svnpath	trunk

%description
This plugin allows site admins to turn on and off the following
widgets on the WPMU dashboard (for all users):
- Primary Feed
- Secondary Feed
- Incoming Links
- Recent Comments
- Recent Drafts
- Plugins
- Quick Press
- Right Now

In addition, site admins can override the primary and secondary feeds.

%prep
%setup -qn wpmu-%{plugin}
%undos readme.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{wp_content},%{pluginsdir},%{_sysconfdir}}
cp -a cets_simple_dashboard.php $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt screenshot-*.png
%{pluginsdir}/*.php