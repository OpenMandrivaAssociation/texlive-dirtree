# revision 19882
# category Package
# catalog-ctan /macros/generic/dirtree
# catalog-date 2009-04-10 11:30:41 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-dirtree
Version:	0.2
Release:	1
Summary:	Display trees in the style of windows explorer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/dirtree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is designed to emulate the way windows explorer
displays directory and file trees, with the root at top left,
and each level of subtree displaying one step in to the right.
The macros work equally well with Plain TeX and with LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
