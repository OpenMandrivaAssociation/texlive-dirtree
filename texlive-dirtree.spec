# revision 28524
# category Package
# catalog-ctan /macros/generic/dirtree
# catalog-date 2012-12-13 10:43:21 +0100
# catalog-license lppl
# catalog-version 0.32
Name:		texlive-dirtree
Version:	0.32
Release:	5
Summary:	Display trees in the style of windows explorer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/dirtree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed to emulate the way windows explorer
displays directory and file trees, with the root at top left,
and each level of subtree displaying one step in to the right.
The macros work equally well with Plain TeX and with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dirtree/dirtree.sty
%{_texmfdistdir}/tex/generic/dirtree/dirtree.tex
%doc %{_texmfdistdir}/doc/generic/dirtree/README
%doc %{_texmfdistdir}/doc/generic/dirtree/dirtree.pdf
#- source
%doc %{_texmfdistdir}/source/generic/dirtree/dirtree.dtx
%doc %{_texmfdistdir}/source/generic/dirtree/dirtree.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
