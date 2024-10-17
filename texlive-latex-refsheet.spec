Name:		texlive-latex-refsheet
Version:	45076
Release:	2
Summary:	LaTeX Reference Sheet for a thesis with KOMA-Script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-refsheet
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-refsheet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-refsheet.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX Reference Sheet is for writing a thesis using the
KOMA-Script document classes (scrartcl, scrreprt, scrbook) and
all the packages needed for a thesis in natural sciences.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex-refsheet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
