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
