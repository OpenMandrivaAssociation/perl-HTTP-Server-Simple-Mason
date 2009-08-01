%define upstream_name    HTTP-Server-Simple-Mason
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module for an abstract baseclass for a standalone mason server
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-HTML-Mason 
BuildRequires:  perl-libwww-perl 
BuildRequires:  perl-HTTP-Server-Simple
BuildRequires:  perl-Hook-LexWrap
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module that contains a abstract baseclass for a standalone mason server.
This is based on HTTP::Server::Simple.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
