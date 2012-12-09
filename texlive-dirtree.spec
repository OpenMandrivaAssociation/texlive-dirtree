# revision 19882
# category Package
# catalog-ctan /macros/generic/dirtree
# catalog-date 2009-04-10 11:30:41 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-dirtree
Version:	0.2
Release:	2
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 750999
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718236
- texlive-dirtree
- texlive-dirtree
- texlive-dirtree
- texlive-dirtree

