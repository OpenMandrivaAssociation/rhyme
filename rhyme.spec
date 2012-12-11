Summary:	A rhyming dictionary
Name:		rhyme
Version:	0.9
Release:	%mkrel 8
License:	GPL+
Group:		Databases
URL:		http://rhyme.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch:      rhyme-0.9-fix-format-errors.patch
BuildRequires:	python
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gdbm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A command-line based rhyming dictionary supporting about 127,000
English words.

%prep
%setup -q
%patch -p 1

# fix strange file perms
chmod 644 *

%build
make LIBS='-lgdbm -lreadline -lncurses' FLAGS='%{optflags}'

# Tue Dec 11 2001 Oden Eriksson
# I suppose it would be possible to do a devel package too,
# but that would require some additional code to keep the *.txt
# compressed...

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m 644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
install -m 644 words.db -D %{buildroot}%{_datadir}/%{name}/words.db
install -m 644 rhymes.db -D %{buildroot}%{_datadir}/%{name}/rhymes.db
install -m 644 multiple.db -D %{buildroot}%{_datadir}/%{name}/multiple.db

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9-8mdv2010.0
+ Revision: 442713
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-7mdv2009.1
+ Revision: 347906
- fix format errors
- drop useless patch, use make arguments instead

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9-6mdv2009.0
+ Revision: 260237
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9-5mdv2009.0
+ Revision: 248413
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9-3mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.9-3mdv2008.0
+ Revision: 81158
- rebuild and reintroduce for 2008
- clean spec, fix description
- Import rhyme



* Fri Jan 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9-2mdk
- rebuild for new readline

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9-1mdk
- 0.9
- fix deps

* Fri Apr 25 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.8-5mdk
- fix buildrequires, thanks to Stefan van der Eijks robot

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.8-4mdk
- build release

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8-3mdk
- rebuild for new readline

* Mon May 20 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.8-2mdk
- rebuilt with gcc3.1

* Tue Jan  1 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.8-1mdk
- new version

* Tue Dec 11 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.7-2mdk
- 0.7-1mdk was lost in cyberspace...

* Mon Dec 10 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.7-1mdk
- initial cooker contrib.
