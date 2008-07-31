%define realname   HTTP-Server-Simple-Mason

Name:		perl-%{realname}
Version:        0.09
Release:        %mkrel 8
License:	GPL or Artistic
Group:		Development/Perl
Summary:        Module for an abstract baseclass for a standalone mason server
Source0:        http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl-HTML-Mason 
BuildRequires:  perl-libwww-perl 
BuildRequires:  perl-HTTP-Server-Simple
BuildRequires:  perl-Hook-LexWrap
BuildArch:      noarch

%description
Perl module that contains a abstract baseclass for a standalone mason server.
This is based on HTTP::Server::Simple.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*

