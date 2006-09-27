Summary:	Framework for developing Web applications in Python
Summary(pl):	Szkielet do tworzenia aplikacji WWW w Pythonie
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

%description -l pl
Quixote to kolejny szkielet do tworzenia aplikacji WWW w Pythonie.
Projekt mia³ na celu:
- pozwoliæ na ³atwe tworzenie aplikacji WWW tam, gdzie jest wiêkszy
  nacisk na skomplikowan± logikê programu ni¿ skomplikowane szablony
- uczyniæ jêzyk szablonów podobnym do Pythona na ile to tylko mo¿liwe,
  zarówno pod wzglêdem sk³adni jak i semantyki; celem jest
  umo¿liwienie korzystania z jak najwiêkszej czê¶ci bieg³o¶ci i
  technik strukturalnych u¿ywanych przy pisaniu normalnego kodu w
  Pythonie w aplikacjach WWW budowanych przy u¿yciu Quixote
- brak magii; je¶li nie jest oczywiste, co zrobiæ w danym przypadku,
  Quixote nie bêdzie zgadywa³.

Je¶li kto¶ patrzy na serwis WWW jak na program, a na strony jak na
procedury, Quixote mo¿e byæ narzêdziem dla niego. Je¶li patrzy na
serwis jako na gablotê, a ka¿d± stronê jako oddzielny obraz, Quixote
prawdopodobnie nie jest tym, czego szuka.

%package doc
Summary:	Documentation for quixote Python module
Summary(pl):	Dokumentacja do modu³u Pythona quixote
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc
This module contains documentation files for quixote Python module.

%description doc -l pl
Modu³ zawieraj±cy dokumentacjê dla modu³u Pythona quixote.

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
