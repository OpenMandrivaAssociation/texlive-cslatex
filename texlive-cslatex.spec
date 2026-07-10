%global tl_name cslatex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for Czech/Slovak typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/cstex/base/cslatex.tar.gz
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cslatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(atbegshi)
Requires:	texlive(atveryend)
Requires:	texlive(cm)
Requires:	texlive(csplain)
Requires:	texlive(everyshi)
Requires:	texlive(firstaid)
Requires:	texlive(hyphen-base)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(latex)
Requires:	texlive(latex-fonts)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX support for Czech/Slovak typesetting

