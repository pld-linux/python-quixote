Summary:	Framework for developing Web applications in Python
Summary(pl.UTF-8):	Szkielet do tworzenia aplikacji WWW w Pythonie
Name:		python-quixote
Version:	2.4
Release:	2
Epoch:		1
License:	CNRI
Group:		Development/Languages/Python
Source0:	http://www.mems-exchange.org/software/files/quixote/Quixote-%{version}.tar.gz
# Source0-md5:	5dc36613faba7dee6c8c6d24c1334303
URL:		http://www.mems-exchange.org/software/quixote/
BuildRequires:	python-modules
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Obsoletes:	Quixote
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quixote is yet another framework for developing Web applications in
Python. The design goals were:
- To allow easy development of Web applications where the
  emphasis is more on complicated programming logic than
  complicated templating.
- To make the templating language as similar to Python as possible,
  in both syntax and semantics. The aim is to make as many of the
  skills and structural techniques used in writing regular Python
  code applicable to Web applications built using Quixote.
- No magic. When it's not obvious what to do in
  a certain case, Quixote refuses to guess.

If you view a web site as a program, and web pages as subroutines,
Quixote just might be the tool for you. If you view a web site as a
graphic design showcase, and each web page as an individual work of art,
Quixote is probably not what you're looking for.

%description -l pl.UTF-8
Quixote to kolejny szkielet do tworzenia aplikacji WWW w Pythonie.
Projekt miał na celu:
- pozwolić na łatwe tworzenie aplikacji WWW tam, gdzie jest większy
  nacisk na skomplikowaną logikę programu niż skomplikowane szablony
- uczynić język szablonów podobnym do Pythona na ile to tylko możliwe,
  zarówno pod względem składni jak i semantyki; celem jest
  umożliwienie korzystania z jak największej części biegłości i
  technik strukturalnych używanych przy pisaniu normalnego kodu w
  Pythonie w aplikacjach WWW budowanych przy użyciu Quixote
- brak magii; jeśli nie jest oczywiste, co zrobić w danym przypadku,
  Quixote nie będzie zgadywał.

Jeśli ktoś patrzy na serwis WWW jak na program, a na strony jak na
procedury, Quixote może być narzędziem dla niego. Jeśli patrzy na
serwis jako na gablotę, a każdą stronę jako oddzielny obraz, Quixote
prawdopodobnie nie jest tym, czego szuka.

%package doc
Summary:	Documentation for quixote Python module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona quixote
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc
This module contains documentation files for quixote Python module.

%description doc -l pl.UTF-8
Moduł zawierający dokumentację dla modułu Pythona quixote.

%prep
%setup -q -n Quixote-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS CHANGES LICENSE README TODO
%dir %{py_sitedir}/quixote
%dir %{py_sitedir}/quixote/demo
%dir %{py_sitedir}/quixote/form
%dir %{py_sitedir}/quixote/html
%dir %{py_sitedir}/quixote/ptl
%dir %{py_sitedir}/quixote/server

%attr(755,root,root) %{py_sitedir}/quixote/*/*.so

%{py_sitedir}/quixote/*.py[co]
%{py_sitedir}/quixote/*/*.py[co]
%{py_sitedir}/quixote/demo/*.ptl

%files doc
%defattr(644,root,root,755)
%doc doc/*
