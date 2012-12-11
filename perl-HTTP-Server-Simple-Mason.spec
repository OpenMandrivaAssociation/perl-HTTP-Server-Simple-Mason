%define upstream_name    HTTP-Server-Simple-Mason
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Module for an abstract baseclass for a standalone mason server
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Mason)
BuildRequires:	perl-libwww-perl 
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(Hook::LexWrap)
BuildArch:	noarch

%description
Perl module that contains a abstract baseclass for a standalone mason server.
This is based on HTTP::Server::Simple.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 596557
- update to new version 0.14

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 461290
- update to 0.13

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 406065
- rebuild using %%perl_convert_version

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2010.0
+ Revision: 393524
- update to new version 0.12

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 309308
- update to new version 0.11

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-8mdv2009.0
+ Revision: 257255
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.09-6mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Michael Scherer <misc@mandriva.org> 0.09-6mdv2008.0
+ Revision: 81721
- rebuild for 2008


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.09-5mdk
- Do not ship empty dir

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-4mdk
- Fix BuildRequires

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-3mdk
- Fix BuildRequires

* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 0.09-2mdk
- Fix BuildRequires

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.09-1mdk
- First mandriva package

