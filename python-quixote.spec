
Summary:	Framework for developing Web applications in Python
Name:		Quixote
Version:	0.7a3
Release:	0.1
License:	CNRI
Group:		Development/Languages/Python
Source0:	http://www.mems-exchange.org/software/files/quixote/%{name}-%{version}.tar.gz
# Source0-md5:	448c83a2b221db7540309b1536c108cd
URL:		http://www.mems-exchange.org/software/quixote/
BuildRequires:	python-modules
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quixote is yet another framework for developing Web applications in
Python.  The design goals were:

1) To allow easy development of Web applications where the
   emphasis is more on complicated programming logic than
   complicated templating.

2) To make the templating language as similar to Python as possible,
   in both syntax and semantics.  The aim is to make as many of the
   skills and structural techniques used in writing regular Python
   code applicable to Web applications built using Quixote.

3) No magic.  When it's not obvious what to do in
   a certain case, Quixote refuses to guess.

If you view a web site as a program, and web pages as subroutines,
Quixote just might be the tool for you.  If you view a web site as a
graphic design showcase, and each web page as an individual work of art,
Quixote is probably not what you're looking for

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ ACKS CHANGES LICENSE README TODO
%{py_sitedir}/quixote/
