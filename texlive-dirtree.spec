%global tl_name dirtree
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.32
Release:	%{tl_revision}.1
Summary:	Display trees in the style of windows explorer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/dirtree
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtree.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is designed to emulate the way windows explorer displays
directory and file trees, with the root at top left, and each level of
subtree displaying one step in to the right. The macros work equally
well with Plain TeX and with LaTeX.

